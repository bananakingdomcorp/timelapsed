import React from 'react';


import {connect} from  'react-redux';
import AddCardModal from './addCard/addCardModal';
import EditPanelModal from './editPanel/editPanelModal';
import Card from './card/card'




class Topic extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      addCardModal: false,
      editCardModal: false,

    }
  }

  openEditCardModal = () => {
    this.setState({editCardModal: true})
  }

  closeEditCardModal = () => {
    this.setState({editCardModal: false})

  }

  openAddCardModal= () =>  {
    this.setState({addCardModal : true})

  }

  closeAddCardModal = () =>  {
    this.setState({addCardModal: false});
  }

  render() {
    let modalView = null;
    if (this.state.addCardModal === true) {
      modalView = <AddCardModal closeModal = {this.closeAddCardModal} id= {this.props.id} />
    }

    let editView = null;
    if(this.state.editCardModal === true) {
      editView = <EditPanelModal closeModal = {this.closeEditCardModal} id = {this.props.id} />
    }

    return (
      <div >
        <div className = 'nameplate'>
          <p> {this.props.board[this.props.id].Data.Name} </p>
        </div>
        <div className = 'topicEdit' onClick = {this.openEditCardModal}>
          Edit
        </div>

        <div className =  'topicAddCard' onClick= {this.openAddCardModal}>
          Add a card
        </div>
        {this.props.board[this.props.id].Data.Cards.map((info, index) => {
          return <Card topic = {this.props.id} data = {info} position ={index} key = {index} />
        }) }

        {modalView}
        {editView}
      </div>
    )
  }
}

function mapStateToProps(state) {
  return {
    board: state.board.board


  }
}

const mapDispatchToProps = {
}


export default connect(mapStateToProps, mapDispatchToProps) (Topic)