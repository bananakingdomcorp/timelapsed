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

  handleSave = () => {

    if(this.state.start === '' || this.state.end === '' ) {
      this.setState({errorMessage: 'Please make sure that you have provided both a start and an end time.'})
    }
    console.log(this.state.end - this.state.start)


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