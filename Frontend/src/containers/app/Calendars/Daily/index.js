import React from 'react'
import {connect} from 'react-redux'
import Selector from './selector'


class DailyCalendar extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      times: []
    }

  }

  //Show existing times for this date. 

  addTime = (time) => {

    this.setState({times: [...this.state.times, time  ]})

  }



  render() {



    return (
      <div>
        Existing Times for {this.props.day}:

        {this.state.times.map((time) => {
          return <div> Time Start: ${time.start} ---- Time End: ${time.end} </div>
        })}

        Add a time:

        <Selector addTime = {this.addTime} />
        
      </div>
    )
  }
}

export default connect(null, null) (DailyCalendar)