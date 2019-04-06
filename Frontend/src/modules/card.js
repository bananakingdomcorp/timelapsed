export const ADD_TIMES = 'card/ADD_TIMES'
export const CLEAR_TIMES = 'card/CLEAR_TIMES'


const initialState = {
  times : {}

}

export default (state = initialState, action) => {
  switch(action.type) {
    case ADD_TIMES:
      return {
        times: {
          ...state.times,
          [action.day] : action.times

        }
      }
    case CLEAR_TIMES:
      return {
        times: {}
      }


  default:
    return state
  }
}


export const addTimes = (day, times) => {
  return {
    type: ADD_TIMES,
    day,
    times
  }
}

export const clearTimes = () => {
  return {
    type: CLEAR_TIMES,
  }
}
