import React from 'react'
import {connect} from 'react-redux'


class Selector extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      start: '',
      end: '',
      errorMessage: ''
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

    //if the time already exists.
    if (this.props.addTime(this.state.start + ' , ' + this.state.end) === 'Already Exists!') {
      this.setState({errorMessage: 'Time already exists!'})
      return
    }

    //If the time overlaps with previous times. 

    



    this.setState({errorMessage: 'Time Saved!!', start: '', end: ''}, () =>  setTimeout(() => this.setState({errorMessage: ''}), 3000))


  }

  render() {
    return (
      <div>

        Enter a start time.

        <input type = 'time' onChange={(e) => {this.setState({start:e.target.value})}} value= {this.state.start} />

        Enter an end time

        <input type = 'time' onChange={(e) => {this.setState({end:e.target.value})}} value = {this.state.end} />

        <div className = 'selectorErrorMessage'> {this.state.errorMessage} </div>

        <button onClick = {this.handleSave} >Save Time</button>


      </div>
    )
  }
}

export default connect(null, null) (Selector)