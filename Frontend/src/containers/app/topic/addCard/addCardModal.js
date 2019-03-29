import React from 'react';

import {connect} from 'react-redux';

import ReactDOM from 'react-dom'

import RecurringCalender from './../../Calendars/Recurring/index';

import MonthlyCalender from './../../Calendars/Monthly/index';




const addCardModalRoot = document.querySelector('#modal-root')

class AddCardModal extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: '',
      description: '',
      optionOpen : false,
      selectedOption: '',


    }
    this.el = document.createElement('div');
    this.cardModalRef = React.createRef();
  }



  componentWillMount() {
    addCardModalRoot.appendChild(this.el);
    document.addEventListener("mousedown", this.handleClickOutside)

  }

  componentWillUnmount() {
    addCardModalRoot.removeChild(this.el)
    document.removeEventListener("mousedown", this.handleClickOutside)
  }

  handleClickOutside = (e) =>  {
    if (!this.cardModalRef.current.contains(e.target)) {
      this.props.closeModal();

    }
  }

  addCard = () =>  {
    console.log('cardAddTesting')

    //Here we are going to simply add to our redux store one card. Yay!

  }

  titleChange = (e) => {
    this.setState({title: e})

  }

  descriptionChange = (e) => {
    this.setState({description: e})


  }

  optionChange = (e) => {
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
 
  openOption = () => {
    this.setState({optionOpen: true})
  }

  render() {

    let options = null;

    let timedDiv = null;

    let recurringDiv = null;

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

    let optionsOpen = null;

    // Style this. 

    let timedButton =   <button className = 'addCardModalTimedUnclicked' value = 'Timed' onClick = {this.optionChange} onMouseOver = {this.timedMouseOver} onMouseOut = {this.timedMouseOut} > Timed</button> 

    let recurringButton =  <button className = 'addCardModalRecurringUnclicked' value = 'Recurring' onClick = {this.optionChange} onMouseOver = {this.recurringMouseOver} onMouseOut = {this.recurringMouseOut}> Recurring</button>

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
      </div>
    }

    let firstCalendar = null ;

    let secondCalendar = null;

    if(this.state.selectedOption == 'Recurring') {
      firstCalendar = <RecurringCalender/>
    }

    if(this.state.selectedOption === 'Timed') {
      firstCalendar = <RecurringCalender/>
      secondCalendar = <MonthlyCalender />
    }


    return ReactDOM.createPortal(

      <div className = 'addCardModal' ref = {this.cardModalRef}>
      
        <input onChange = {(e) => this.titleChange(e.target.value)} placeholder = 'Title' className = 'addCardModalTitle'  />


        <input onChange = {(e) => this.descriptionChange(e.target.value)} placeholder = "Description" className = 'addCardModalDescription' />

        {options}
        {firstCalendar}
        {secondCalendar}



        <button type= 'submit' className = "saveButton" onClick = {this.addCard}> Save </button>
        <button className = "cancelButton" onClick = {this.props.closeModal} > Cancel </button>
      </div>, 
      this.el
    )
  }
}

export default connect(null, null) (AddCardModal);