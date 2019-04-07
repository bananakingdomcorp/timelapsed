import React from 'react';
import {connect} from 'react-redux'
import AddTopic from './addTopic/addATopic'
import Topic from './topic/topic'
import {setAuthToken} from '../../modules/token';
import Axios from 'axios';
import {clientId, clientSecret} from '../../djangoSecrets';
import {Api} from  './../../djangoApi'
import {setBoard} from '../../modules/board';
import LoginPage from './loginPage';

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
            this.props.setBoard(res.data)
    
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
      <LoginPage onSuccess = {this.responseGoogle} onFailure = {this.responseGoogle} />
    }

    return (
      <div>
        {googs}

        { this.props.board.map((item, index) => {
          return (<div className = 'topic'> <Topic id = {index} key = {index} /> </div>)
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
  setAuthToken,
  setBoard

}


export default connect(mapStateToProps, mapDispatchToProps) (BackGroundPage);