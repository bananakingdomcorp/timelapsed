import React from 'react';
import ReactDom from 'react-dom'

const ModalRoot = document.querySelector('#modal-root-two')


class DeletionWarningModal extends React.Component{
  constructor(props) {
    super(props)


    this.el = document.createElement('div');
    this.deleteWarningModalRef = React.createRef();
  }

  //Not sure right now if the mousedown will work correctly or not. 

  
  componentWillMount() {
    ModalRoot.appendChild(this.el)
    this.props.unloadParentListener()

  }

  componentWillUnmount() {
    ModalRoot.removeChild(this.el)
    this.props.loadParentListener()
  }


  render() {
    return ReactDom.createPortal(
      <div>
        Are you sure that you want to delete this topic?Are
        
        Any cards within this topic will be removed. 

       <p> Warning: If you have a lot of active cards in this topic, this may take a while.</p>


       <button onClick = {this.props.handleDeletion}> Delete</button>

       <button onClick = {this.props.closeModal}> Cancel </button>  
      </div>, 
      this.el

    )
  }


}

export default DeletionWarningModal