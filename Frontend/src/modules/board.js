export const ADD_TOPIC = 'board/ADD_TOPIC'
export const SET_BOARD = 'board/SET_BOARD'
export const DELETE_TOPIC = 'board/DELETE_TOPIC'




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
          ...action.name
          
        }
      }
    case SET_BOARD:
      return{
        ...state,
        board: action.board
      }
    case DELETE_TOPIC:
      return {
        board: action.rest
      }
      


    default:
      return state
  }
}

export const setBoard = (board) => {
  return {
    type: SET_BOARD,
    board
  }
}

export const addTopic = (name) => {
  return {
      type: ADD_TOPIC,
      name
  }
}

export const deleteTopic = (id) => {
  const {[id] : value, ...rest} = this.state.board.board
  return {
    type: DELETE_TOPIC,
    rest
  }
}