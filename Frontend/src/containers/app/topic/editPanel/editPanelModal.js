import React from 'react';

import ReactDOM from 'react-dom'

import {connect} from 'react-redux';


const ModalRoot = document.querySelector('#modal-root')

//A lot of the modal boilerplate code is the same as in our other modals. I wonder if there would be a way to fix this??

//Perhaps we could have a Modal class that modals we want to make can inherit from. Not sure if subclassing like that is frowned upon in React.



class EditPanelModal extends React.Component{
  constructor(props) {
    super(props)
    this.state = {
      name : this.props.board[this.props.id][0],
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


  render() {
    

    return ReactDOM.createPortal(
      <div className = 'editPanelModal' ref = {this.editPanelModalRef}> 
        


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