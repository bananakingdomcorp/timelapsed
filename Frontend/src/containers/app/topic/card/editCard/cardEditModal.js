import React from 'react';
import {connect} from 'react-redux';
import ReactDOM from 'react-dom'

const ModalRoot = document.querySelector('#modal-root')

class CardEditModal extends React.Component {
  constructor(props) {
    super(props)

    
    this.el = document.createElement('div');
    this.cardModalRef = React.createRef();
  }


  componentWillMount() {
    ModalRoot.appendChild(this.el);
    document.addEventListener("mousedown", this.handleClickOutside)

  }

  componentWillUnmount() {
    ModalRoot.removeChild(this.el)
    document.removeEventListener("mousedown", this.handleClickOutside)
  }

  handleClickOutside = (e) =>  {
    if (!this.cardModalRef.current.contains(e.target)) {
      this.props.closeModal();

    }
  }


  render() {
    return ReactDOM.createPortal(
      <div>

      </div>, 
      this.el

    )
  }

}



export default connect(null, null) (CardEditModal);