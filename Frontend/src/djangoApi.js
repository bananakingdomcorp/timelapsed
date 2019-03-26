//USE THIS AS YOUR AXIOS REQUEST. 



import store from './store'
import axios from 'axios'




//This creates a function that you can call. 

export const Api =() => {

  let token = store.getState().token.authToken

  let params = {
    baseURL: 'http://localhost:8000/api',
    
    headers: {
      Authorization: 'Bearer ' + token
    }
  }

  let res = axios.create(params)

  res.interceptors.response.use(function (response) {
    // Do something with response data
    console.log(response)
    return response
  }, function (error) {
    // Do something with response error
    console.log('error', error)
    return Promise.reject(error);
  }
  );

  return res
}
