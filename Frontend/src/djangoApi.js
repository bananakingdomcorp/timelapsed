//USE THIS AS YOUR AXIOS REQUEST. 



import store from './store'
import axios from 'axios'
import setAuthToken from './modules/token'



//This creates a function that you can call. 

export const Api =() => {

  let token = store.getState().token.authToken

  let params = {
    //Or whatever your server port is 
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
      //If we need to log in again, reset the state so that it does that. 
      store.dispatch(setAuthToken(''))

    }
    if(error.response.status === 500) {
      //If the server is down, set our server down page.

      console.log('Server down error')
    }
    return Promise.reject(error);
  });

  return temp
}
