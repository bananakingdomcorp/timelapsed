import React from 'react';

import {connect} from 'react-redux';

import Day from './day'

import Chrono from 'chrono-node';

import DailyCalendar from './../Daily/index'


class RecurringCalender extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      dailyCalendarOpen: false,
      currentDay : '',
      dailyTimes : {
        Sunday: [],
        Monday: [],
        Tuesday: [],
        Wednesday: [],
        Thursday: [],
        Friday: [],
        Saturday: []

      }

    }
  }

  selectDay =  (day) => {
    console.log(day)
    //Open daily calendar
    this.setState({dailyCalendarOpen: true, currentDay : day});


  }

  closeModal = (times) => {
    this.setState({dailyTimes: {currentDay: times}})

    this.setState({dailyCalendarOpen: false})

 
  }

  addTimes = (times) => {
    this.setState({dailyTimes: {...this.state.dailyTimes,  currentDay: times }  })

  }

  render() {

    let theWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    let dailyCalender = null;

    if (this.state.dailyCalendarOpen === true) {

      dailyCalender = <DailyCalendar addTimes = {this.addTimes} closeModal = {this.closeModal} day = {this.state.currentDay} listenerLoader = {this.props.listenerLoader} listenerUnLoader = {this.props.listenerUnLoader} />

    }

    //Shows all of our currently selected days. 
    let dates = Object.keys(this.state.dailyTimes).map((item) => this.state.dailyTimes[item].length ===0? null: this.state.dailyTimes[item].map((time) => <div> {item}, {time.split(',')[0]}--{time.split(',')[1]} </div> ) )




    return (
      <div className = 'recurringCalendar'>

      {theWeek.map((date) => {
        return (
          <Day name = {date} selectDay = {this.selectDay} /> 
          // <div>{date}</div>
        )
      })}
      {dailyCalender}
      {dates}





      </div>
    )
  }

}

export default connect(null, null) (RecurringCalender);