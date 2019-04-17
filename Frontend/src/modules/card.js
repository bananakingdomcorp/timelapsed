export const ADD_TIMES = 'card/ADD_TIMES'
export const CLEAR_TIMES = 'card/CLEAR_TIMES'
export const REMOVE_TIMES = 'card/REMOVE_TIMES'


const initialState = {
  times : {}

}

export default (state = initialState, action) => {
  switch(action.type) {
    case ADD_TIMES:
      let ourTimes
      if(state.times[action.day] === undefined ) {
        ourTimes = action.times;          
      } else {
        ourTimes = [...state.times[action.day], action.times]
      }
      return {
        times: {
          ...state.times,
          [action.day] : ourTimes

        }
      }
    case REMOVE_TIMES:
      return {
        times: {
          ...state.times,
          [action.day] : state.times[action.day].filter((item) => item !== action.time)
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

export const removeTimes = (day, time) => {
  return {
    type: REMOVE_TIMES,
    day,
    time
  }

}

export const clearTimes = () => {
  return {
    type: CLEAR_TIMES,
  }
}