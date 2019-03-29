import React from 'react';


import {connect} from  'react-redux';
import AddCardModal from './addCard/addCardModal';
import EditPanelModal from './editPanel/editPanelModal';




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
          <p> {this.props.board[this.props.id][0]} </p>
        </div>
          <div className =  'topicAddCard' onClick= {this.openAddCardModal}>
            Add a task
          </div>
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