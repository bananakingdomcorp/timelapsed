import React from 'react';

import {connect} from 'react-redux';

import ReactDOM from 'react-dom'

import RecurringCalender from './../../Calendars/Recurring/index';

import MonthlyCalender from './../../Calendars/Monthly/index';

import {clearTimes} from './../../../../modules/card'

import {addCard} from './../../../../modules/board'

import {Api} from './../../../../djangoApi';



const ModalRoot = document.querySelector('#modal-root')

class AddCardModal extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: '',
      description: '',
      optionOpen : false,
      selectedOption: 'Untimed',
      tooltipRecurring: false,
      tooltipTimed: false,
      tooltipUntimed: false


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

  getCalendarState = (childState) => {

    return childState;
  }

  addCard = () =>  {
    console.log('cardAddTesting')

    //first write to our backend.

    if(Object.keys(this.props.times).length === 0) {
      //if no times. 
      Api().post('/card/', {
        Data: {Name: this.state.title, Description: this.state.description, Topic: this.props.board[this.props.id]['Data']['id']},
      })
      .then((res) => {
        if(res.status === 201) {
          //Add to our redux. 
          console.log(res.data)
          let card = {
            id: res.data.Data.id,
            Name: this.state.title,
            Description: this.state.description,
            times : [],
          }

          this.props.addCard(this.props.id, card)
        }
      })
      


    } else {
      //If we have times. 
      let times = [];

      for (let key in this.props.times) {
        let test = {}
        let split = key.split(' ')
        let day = new Date(key)
        test['Day'] = day.toLocaleDateString('en-US',{weekday: 'long'})
        test['Begin_Date'] = `${split[3]}-${day.getMonth() +1}-${split[2]}`

        this.props.times[key].forEach((item) => {
          let time = item[0].split(',')
          test['Begin_Time'] = time[0]
          test['End_Time'] = time[1].trim()
          test['Num_Weeks'] = item[1]
          test['Weeks_Skipped'] = item[2]
        })
        times.push(test)
      }

      Api().post('/card/', {
        Data: {Name: this.state.title, Description: this.state.description, Topic: this.props.board[this.props.id]['Data']['id']},
        Times: times
      })
      .then((res) => {
        if(res.status ===201) {
          let temp = this.props.times
          temp.map((item, index) => {
            return {
              'Begin_Time': times[index]['Begin_Time'],
              'End_Time': times[index]['End_Time'],
              'Num_Weeks': times[index]['Num_Weeks'],
              'Weeks_Skipped': times[index]['Weeks_Skipped'],
              'id' : res.data.Data.ids[index],
            }
          })

          let card = {
            id: res.data.Data.id,
            Name: this.state.title,
            Description: this.state.description,
            Times: temp,
          }

          this.props.addCard(this.props.id, card)
          .then(() => {
            this.props.clearTimes()
          })
        }
      })
      .then(() => {
        this.props.closeModal()
      })
      

    }


    //Then clear our times in Redux.

    //Then add the card to the topic.

    //Then close the modal.


  }

  titleChange = (e) => {
    this.setState({title: e})

  }

  descriptionChange = (e) => {
    this.setState({description: e})


  }

  optionChange = (e) => {
    if(e.target.value !== this.state.selectedOption) {
      //Every time the option changes, clear the times. This may need to be changed at a later date. 
      this.props.clearTimes()
    }
    this.setState({selectedOption: e.target.value})

  }

  timedMouseOver = () => {
    this.setState({tooltipTimed: true})

  }

  timedMouseOut = () => {
    this.setState({tooltipTimed: false})

  }

  recurringMouseOver = () => {
    this.setState({tooltipRecurring: true})


  }

  recurringMouseOut = () => {
    this.setState({tooltipRecurring: false})


  }

  untimedMouseOver = () => {
    this.setState({tooltipUntimed: true})

  }

  untimedMouseOut = () => {
    this.setState({tooltipUntimed: false})

  }
 
  openOption = () => {
    this.setState({optionOpen: true})
  }

  
  listenerLoader = () => {
    document.addEventListener("mousedown", this.handleClickOutside)

  }

  listenerUnLoader = () => {
    document.removeEventListener("mousedown", this.handleClickOutside)
    
  }

  render() {

    let options = null;

    let timedDiv = null;

    let recurringDiv = null;

    let untimedDiv = null;

    if(this.state.tooltipTimed) {
      timedDiv = <div className ='addCardModalInstructions' >
        A timed task is one where you have an idea how long a task will take to accomplish, and you want to measure that time with regards 
        to your schedule. For example, if you estimate that it will take four hours for you to read a book, this option will estimate a completion date 
        based on your schedule. 

      </div>
    }

    if(this.state.tooltipRecurring) {
      recurringDiv = <div className ='addCardModalInstructions' >
        A recurring task is one that you would like to repeat at certain intervals. For example, let's say that you want to read for an hour a day
        after work. Other tasks that you calculate after work will take this into account. 
      </div>
    }

    if(this.state.tooltipUntimed) {
      untimedDiv = <div className = 'addCardModalInstructions'>
      This task will not be timed. This can be changed at a later date 
      </div>

    }
 
    let optionsOpen = null;

    // Style this. 

    let timedButton =   <button className = 'addCardModalTimedUnclicked' value = 'Timed' onClick = {this.optionChange} onMouseOver = {this.timedMouseOver} onMouseOut = {this.timedMouseOut} > Timed</button> 

    let recurringButton =  <button className = 'addCardModalRecurringUnclicked' value = 'Recurring' onClick = {this.optionChange} onMouseOver = {this.recurringMouseOver} onMouseOut = {this.recurringMouseOut}> Recurring</button>

    let untimedButton = <button className = 'addCardModalRecurringUnclicked' value = 'Untimed' onClick = {this.optionChange} onMouseOver = {this.untimedMouseOver} onMouseOut = {this.untimedMouseOut} />

    if(this.state.selectedOption === 'Timed') {
      timedButton =  <button className = 'addCardModalTimedClicked' value = 'Timed' onClick = {this.optionChange} onMouseOver = {this.timedMouseOver} onMouseOut = {this.timedMouseOut} > Timed Clicked</button> 
    }

    if(this.state.selectedOption === 'Recurring') {
      recurringButton = <button className = 'addCardModalRecurringClicked' value = 'Recurring' onClick = {this.optionChange} onMouseOver = {this.recurringMouseOver} onMouseOut = {this.recurringMouseOut}> Recurring clicked</button>
    }


    if(this.state.optionOpen === true) {
      optionsOpen = 
      <div className = 'addCardModalOptionsOpen'>
        is it....
        {timedButton}
        {recurringButton}
        {untimedButton}
      </div>

    }



    if(this.state.title!== '' && this.state.description !== '') {
      options =         
      <div>
        <div className = 'addCardModalSelectPrompt' onClick = {this.openOption} >Click here to tell me more about this task...   </div>
        <br></br>
        {optionsOpen}
        {timedDiv}
        {recurringDiv}
        {untimedDiv}

      </div>
    }

    let firstCalendar = null ;

    let secondCalendar = null;

    if(this.state.selectedOption == 'Recurring') {
      firstCalendar = <RecurringCalender getCalendarState = {this.getCalendarState} listenerLoader = {this.listenerLoader} listenerUnLoader = {this.listenerUnLoader}/>
    }

    if(this.state.selectedOption === 'Timed') {
      secondCalendar = <MonthlyCalender getCalendarState = {this.getCalendarState} listenerLoader = {this.listenerLoader} listenerUnLoader = {this.listenerUnLoader} />
    }


    return ReactDOM.createPortal(

      <div className = 'genericModal' ref = {this.cardModalRef}>
      
        <input onChange = {(e) => this.titleChange(e.target.value)} placeholder = 'Title' className = 'addCardModalTitle'  />


        <input onChange = {(e) => this.descriptionChange(e.target.value)} placeholder = "Description" className = 'addCardModalDescription' />

        {options}
        {firstCalendar}
        {secondCalendar}


        <div className = 'addCardModalButtons'>
          <button type= 'submit' className = "saveButton" onClick = {this.addCard}> Save </button>
          <button className = "cancelButton" onClick = {this.props.closeModal} > Cancel </button>
        </div>

      </div>, 
      this.el
    )
  }
}


function mapStateToProps(state) {
  return {
    times: state.card.times,
    board: state.board.board,


  }
}

const mapDispatchToProps = {
  clearTimes,
  addCard

}



export default connect(mapStateToProps, mapDispatchToProps) (AddCardModal);