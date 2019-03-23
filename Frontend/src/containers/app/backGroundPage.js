import React from 'react';
import {connect} from 'react-redux'
import AddTopic from './addTopic/addATopic'
import Topic from './topic/topic'
import { GoogleLogin } from 'react-google-login';
import {setAuthToken} from '../../modules/token';


class BackGroundPage extends React.Component {
  constructor(props) {
    super(props);
  }
 
  responseGoogle = (response) => {
    console.log(response);
  }

  render() {


    return (
      <div>
        <GoogleLogin
          clientId="346085700873-dsg2gea98rmschm8f1pm4kt8u0f9av3f.apps.googleusercontent.com"
          buttonText="Login"
          onSuccess={this.responseGoogle}
          onFailure={this.responseGoogle}
        />

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
  setAuthToken
}


export default connect(mapStateToProps, mapDispatchToProps) (BackGroundPage);