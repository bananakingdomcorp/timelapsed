export const ADD_TOPIC = 'board/ADD_TOPIC'
export const SET_BOARD = 'board/SET_BOARD'
export const DELETE_TOPIC = 'board/DELETE_TOPIC'
export const CHANGE_TOPIC_NAME = 'board/CHANGE_TOPIC_NAME'
export const CHANGE_TOPIC_POSITIONS = 'board/CHANGE_TOPIC_POSITIONS'
export const ADD_CARD = 'board/ADD_CARD'
export const CHANGE_CARD_INFO = 'board/CHANGE_CARD_INFO'
export const CHANGE_CARD_POSITION = 'board/CHANGE_CARD_POSITION'
export const CARD_TOPIC_MOVE = 'board/CARD_TOPIC_MOVE'



const initialState = {
  board: [],
}

export default (state = initialState, action) => {
  switch (action.type) {
    case ADD_CARD: 
      return {
        ...state,
        board: state.board.map((item, index) =>  {
          if(index === action.index) {
            return {
              ...state.board.index,
              Data : {
                ...state.board[action.index].Data,
                Cards: [...state.board[action.index].Data.Cards, action.card]
              }                
            }
          } else {
            return item;
          }
        })
      }

    case ADD_TOPIC:
      return {
        board: [
          ...state.board,
          action.name
        ]
      }
    case SET_BOARD:
      return{
        board: action.board
      }
    case DELETE_TOPIC:
      return {
        ...state,
        board: state.board.filter(item => item.Data.id !== action.id)
      }
    case CHANGE_TOPIC_NAME:
      let fixedName = state.board.map((item, index) => {
        if (index ===action.id) {
          return {...state.board.item, Data: {...item.Data, Name: action.name}}
        } else {
          return item;
        }
      })
      return {
        ...state,
        board: fixedName
      }
    
    case CHANGE_CARD_INFO:
      return {
        ...state,
        board: state.board.map((item, index) => {
          if(index === action.topic) {
            return {
              ...state.board[action.topic],
              Data: {
                ...state.board[action.topic].Data,
                Cards: state.board[action.topic].Data.Cards.map((card) => {
                  if (card.id === action.info.id ) {
                    return {
                      ...state.board[action.topic].Data.Cards.card,
                      Name: action.info.Name,
                      Description: action.info.Description,
                      Times: action.info.Times                  
                    }
                  } else {
                    return card;
                  }
                })
              }
            }
          } else {
            return item;
          }
        })
      }

    case CARD_TOPIC_MOVE:
      let last = state.board[action.oldTopic].Data.Cards[action.info.Position]
      console.log(last)
      return {
        ...state,
        board : state.board.map((item, index) => {
          if(index === action.oldTopic) {
            //Delete from here
            return {
              ...state.board[action.oldTopic],
              Data:{
                ...state.board[action.oldTopic].Data,
                Cards: state.board[action.oldTopic].Data.Cards.filter(item => item.id !== last.id)
              }
            }
          } else if (index === action.newTopic) {
            return {
              ...state.board[action.newTopic],
              Data: {
                ...state.board[action.newTopic].Data,
                Cards: [...state.board[action.newTopic].Data.Cards, last ]
              }
            }
          } else {
            return item;
          } 

        })

      }

    case CHANGE_TOPIC_POSITIONS:
      let saveOne = state.board[action.topic1];
      let saveTwo = state.board[action.topic2];

      let fixedPosition = state.board.map((item, index) => {
        if (index === action.topic2) {
          return saveOne;
        }
        if (index === action.topic1) {
          return saveTwo;
        }
        return item;
      })
      return {
        ...state,
        board: fixedPosition
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
  return {
    type: DELETE_TOPIC,
    id
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
  return {
    type: CHANGE_TOPIC_POSITIONS,
    topic1,
    topic2
  }

}

export const changeTopicAndPosition = (name, id, topic1, topic2) => {
  return dispatch => {
    dispatch(changeTopicName(name, id))
    dispatch(changeTopicPositions(topic1,topic2))
}

}

export const addCard = (index, card) => {
  return {
    type: ADD_CARD,
    index,
    card
  }
}


export const changeCardInfo = (topic, info) => {
  return {
    type: CHANGE_CARD_INFO,
    topic,
    info
  }
}

export const cardTopicMove = (oldTopic, newTopic, info) => {
  return {
    type: CARD_TOPIC_MOVE,
    oldTopic,
    newTopic,
    info
  }
}

export const changeCardTopic = (oldTopic, newTopic, info) => {
  return dispatch => {
    dispatch(cardTopicMove(oldTopic, newTopic, info))
    dispatch(changeCardInfo(newTopic, info))
  }
}



export const changeCardPosition =(topic, info, newPosition) => {



}
