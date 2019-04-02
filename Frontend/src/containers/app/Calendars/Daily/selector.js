import React from 'react'
import connect from 'react-redux'


class Selector extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      start: '',
      end: ''
    }

  }

  render() {
    return (
      <div>

        Enter a start time. Just type in the time that you want, and we will figure out the rest.

        



        Enter an end time. 


      </div>
    )
  }
}

export default connect(null, null) (Selector)