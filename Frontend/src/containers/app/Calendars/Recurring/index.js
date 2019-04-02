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

    }
    this.dailyCalender = null;
  }

  selectDay =  (day) => {
    console.log(day)
    //Open daily calendar
    this.setState({dailyCalendarOpen: true});

    // this.dailyCalender = <DailyCalendar day = {day} />


  }

  render() {

    let theWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


    return (
      <div className = 'recurringCalendar'>

      {theWeek.map((date) => {
        return (
          <Day name = {date} selectDay = {this.selectDay} selected = {this.state.selected} /> 
          // <div>{date}</div>
        )
      })}
      {this.dailyCalender}
      </div>
    )
  }

}

export default connect(null, null) (RecurringCalender);