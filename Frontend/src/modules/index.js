import { combineReducers } from 'redux'
import board from './board'
import token from './token'

export default combineReducers({
  board,
  token
})
