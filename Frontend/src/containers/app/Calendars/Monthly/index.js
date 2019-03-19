//This component primarially holds everything in our calendar. 


//Our Calendar will use Chrono for date language processing. 

//Since this may take a while to load, try react.lazy to load this with the modal.

import React from 'react';

import {connect} from 'react-redux';

class MonthlyCalender extends React.Component {
  constructor(props) {
    super(props)
  }



  render () {

    return (
      <div className = 'monthlyCalendar'>
        
      </div>
    )
  }

}

export default connect(null, null) (MonthlyCalender);