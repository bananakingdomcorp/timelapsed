import React from 'react'
import { Route, Link } from 'react-router-dom'
import BackGroundPage from './backGroundPage'
import { hot } from 'react-hot-loader'
import { GoogleLogin } from 'react-google-login';


class App extends React.Component {
  constructor(props) {
    super(props)
  }
  
  responseGoogle = (response) => {
    console.log(response);
  }

  render() {
    return (
      <div className = 'background'>
      <GoogleLogin
        clientId="346085700873-dsg2gea98rmschm8f1pm4kt8u0f9av3f.apps.googleusercontent.com"
        buttonText="Login"
        onSuccess={this.responseGoogle}
        onFailure={this.responseGoogle}
      />,  
        <BackGroundPage />
      </div>
    
    )
  }


}

export default hot(module)(App)