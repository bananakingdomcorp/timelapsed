// This file gives us a basic pattern for accepting responses to card changes. 

//This can be called every time that we get data back from the backend. It provides a singluar interface for interacting with the redux
//calls that are crucial for dealing with the api. 

import store from './../store'

export const handleResponse = (returnData) =>  {

  returnData.Subclass.forEach((item) => {


    //Perform redux call here. 
  })

  returnData.Edit.forEach((item) => {

    //Redux call here. 
  })

  returnData.Delete.forEach((item) => {

    
    //Redux call here. 
  })



}