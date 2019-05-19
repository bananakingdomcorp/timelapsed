import { combineReducers } from 'redux'
import board from './board'
import token from './token'
import card from './card'
import relationships from './relationships'
import subclass from './subclass'


export default combineReducers({
  board,
  token,
  card,
  relationships,
  subclass,
})
