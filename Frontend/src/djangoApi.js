//USE THIS AS YOUR AXIOS REQUEST. 


//HERE'S WHY. WE DON'T WANT TO HAVE TO WRITE OUT OUR AUTH TOKENS AND URL INTO EVERY SINGLE REQUEST. 

//IN LIEU OF THAT, WE WILL CREATE AN AXIOS FUNCTION HERE THAT WE WILL USE AS OUR REQUEST HEADER THROUGHOUT THE APPLICATION. 

import store from './store'
import axios from 'axios'

export const djangoApi = () => {
  
  const token = store.getState().authToken;

  const params = {

    baseURL: 'http://localhost:8000/',
    
    headers: {'Authorization': 'Token ' + token}
    
    };

    return axios.create(params)

}