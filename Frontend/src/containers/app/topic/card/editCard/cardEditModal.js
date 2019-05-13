import React from 'react';
import {connect} from 'react-redux';
import ReactDOM from 'react-dom'
import {Api} from './../../../../../djangoApi'
import MonthlyCalendar from './../../../Calendars/Monthly/index'

import {changeCardInfo, changeCardTopic, changeCardPosition, deleteCard} from './../../../../../modules/board'
import {setBoard} from './../../../../../modules/card'
import {editParser, parser} from './../../../../../tools/serializerTools'

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
      editTimesModalOpen: false,

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
    Api().delete(`/card/${this.props.data.id}/`)
    .then((res) => {
      if (res.status === 204) {
        //call redux.
        this.props.deleteCard(this.props.topic, {Description: this.state.description, Name: this.state.title, Position: this.props.position, Times : this.state.times, id: this.props.data.id })

      }
    })
    .then(() => {
      this.props.closeModal();
    })

  }

  saveEdit = () => {
    let query = {Data: {Description: this.state.description, Name: this.state.title, Position: this.state.switchPosition === -Infinity? -1: this.props.board[this.props.topic].Data.Cards[this.state.switchPosition].id , Topic: this.props.board[this.state.topic].Data.id} }
    
    let times = {'Edit': {}, 'Delete': [], 'Add': [] }

    if (Object.keys(this.props.times).length !== 0) {
      //If we have edited our times. 

      let temp = Object.entries(this.props.data.Times)
  
  
  
      Object.keys(this.props.times).forEach((item) => {this.props.times[item].forEach((time) => {
        //If our time has an id. 
        console.log('TIME', time)
        if (time[3] !== undefined) {
          times['Edit'][time[3]] = parser(time.slice(0, 3));
        } else {
          //It is an addition.
          //Create our item here. Use our TimelapsedTools.
          times['Add'].push(editParser(item, time))
        }
      })})
  
      //Then check for deletions:
      temp.forEach((item) => {
        let data = item[1];
        if(times['Edit'][data.id] === undefined ) {
          //then it has been deleted
          times['Delete'].push(data.id)
        }
      })
  
      //times is now correct
  
      query['Times'] = times

    }


    //Send everything to the backend. 
    let pos = this.state.switchPosition === -Infinity? this.props.position : this.state.switchPosition;

    Api().put(`/card/${this.props.data.id}/`, query)
    .then((res) => {
      if (res.status === 200) {
        //Now we have to add in id's for any added items.
        console.log(res.data, 'DATA')

        //Call redux. 
        let temp =  {Description: this.state.description, Name: this.state.title, Position: this.props.position, Times : Object.values(this.props.times), id: this.props.data.id } 
        //if we are changing the topic that the card is in.
        if(this.state.topic !== this.props.topic) {
          this.props.changeCardTopic(this.props.topic, Number(this.state.topic), temp )
        } else if ( this.state.switchPosition !== -Infinity ) {
          this.props.changeCardPosition(this.props.topic, temp, pos )
          //We have changed the position of the card. 
        }else {
       //If we are just changing the information about the card...
          this.props.changeCardInfo(this.props.topic, temp)
        }
      }
    })
    .then(() => {
      this.props.closeModal();
    })

  }

  listenerLoader = () => {
    document.addEventListener("mousedown", this.handleClickOutside)

  }

  listenerUnLoader = () => {
    document.removeEventListener("mousedown", this.handleClickOutside)
    
  }

  openModal = () => {
    this.setState({editTimesModalOpen: true})
  }

  closeModal = () => {

    this.setState({editTimesModalOpen: false})
  }

  editTimes = () => {
    this.props.setBoard(this.props.editable)
    this.openModal();
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

    let editTimesModal =  <div onClick = {this.editTimes}>Edit times </div>;

    if(this.state.editTimesModalOpen) {
      editTimesModal = <div> <div onClick = {this.closeModal}>Close Calendar </div> <MonthlyCalendar listenerLoader = {this.listenerLoader} listenerUnLoader = {this.listenerUnLoader} /> </div>
      topicSelector = null;
      selections = null;
    }

    return ReactDOM.createPortal(
      <div ref = {this.editCardModalRef} className= "genericModal">
        <input onChange = {(e) => this.titleChange(e.target.value)} value = {this.state.title} className = 'addCardModalTitle'  />

        <input onChange = {(e) => this.descriptionChange(e.target.value)} value = {this.state.description} className = 'addCardModalDescription' />        


        <span className = 'cardEditSelectionDropdown'>
          {selections}
        </span>

        <span>
          {topicSelector}
        </span>

         Times for this card:
         {this.props.iteratableTimes.map((item) => {
           return item;
         })}
        {editTimesModal}
        <button onClick = {this.deleteCard}> DELETE </button>
        <button onClick = {this.saveEdit} >Save </button>
        <button onClick = {() => this.props.closeModal() }>Cancel </button>
      </div>, 
      this.el

    )
  }

}
function mapStateToProps(state) {
  return {
    board: state.board.board,
    times: state.card.times


  }
}

const mapDispatchToProps = {
  changeCardInfo,
  changeCardTopic,
  changeCardPosition,
  deleteCard,
  setBoard,

}


export default connect(mapStateToProps, mapDispatchToProps) (CardEditModal);