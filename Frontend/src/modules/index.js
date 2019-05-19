import { combineReducers } from 'redux'
import board from './board'
import token from './token'
import card from './card'
import cardRelationships from './cardRelationships'
import subclass from './subclass'
import topicRelationships from './topicRelationships'


export default combineReducers({
  board,
  token,
  card,
  cardRelationships,
  topicRelationships, 
  subclass,
})
