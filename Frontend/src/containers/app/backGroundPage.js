import React from 'react';
import {connect} from 'react-redux'
import AddTopic from './addTopic/addATopic'
import Topic from './topic/topic'


class BackGroundPage extends React.Component {
  constructor(props) {
    super(props);
  }
 
  
  render() {


    return (
      <div>

        { Object.keys(this.props.board).map((item) => {
          return (<div className = 'topic'> <Topic name = {item} key = {item} number = {item} /> </div>)
        })

    }

        <div className = 'addTopic' >
          <AddTopic />
        </div>
        
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


export default connect(mapStateToProps, mapDispatchToProps) (BackGroundPage);