//USE THIS AS YOUR AXIOS REQUEST. 



import store from './store'
import axios from 'axios'
import {clientId, clientSecret} from '../../djangoSecrets';




//This creates a function that you can call. 

export const Api =() => {

  let token = store.getState().token.authToken

  let params = {
    baseURL: 'http://localhost:8000/api',
    
    headers: {
      Authorization: 'Bearer ' + token
    }
  }

  let temp = axios.create(params)

  temp.interceptors.response.use(function (response) {
    // Do something with response data
    console.log(response)
    return response
  }, function (error) {
    // Do something with response error
    let lastRequest = error.config;
    console.log(lastRequest)


    if(error.response.status === 401) {
      
      return  axios.post('http://localhost:8000/auth/convert-token', {
        grant_type: 'convert_token', 
        client_id: clientId,
        client_secret: clientSecret,
        backend: 'google-oauth2',
        // token: refresh token here
      })
      .then((res) => {
        //Retry out original request




      })

    }


    return Promise.reject(error);
  }
  );

  return temp
}
