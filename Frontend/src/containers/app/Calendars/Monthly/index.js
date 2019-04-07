//This component primarially holds everything in our calendar. 


//Since this may take a while to load, try react.lazy to load this with the modal.

import React from 'react';

import {connect} from 'react-redux';

import {getDaysInMonth} from 'date-fns/get_days_in_month';

import {getDate} from 'date-fns/get_date'

class MonthlyCalender extends React.Component {
  constructor(props) {
    super(props)
  }

  componentWillMount() {
    let numDays = getDaysInMonth(new Date());

  }



  render () {

    let days= [];



    return (
      <div className = 'monthlyCalendar'>

      {days}

        
      </div>
    )
  }

}

export default connect(null, null) (MonthlyCalender);