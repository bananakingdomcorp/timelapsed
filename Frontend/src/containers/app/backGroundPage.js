import React from 'react';
import {connect} from 'react-redux'
import AddTopic from './addTopic/addATopic'
import Topic from './topic/topic'
import { GoogleLogin } from 'react-google-login';
import {setAuthToken} from '../../modules/token';
import Axios from 'axios';
import {clientId, clientSecret} from '../../djangoSecrets';
import {Api, token} from  './../../djangoApi'

class BackGroundPage extends React.Component {
  constructor(props) {
    super(props);
  }
 
  responseGoogle = (response) => {
      if (response.accessToken !== undefined) {
      //Outside of this request, use our djangoapi
      Axios.post('http://localhost:8000/auth/convert-token', {
        grant_type: 'convert_token', 
        client_id: clientId,
        client_secret: clientSecret,
        backend: 'google-oauth2',
        token: response.accessToken
      })
      .then((res) => {
        //Set our Auth Token in Redux
        this.props.setAuthToken(res.data.access_token)

      })
      .then(() => {
          
        //Query our backend for our information.
        let data = new FormData();
        data.append('Email', response.profileObj.email)

        //For this response, 201 means that you created a new record, will return a 400 if already exists. 

        Api().post('/user/', data,)
        .then((res) => {

          if (res.status === 200) {
            //From here we need to make a redux call that both organizes as well as writes our information to the board. 
          }
        })
      
      })

    }

  }

  render() {

    //SET TO MODAL 

    let googs = null;

    if(this.props.token === '') {
      googs =
      <div className = 'googleModal'>
        <GoogleLogin
          clientId="346085700873-dsg2gea98rmschm8f1pm4kt8u0f9av3f.apps.googleusercontent.com"
          buttonText="Login"
          onSuccess={this.responseGoogle}
          onFailure={this.responseGoogle}
        />

     </div>
    }

    return (
      <div>
        {googs}

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
    board: state.board.board,
    token: state.token.authToken


  }
}

const mapDispatchToProps = {
  setAuthToken
}


export default connect(mapStateToProps, mapDispatchToProps) (BackGroundPage);