import React from 'react';
import {connect} from 'react-redux';
import ReactDOM from 'react-dom'
import {Api} from './../../../../../djangoApi'

import {changeCardInfo, changeCardTopic} from './../../../../../modules/board'

const ModalRoot = document.querySelector('#modal-root')

class CardEditModal extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      title: this.props.data.Name,
      description: this.props.data.Description,
      selectionOpen: false,
      switchPosition : -Infinity,
      times : [],
      topic: this.props.topic,
      topicSelectionOpen: false,

    }

    
    this.el = document.createElement('div');
    this.editCardModalRef = React.createRef();
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
    if (!this.editCardModalRef.current.contains(e.target)) {
      this.props.closeModal();

    }
  }

  openPositionSelection = () => {
    this.setState({selectionOpen: true})

  } 
  
  closePositionSelection = () => {
    this.setState({selectionOpen: false})

  }

  titleChange = (e) => {
    this.setState({title:e })
  }

  descriptionChange = (e) => {
    this.setState({description: e})
  }

  switchPositions = (e) => {
    this.setState({switchPosition: e}, () => this.closePositionSelection())

  }

  openTopicSelection = () => {
    this.setState({topicSelectionOpen: true})
  }

  closeTopicSelection = () => {
    this.setState({topicSelectionOpen: false})

  }

  switchTopic = (e) => {

    this.setState({topic: e}, () => this.closeTopicSelection())
  }

  deleteCard = () => {
    //Deletes our card.
    Api().delete(`/card/${this.props.board[this.props.topic].Data.id}/`)

  }

  saveEdit = () => {

    //Send everything to the backend. 
    let pos = this.state.switchPosition === -Infinity? this.props.position : this.state.switchPosition;


    Api().put(`/card/${this.props.board[this.props.topic].Data.id}/`, {Data: {Description: this.state.description, Name: this.state.title, Position: pos, Topic: this.state.topic} } )
    .then((res) => {
      if (res.status === 200) {
        //Call redux. 

        //if we are changing the topic that the card is in.
        if(this.state.topic !== this.props.topic) {
          this.props.changeCardTopic(this.props.topic, Number(this.state.topic),  {Description: this.state.description, Name: this.state.title, Position: this.props.position, Times : this.state.times, id: this.props.data.id } )
        } else {
       //If we are just changing the information about the card...



       this.props.changeCardInfo(this.props.topic, {Description: this.state.description, Name: this.state.title, Position: this.props.position, Times : this.state.times })
        }






        //if we are changing the position of the card. 
      }
    })

    //This doesn't fix cards/times. That still needs to be added. 

  }


  render() {
    let selections =  <option onClick = {this.openPositionSelection} > Switch Positions with another card  </option>
    if(this.state.selectionOpen) {
      selections = [] 

      this.props.board[this.props.topic].Data.Cards.forEach((item, index) => {
        if(this.props.data.id !== item.id)
        selections.push(<ul onClick = {() => this.switchPositions(index) } > {item.Name}</ul> )
      })

    }

    if(this.state.selectionOpen === false && this.state.switchPosition !== -Infinity) {
      selections = <option onClick = {this.openPositionSelection} > {this.props.board[this.props.topic].Data.Cards[this.state.switchPosition].Name}  </option>
    }

    let topicSelector =  <option onClick = {this.openTopicSelection} > Change Topic  </option>

    if(this.state.topicSelectionOpen) {
      topicSelector = [];
      Object.keys(this.props.board).forEach((item) => {
        if(Number(item) !== this.props.topic) {
          topicSelector.push(<ul onClick = {() => this.switchTopic(item)}> {this.props.board[item].Data.Name} </ul>)
        }
      })
    }

    if(this.state.topicSelectionOpen === false && this.state.topic !== this.props.data.Name) {
      topicSelector = <option onClick = {this.openTopicSelection}> {this.props.board[this.state.topic].Data.Name} </option>
    }

    let times = null;



    return ReactDOM.createPortal(
      <div ref = {this.editCardModalRef} className= "genericModal">
        <input onChange = {(e) => this.titleChange(e.target.value)} value = {this.state.title} className = 'addCardModalTitle'  />

        <input onChange = {(e) => this.descriptionChange(e.target.value)} value = {this.state.description} className = 'addCardModalDescription' />        

        Times for this card:
        {times}

        <div>Edit times </div>

        Change position with:
        <div className = 'cardEditSelectionDropdown'>
          {selections}
        </div>

        <div>
          {topicSelector}
        </div>

        <div onClick = {this.deleteCard}> DELETE THIS CARD </div>

        <button onClick = {this.saveEdit} >Save </button>
        <button>Cancel </button>
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
  changeCardInfo,
  changeCardTopic,

}


export default connect(mapStateToProps, mapDispatchToProps) (CardEditModal);