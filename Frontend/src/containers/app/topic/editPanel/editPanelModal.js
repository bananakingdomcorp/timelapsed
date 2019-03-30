import React from 'react';

import ReactDOM from 'react-dom'

import {connect} from 'react-redux';

import DeletionWarningModal from './deletionWarningModal';

import {Api} from './../../../../djangoApi';



const ModalRoot = document.querySelector('#modal-root')

//A lot of the modal boilerplate code is the same as in our other modals. I wonder if there would be a way to fix this??

//Perhaps we could have a Modal class that modals we want to make can inherit from. Not sure if subclassing like that is frowned upon in React.



class EditPanelModal extends React.Component{
  constructor(props) {
    super(props)
    this.state = {
      name : this.props.board[this.props.id][0],
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
    console.log('herrrr')
    Api().delete('topic', {id: this.props.id})
    .then((res) => {
      console.log(res);
      if (res.status === 200) {
        //Call our redux deletion
      }
    })


    //Make a call to delete the topic. 
  }

  saveChanges = () => {



  }


  render() {

    let dropDown = <option onClick = {this.switchDropdown} > Select Topic  </option>
    
    
    let dropDownClear = null;
    
    if(this.state.switchDropdownOpen === true) {
      dropDown = []
      for (let key in this.props.board) {

        if(key !== this.props.id) {
          dropDown.push(<li value = {key} onClick = {(e) => this.setSwitchPostion(e)} > {this.props.board[key][0]} </li> )
        }     
      }

    }

    if(this.state.switchDropdownOpen === false && this.state.switchPosition !== -Infinity) {
     
      dropDownClear = <div onClick = {this.clearSwitchPosition} > Clear </div>
      dropDown =  <li onClick = {this.switchDropdown}  > {this.props.board[this.state.switchPosition][0]} </li>
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

}



export default connect(mapStateToProps, matchDispatchToProps) (EditPanelModal);