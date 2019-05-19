import { combineReducers } from 'redux'
import board from './board'
import token from './token'
import card from './card'
import relationships from './relationships'


export default combineReducers({
  board,
  token,
  card
})
