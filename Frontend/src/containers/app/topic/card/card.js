import React from 'react'
import {connect} from 'react-redux'



class Card extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      editModalOpen: false,

    }
  }


  render() {
    return (
      <div className = 'card'>
        <div className = 'cardEdit' > ... </div>      
        <p className = 'cardTitle' > {this.props.data.Name} </p>
        
      </div>
    )
  }



}


export default connect(null, null) (Card)