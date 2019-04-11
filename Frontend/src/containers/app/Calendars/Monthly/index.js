//This component primarially holds everything in our calendar. 


//Since this may take a while to load, try react.lazy to load this with the modal.

import React from 'react';

import {connect} from 'react-redux';

import Day from './day'

import DayInvalid from './dayInvalid'

import DailyCalendar from './../Daily/index'

class MonthlyCalender extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      numdays: 0,
      dailyCalendarOpen: false,
      selectedDay: '',
      startDate: '',
      spaceDays: 0,
      currentDate: 0,
      currentMonth: 0,
      currentYear: 0,

    }
    this.months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  }

  componentWillMount() {
    let d = new Date();
    let r = new Date(d.getFullYear(), d.getMonth() +1, 0).getDate()

    this.setState({startDate: d, numDays : r, spaceDays: d.getDay(), currentDate: d.getDate(), currentMonth: d.getMonth(), currentYear: d.getFullYear()})

  }

  selectDay(day) {
    //Once a day has been selected, open the daily calendar. 
    
    this.setState({dailyCalendarOpen: true})
    
    //Get the full date of this day, add to state. 

    let selected = new Date()

  }

  increaseMonth() {

    if (this.state.currentMonth === 11) {
      //Advance the year. 
      this.increaseYear()
      this.setState({currentMonth: 0})

    } else {
      this.setState({currentMonth: this.state.currentMonth + 1});
    }

  }

  decreaseMonth() {
    if(this.state.currentMonth <= this.state.startDate.getMonth() && this.state.currentYear <= this.state.startDate.getFullYear() ) {
      return 
      //We can not go to previous months. 

    }

    if (this.state.currentMonth === 0) {
      this.decreaseYear()
      this.setState({currentMonth: 11})
    } else {
      this.setState({currentMonth: this.state.currentMonth -1})
    }

  }

  increaseYear() {

    this.setState({currentYear: this.state.currentYear +1})

  }

  decreaseYear() {

    this.setState({currentYear: this.state.currentYear -1})

  }

  renderCalendar() {
    let arr = []

    for (let i = 0; i < this.state.spaceDays; i++) {
      arr.push(<DayInvalid date = {''} /> )
    }


  }


  render () {

    let days= [];

    //First, we are going to fill in our space days, which do nothing...

    for (let i = 0; i < this.state.spaceDays; i++) {
      days.push(<DayInvalid date = {''} /> )
    }



    for(let i = 1; i <= this.state.numDays; i++) {
      if(i < this.state.currentDate) {
        days.push(<DayInvalid date = {i} />)
      } else {
        days.push(<Day date = {i} selectDay = {this.selectDay} />)
      }
    }



    return (
      <div className = 'monthlyCalendar'>
      <div className = 'monthlyCalendarHeader'> 
        <button onclick = {this.decreaseMonth}> <i className = 'arrowLeft'></i> </button>  
        {this.months[this.state.currentMonth]}, {this.state.currentYear}  
        <button onclick = {this.increaseMonth}> <i className = 'arrowRight'></i> </button>          
      </div>



      {days}
        
      </div>
    )
  }

}

export default connect(null, null) (MonthlyCalender);