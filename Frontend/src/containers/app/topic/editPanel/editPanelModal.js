import React from 'react';

import ReactDOM from 'react-dom'

import {connect} from 'react-redux';

import DeletionWarningModal from './deletionWarningModal';

import {Api} from './../../../../djangoApi';

import {deleteTopic, changeTopicName, changeTopicPositions, changeTopicAndPosition} from './../../../../modules/board'



const ModalRoot = document.querySelector('#modal-root')

//A lot of the modal boilerplate code is the same as in our other modals. I wonder if there would be a way to fix this??

//Perhaps we could have a Modal class that modals we want to make can inherit from. Not sure if subclassing like that is frowned upon in React.



class EditPanelModal extends React.Component{
  constructor(props) {
    super(props)
    this.state = {
      name : this.props.board[this.props.id].Data.Name,
      switchPosition: -Infinity,
      switchDropdownOpen: false,
      deletionWarningModalOpen: false
    }

    this.el = document.createElement('div');
    this.editPanelModalRef = React.createRef();
  }

  componentWillMount() {
    ModalRoot.appendChild(this.el)
    this.listenerLoader()
    // document.addEventListener("mousedown", this.handleClickOutside)

  }

  componentWillUnmount() {
    ModalRoot.removeChild(this.el)
    this.listenerUnLoader()
    // document.removeEventListener("mousedown", this.handleClickOutside)
  }


  listenerLoader = () => {
    document.addEventListener("mousedown", this.handleClickOutside)

  }

  listenerUnLoader = () => {
    document.removeEventListener("mousedown", this.handleClickOutside)
    
  }

  handleClickOutside = (e) =>  {
    if (!this.editPanelModalRef.current.contains(e.target)) {
      this.props.closeModal();

    }
  }

  nameChange = (e) => {
    this.setState({name: e.target.value})
  }

  switchDropdown= () => {
    this.setState({switchDropdownOpen: true})

  }

  setSwitchPostion= (e) => {

    this.setState({switchPosition: e.target.value})
    this.setState({switchDropdownOpen: false})

  }

  clearSwitchPosition = () => {

    this.setState({switchPosition: -Infinity})
    this.setState({switchDropdownOpen: true})

  }

  handleDeletionModalOpen = () => {

    this.setState({deletionWarningModalOpen: true})
  }

  handleDeletionModalClose = () => {

    this.setState({deletionWarningModalOpen: false})
  }

  handleDeletion = () => {
    Api().delete(`/topic/${this.props.board[this.props.id].Data.id}/`)
    .then((res) => {
      if (res.status === 204) {
        this.props.closeModal()
        
        let temp = Object.assign({}, this.props.board);

        delete temp[this.props.id]

        this.props.deleteTopic(temp)
        //Call our redux deletion
      }
    })
    .catch((err) => {
      console.log('err', err)
    })


    //Make a call to delete the topic. 
  }

  saveChanges = () => {
    //If nothing has changed.

    if (this.state.name === this.props.board[this.props.id].Data.Name && this.state.switchPosition === -Infinity ) {
      //Nothing has happened.

      this.props.closeModal();
    }

    //Only the name has changed.

    if (this.state.name !== this.props.board[this.props.id].Data.Name && this.state.switchPosition === -Infinity) {


      Api().put(`/topic/${this.props.board[this.props.id].Data.id}/`, {Name: this.state.name})
      .then((res) => {
        //Update the store. 
        if (res.status === 200) {
          this.props.changeTopicName(this.state.name, this.props.id)
        }
      })
      .then(() => {
        this.props.closeModal()
      })
      .catch((err) => {
        console.log(err)
      })
    }

    //Only a position change.
    
    let position = this.props.board[this.state.switchPosition].Data.id


    if(this.state.name === this.props.board[this.props.id].Data.Name && this.state.switchPosition !== -Infinity ) {

      Api().put(`/topic/${this.props.board[this.props.id].Data.id}/`, { switchPosition: position})
      .then((res) => {
        if (res.status === 200) {
          this.props.changeTopicPositions(this.props.id, this.state.switchPosition)
        }
      })
      .then(() => {
        this.props.closeModal()
      })
      .catch((err) => {
        console.log(err)
      })
    }

    //Both have changed.

    if(this.state.name !== this.props.board[this.props.id].Data.Name && this.state.switchPosition !== -Infinity) {
      console.log('both change')

      Api().put( `/topic/${this.props.board[this.props.id].Data.id}/`, {Name: this.state.name, switchPosition: this.state.switchPosition})
      .then((res) => {
        if (res.status === 200) {
          this.props.changeTopicAndPosition(this.state.name, this.props.id, this.props.id, this.state.switchPosition)
        }
      })
      .then(() => {
        this.props.closeModal()
      })
      .catch((err) => {
        console.log(err)
      })

    }

  }


  render() {

    let dropDown = <option onClick = {this.switchDropdown} > Select Topic  </option>
    
    
    let dropDownClear = null;
    
    if(this.state.switchDropdownOpen === true) {
      dropDown = []
      for (let key in this.props.board) {

        if(key !== this.props.id) {
          dropDown.push(<li value = {key} onClick = {(e) => this.setSwitchPostion(e)} > {this.props.board[key].Data.Name} </li> )
        }     
      }

    }

    if(this.state.switchDropdownOpen === false && this.state.switchPosition !== -Infinity) {
     
      dropDownClear = <div onClick = {this.clearSwitchPosition} > Clear </div>
      dropDown =  <li onClick = {this.switchDropdown}  > {this.props.board[this.state.switchPosition].Data.Name} </li>
    }



    let deleteModal = null;

    if(this.state.deletionWarningModalOpen === true) {
      deleteModal = <DeletionWarningModal loadParentListener = {this.listenerLoader} unloadParentListener ={this.listenerUnLoader} closeModal ={this.handleDeletionModalClose} handleDeletion = {this.handleDeletion} />
    }


  
    return ReactDOM.createPortal(
      <div className = 'editPanelModal' ref = {this.editPanelModalRef}> 
        <input className = 'editPanelNameChange' onChange = {(e) => this.nameChange(e)} value = {this.state.name} />

        <p>Change Position with another Topic</p>

        <ul>
          {dropDown}
        </ul>

        <p onClick = {this.handleDeletionModalOpen}>Delete this Topic</p>

        {dropDownClear}

        {deleteModal}

        <button onClick = {this.saveChanges}> Save </button>
        <button onClick = {this.props.closeModal}> Cancel </button>

      </div>, 
      this.el
    )
  }

}

function mapStateToProps(state) {
  return {
    board: state.board.board


  }
}

const matchDispatchToProps = {
  deleteTopic,
  changeTopicName,
  changeTopicPositions,
  changeTopicAndPosition
}



export default connect(mapStateToProps, matchDispatchToProps) (EditPanelModal);