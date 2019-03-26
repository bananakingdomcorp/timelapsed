//USE THIS AS YOUR AXIOS REQUEST. 



import store from './store'
import axios from 'axios'
import {clientId, clientSecret} from './djangoSecrets';
import setAuthToken from './modules/token'



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
    return response
  }, function (error) {
    if(error.response.status === 401) {
      //If we need to log in again, reset the state so that it does that, then return an error to the user. 
      store.dispatch(setAuthToken(''))

    }
    return Promise.reject(error);
  });

  return temp
}
