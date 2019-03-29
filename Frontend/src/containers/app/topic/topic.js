import React from 'react';


import {connect} from  'react-redux';
import AddACard from './addACard';


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
    return (
      <div >
        <div className = 'nameplate'>
          <p> {this.props.board[this.props.id][0]} </p>
        </div>
          <AddACard modal = {this.state.addCardModal} openModal = {this.openAddCardModal} closeModal = {this.closeAddCardModal} />
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