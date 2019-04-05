import { combineReducers } from 'redux'
import board from './board'
import token from './token'
import card from './card'

export default combineReducers({
  board,
  token,
  card
})
