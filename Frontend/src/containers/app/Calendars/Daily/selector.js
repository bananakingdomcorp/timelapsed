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

    if(this.state.start === '' || this.state.end === '' ) {
      this.setState({errorMessage: 'Please make sure that you have provided both a start and an end time.'})
      return
    }
    if ((this.convertTime(this.state.start) - this.convertTime(this.state.end)) > -1 ) {
      this.setState({errorMessage: 'Please make sure that your end time is after your start time'})
      return 
    }

    this.setState({errorMessage: 'Time Saved!!', start: '', end: ''}, () =>  setTimeout(() => this.setState({errorMessage: ''}), 3000))

    this.props.addTime([this.state.start, this.state.end])

  }

  render() {
    return (
      <div>

        Enter a start time.

        <input type = 'time' onChange={(e) => {this.setState({start:e.target.value})}} />

        Enter an end time

        <input type = 'time' onChange={(e) => {this.setState({end:e.target.value})}} />

        <div className = 'selectorErrorMessage'> {this.state.errorMessage} </div>

        <button onClick = {this.handleSave} >Save</button>


      </div>
    )
  }
}

export default connect(null, null) (Selector)