export const ADD_TOPIC = 'board/ADD_TOPIC'
export const SET_BOARD = 'board/SET_BOARD'
export const DELETE_TOPIC = 'board/DELETE_TOPIC'
export const CHANGE_TOPIC_NAME = 'board/CHANGE_TOPIC_NAME'
export const CHANGE_TOPIC_POSITIONS = 'board/CHANGE_TOPIC_POSITIONS'



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
        board: action.newBoard
      }
    case CHANGE_TOPIC_NAME:
      return {
        board: {
          ...state.board,
          ...action.id[0] = action.name
        }
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

//Maybe this should be for every board reset?

export const deleteTopic = (newBoard) => {
  return {
    type: DELETE_TOPIC,
    newBoard
  }
}

export const changeTopicName = (name, id) => {
  return{
    type: CHANGE_TOPIC_NAME,
    name,
    id
  }
}

export const changeTopicPositions = (topic1, topic2) => {
  
}

