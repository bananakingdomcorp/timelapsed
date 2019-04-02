import React from 'react';

import {connect} from 'react-redux';

import Day from './day'

import Chrono from 'chrono-node';

import DailyCalendar from './../Daily/index'


class RecurringCalender extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      selected : [],
      dailyCalendarOpen: false,
      currentDay : ''

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

  render() {

    let theWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    let dailyCalender = null;

    if (this.state.dailyCalendarOpen === true) {

      dailyCalender = <DailyCalendar closeModal = {this.closeModal} day = {this.state.currentDay} listenerLoader = {this.props.listenerLoader} listenerUnLoader = {this.props.listenerUnLoader} />

    }




    return (
      <div className = 'recurringCalendar'>

      {theWeek.map((date) => {
        return (
          <Day name = {date} selectDay = {this.selectDay} selected = {this.state.selected} /> 
          // <div>{date}</div>
        )
      })}
      {dailyCalender}
      </div>
    )
  }

}

export default connect(null, null) (RecurringCalender);