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

      }

    }
  }

  selectDay =  (day) => {
    console.log(day)
    //Open daily calendar
    this.setState({dailyCalendarOpen: true, currentDay : day});


  }

  closeModal = () => {

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




    return (
      <div className = 'recurringCalendar'>

      {theWeek.map((date) => {
        return (
          <Day name = {date} selectDay = {this.selectDay} /> 
          // <div>{date}</div>
        )
      })}
      {dailyCalender}
      </div>
    )
  }

}

export default connect(null, null) (RecurringCalender);