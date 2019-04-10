import React from 'react';

import {connect} from 'react-redux';

import Day from './day'

import DailyCalendar from './../Daily/index'


class RecurringCalender extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      dailyCalendarOpen: false,
      currentDay : '',

    }
  }

  selectDay =  (day) => {
    console.log(day)
    //Open daily calendar
    this.setState({dailyCalendarOpen: true, currentDay : day});


  }

  closeModal = (times) => {

    this.setState({dailyCalendarOpen: false})

 
  }



  render() {

    let theWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    let dailyCalender = null;

    if (this.state.dailyCalendarOpen === true) {

      dailyCalender = <DailyCalendar closeModal = {this.closeModal} day = {this.state.currentDay} listenerLoader = {this.props.listenerLoader} listenerUnLoader = {this.props.listenerUnLoader} />

    }

    //Shows all of our currently selected days. 
    let dates = Object.keys(this.props.times).map((item) => this.props.times[item].map((time) => <div> {item}, {time.split(',')[0]}--{time.split(',')[1]} </div> ) )




    return (
      <div>
        <div className = 'recurringCalendar'>

          {theWeek.map((date) => {
            return (
              <Day name = {date} selectDay = {this.selectDay} /> 
              // <div>{date}</div>
            )
          })}
          {dailyCalender}

        </div>
        <div className = 'recurringCalendarSelectedDates'>
        Curent Times:
          {dates}

        </div>
      </div>      
    )
  }

}

function mapStateToProps(state) {
  return {
    times: state.card.times

  }
}

const mapDispatchToProps = {
}


export default connect(mapStateToProps, mapDispatchToProps) (RecurringCalender);