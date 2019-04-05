export const ADD_TIMES = 'card/ADD_TIMES'
export const CLEAR_TIMES = 'card/CLEAR_TIMES'


const initialState = {
  times : null

}

export default (state = initialState, action) => {
  switch(action.type) {
    case ADD_TIMES:
      return {
        times: action.times
      }


  default:
    return state
  }
}


export const addTimes = (times) => {
  return {
    type: ADD_TIMES,
    times
  }
}

export const clearTimes = () => {
  return {
    type: CLEAR_TIMES,
  }
}