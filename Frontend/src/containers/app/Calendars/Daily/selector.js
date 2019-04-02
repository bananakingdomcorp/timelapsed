import React from 'react'
import {connect} from 'react-redux'
import Chrono from 'chrono-node'


class Selector extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      start: '',
      end: '',
      meantStart: '',
      meantEnd: ''
    }

  }

  handleStartChange = (e) => {
    this.setState = {start: e.target.value}

  this.setState({meantStart: Chrono.parse(e.target.value)})


  }

  handleEndChange = (e) => {
    this.setState = {end: e.target.value}

    this.setState({meantEnd: Chrono.parse(e.target.value)})



  }


  render() {
    return (
      <div>

        Enter a start time. Just type in the time that you want, and we will figure out the rest.

        <input value = {this.state.start} onChange = {(e) => this.handleStartChange(e.target.value)}  />
        Did you mean: {this.state.meantStart} ???

        Enter and end time

        <input value = {this.state.end} onChange = {(e) => {this.handleEndChange(e.target.value)}} />
        Did you mean: {this.state.meantEnd} ????


        <button onClick = {this.handleSave}>Save</button>


      </div>
    )
  }
}

export default connect(null, null) (Selector)