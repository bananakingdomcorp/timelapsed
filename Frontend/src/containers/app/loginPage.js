import React from 'react';
import { GoogleLogin } from 'react-google-login';



class Login extends React.Component {


  render() {
    return (
      <div className = 'loginPage'> 


      <p>You need to login to Google to access this site. Please login below </p>

      <GoogleLogin
          clientId="346085700873-dsg2gea98rmschm8f1pm4kt8u0f9av3f.apps.googleusercontent.com"
          buttonText="Login"
          onSuccess={this.props.onSuccess}
          onFailure={this.props.onFailure}
        /> 



      </div>
    )
  }
}

export default Login