import React from 'react';
import {connect} from 'react-redux';
import ReactDOM from 'react-dom'

const ModalRoot = document.querySelector('#modal-root')

class CardEditModal extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      title: this.props.data.Name,
      description: this.props.data.Description,
      selectionOpen: false,
    }

    
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

  openSelections = () => {
    this.setState({selectionOpen: true})

  } 
  
  closeSelections = () => {
    this.setState({selectionOpen: false})

  }

  titleChange = (e) => {
    this.setState({title:e })
  }

  descriptionChange = (e) => {
    this.setState({description: e})
  }


  render() {
    let selections =  <div onClick = {this.openSelections} > Change position </div>
    if(this.state.selectionOpen) {
      

    }
    return ReactDOM.createPortal(
      <div>
        <input onChange = {(e) => this.titleChange(e.target.value)} value = {this.state.title} className = 'addCardModalTitle'  />

        <input onChange = {(e) => this.descriptionChange(e.target.value)} value = {this.state.description} className = 'addCardModalDescription' />        
        {selections}

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

const mapDispatchToProps = {
}


export default connect(mapStateToProps, null) (CardEditModal);