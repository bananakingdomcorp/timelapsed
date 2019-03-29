import React from 'react';

const ModalRoot = document.querySelector('#modal-root-two')


class DeletionWarningModal extends React.Component{
  constructor(props) {
    super(props)


    this.el = document.createElement('div');
    this.deleteWarningModalRef = React.createRef();
  }

  //Not sure right now if the mousedown will work correctly or not. 


  render() {
    return (
      <div>

      </div>

    )
  }


}

export default DeletionWarningModal