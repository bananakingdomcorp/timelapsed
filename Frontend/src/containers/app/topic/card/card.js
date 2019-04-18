import React from 'react'
import {connect} from 'react-redux'

class Card extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div className = 'card'>
        <p className = 'title' > {this.props.data.Name} </p>

        {this.props.data.Description}

      </div>
    )
  }



}


export default connect(null, null) (Card)