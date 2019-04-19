import React from 'react'
import {connect} from 'react-redux'
import CardEditModal from './editCard/cardEditModal';



class Card extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      editModalOpen: false,

    }
  }

  openModal = () => {
    this.setState({editModalOpen: true})
  }
  closeModal = () => {
    this.setState({editModalOpen: false})
  }


  render() {

    let modal = null;

    if(this.state.editModalOpen) {
      modal = <CardEditModal topic = {this.props.topic} closeModal = {this.closeModal} data = {this.props.data} />
    }

    return (
      <div className = 'card'>
        <div className = 'cardEdit' > ... </div>      
        <p className = 'cardTitle' > {this.props.data.Name} </p>
        View relationships. 
      </div>
    )
  }



}


export default connect(null, null) (Card)