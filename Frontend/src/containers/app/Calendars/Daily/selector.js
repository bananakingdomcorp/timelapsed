import React from 'react'
import {connect} from 'react-redux'


class Selector extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      start: '',
      end: '',
      errorMessage: '',
      numWeeks: 0,
      weeksSkipped: 0,
    }

  }

  convertTime = (time) => {
    let split = time.split(':');
    return split[0] * 60 + split[1]
  }

  handleSave = () => {


    //If your selection is incomplete.
    if(this.state.start === '' || this.state.end === '' ) {
      this.setState({errorMessage: 'Please make sure that you have provided both a start and an end time.'})
      return
    }

    //If your end time is not after your start time.
    if ((this.convertTime(this.state.start) - this.convertTime(this.state.end)) > -1 ) {
      this.setState({errorMessage: 'Please make sure that your end time is after your start time'})
      return 
    }

    //If the time overlaps with previous times. 
    if (this.props.addTime(this.state.start + ' , ' + this.state.end, this.state.numWeeks, this.state.weeksSkipped) === 'Overlap') {
      this.setState({errorMessage: 'The times that you entered overlaps with an existing time. The times have been merged.'})
      return
    }

    this.setState({errorMessage: 'Time Saved!!', start: '', end: ''}, () =>  setTimeout(() => this.setState({errorMessage: ''}), 3000))


  }

  render() {
    return (
      <div>

        Enter a start time.

        <input type = 'time' onChange={(e) => {this.setState({start:e.target.value})}} value= {this.state.start} />

        Enter an end time

        <input type = 'time' onChange={(e) => {this.setState({end:e.target.value})}} value = {this.state.end} />

        Enter how many weeks you would like this task to repeat for, leave at zero for this to only happen once.

        <input type = 'number' min = '0' max = '52' onChange = {(e) => {this.setState({numWeeks: e.target.value})}} value = {this.state.numWeeks} /> 

        Enter how many weeks you would like this task to skip between events? Zero will be every week, one will be every other week, two every third week, ect ect ect..

        <input type = 'number' min = '0' max = '52' onChange = {(e) => {this.setState({weeksSkipped: e.target.value})}} value = {this.state.weeksSkipped} />


        <div className = 'selectorErrorMessage'> {this.state.errorMessage} </div>

        Note: If you overlap a time with a time from a previously day, the previous time will be removed and the new time will start on this day. 

        <button onClick = {this.handleSave} >Save Time</button>


      </div>
    )
  }
}

export default connect(null, null) (Selector)