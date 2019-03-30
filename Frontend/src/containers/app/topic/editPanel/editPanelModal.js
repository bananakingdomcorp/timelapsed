import React from 'react';

import ReactDOM from 'react-dom'

import {connect} from 'react-redux';

import DeletionWarningModal from './deletionWarningModal';


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
    document.addEventListener("mousedown", this.handleClickOutside)

  }

  componentWillUnmount() {
    ModalRoot.removeChild(this.el)
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

  switchDropdown() {
    this.setState({switchDropdown: true})

  }

  setSwitchPostion= (e) => {
    this.setState({setSwitchPostion: e.target.value})
    this.setState({switchDropdownOpen: false})

  }

  handleDeletionModalOpen() {

    this.setState({deletionWarningModalOpen: true})
  }

  handleDeletionModalClose() {

    this.setState({deletionWarningModalOpen: false})
  }

  handleDeletion() {
    //Make a call to delete the topic. 
  }


  render() {

    let dropDown = <option onClick = {this.switchDropdown} > Select Topic  </option>

    if(this.state.switchDropdownOpen === true) {
      dropDown = []
      for (let key in this.props.board) {
        dropDown.push(<li value = {this.props.board} onClick = {(e) => this.setSwitchPostion(e.target.value)} > {this.props.board[key][0]} </li> )
      }

    }

    if(this.state.switchDropdownOpen === false && this.state.switchPosition !== -Infinity) {
      dropDown =  <li onClick = {this.switchDropdown} > {this.props.board[this.state.switchPosition][0]} </li>
    }

    let deleteModal = null;

    if(this.state.deletionWarningModalOpen === true) {
      deleteModal = <DeletionWarningModal closeModal ={this.handleDeletionModalClose} handleDeletion = {this.handleDeletion} />
    }


  
    return ReactDOM.createPortal(
      <div className = 'editPanelModal' ref = {this.editPanelModalRef}> 
        <input className = 'editPanelNameChange' onChange = {(e) => this.nameChange(e.target.value)} value = {this.state.name} />

        <p>Change Position with another Topic</p>

        <ul>
          {this.dropdown}
        </ul>

        {deleteModal}

      </div>
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