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
      switchPosition : -Infinity,
      

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

  switchPositions = (e) => {
    this.setState({switchPosition: e}, () => this.closeSelections())

  }


  render() {
    let selections =  <option onClick = {this.openSelections} > Select Topic  </option>
    if(this.state.selectionOpen) {
      selections = [] 
      this.props.board[this.props.topic].data.cards.forEach((item, index) => {
        if(this.props.data.id !== item.id)
        selections.push(<ul onClick = {() => this.switchPositions(index) } > {item.Name}</ul> )
      })

    }

    if(this.state.selectionOpen === false && this.state.switchPosition !== -Infinity) {
      selections = <option onClick = {this.openSelections} > {this.props.board[this.props.topic].data.cards[this.state.switchPosition].Name}  </option>
    }

    let times = null;



    return ReactDOM.createPortal(
      <div>
        <input onChange = {(e) => this.titleChange(e.target.value)} value = {this.state.title} className = 'addCardModalTitle'  />

        <input onChange = {(e) => this.descriptionChange(e.target.value)} value = {this.state.description} className = 'addCardModalDescription' />        

        Times for this card:
        {times}

        <div>Edit times </div>

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