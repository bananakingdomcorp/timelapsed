import React from 'react';

import {connect} from 'react-redux';

import Day from './day'

class RecurringCalender extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {

    let theWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']




    return (
      <div className = 'recurringCalendar'>

      {theWeek.map((date) => {
        return (
          <Day name = {date} /> 
        )
      })}
      </div>
    )
  }

}

export default connect(null, null) (RecurringCalender);