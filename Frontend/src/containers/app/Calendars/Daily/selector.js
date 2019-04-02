import React from 'react'
import {connect} from 'react-redux'


class Selector extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      start: '',
      end: '',
    }

  }

  handleStartChange = (e) => {
    this.setState({start: e.target.value} )

  }



  handleEndChange = (e) => {
    console.log(e)
    this.setState({end: e.target.value})




  }


  render() {
    return (
      <div>

        Enter a start time.

        <input type = 'time' > </input>

        Enter an end time

        <input type = 'time'> </input>

        <button onClick = {this.handleSave}>Save</button>


      </div>
    )
  }
}

export default connect(null, null) (Selector)