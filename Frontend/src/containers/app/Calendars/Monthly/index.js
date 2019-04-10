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
      spaceDays: 0,
      currentDate: 0,


    }
  }

  componentWillMount() {
    let d = new Date();
    let r = new Date(d.getFullYear(), d.getMonth() +1, 0).getDate()
    let s = d.getDay()
    let t = d.getDate()

    this.setState({ numDays : r, spaceDays: s, currentDate: t})

  }

  selectDay(day) {
    //Once a day has been selected, open the daily calendar. 
    
    this.setState({dailyCalendarOpen: true})
    
    //Get the full date of this day, add to state. 

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
        days.push(<Day date = {i} />)
      }
    }



    return (
      <div className = 'monthlyCalendar'>

      {days}

        
      </div>
    )
  }

}

export default connect(null, null) (MonthlyCalender);