import React from 'react';


import {connect} from  'react-redux';
import AddACard from './addACard';


class Topic extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      modal: false,

    }
  }
  openModal= () =>  {
    this.setState({modal : true})

  }

  closeModal = () =>  {
    this.setState({modal: false});
  }

  render() {
    return (
      <div >
        <div className = 'nameplate'>
          <p> {this.props.board[this.props.id][0]} </p>
        </div>
          <AddACard modal = {this.state.modal} openModal = {this.openModal} closeModal = {this.closeModal} />
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