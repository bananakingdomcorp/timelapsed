export const ADD_TOPIC = 'board/ADD_TOPIC'

const initialState = {
  board: {},
  count: 0
}

export default (state = initialState, action) => {
  switch (action.type) {
    case ADD_TOPIC:
      return {
        board: {
          ...state.board,
          [action.name] : []
          
        }
        
      }

    default:
      return state
  }
}

export const addTopic = (name) => {
  return {
      type: ADD_TOPIC,
      name
  }
}