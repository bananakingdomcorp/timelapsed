//This component primarially holds everything in our calendar. 


//Since this may take a while to load, try react.lazy to load this with the modal.

import React from 'react';

import {connect} from 'react-redux';

import {getDaysInMonth} from 'date-fns/get_days_in_month';

import {getDate} from 'date-fns/get_date'

import Day from './day'

import DailyCalendar from './../Daily/index'

class MonthlyCalender extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      numdays: 0,
      dailyCalendarOpen: false,
      currentDay: ''

    }
  }

  componentWillMount() {
    this.setState({ numDays : getDaysInMonth(new Date())})

  }

  selectDay(day) {
    //Once a day has been selected, open the daily calendar. 
    
    this.setState({dailyCalendarOpen: true})
    
    //Get the full date of this day, add to state. 



  }



  render () {

    let days= [];

    for(let i = 1; i <= this.state.numDays; i++) {
      days.push(<Day date = {i} />)
    }



    return (
      <div className = 'monthlyCalendar'>

      {days}

        
      </div>
    )
  }

}

export default connect(null, null) (MonthlyCalender);