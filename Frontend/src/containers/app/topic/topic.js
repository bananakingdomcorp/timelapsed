import React from 'react';


import {connect} from  'react-redux';
import AddCardModal from './addCard/addCardModal';


class Topic extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      addCardModal: false,

    }
  }
  openAddCardModal= () =>  {
    this.setState({addCardModal : true})

  }

  closeAddCardModal = () =>  {
    this.setState({addCardModal: false});
  }

  render() {
    let modalView = null;
    if (this.state.addCardModal == true) {
      modalView = <AddCardModal closeModal = {this.closeAddCardModal} />
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