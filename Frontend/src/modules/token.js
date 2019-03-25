export const SET_AUTH_TOKEN = 'token/SET_AUTH_TOKEN'


const initialState = {
  authToken: '',
}

export default (state = initialState, action) => {
  switch (action.type) {
    case SET_AUTH_TOKEN:
      return {
        ...state,
        authToken : action.token
        
      }

    default:
      return state
  }
}

export const setAuthToken = (token) => {
  return {
      type: SET_AUTH_TOKEN,
      token
  }
}