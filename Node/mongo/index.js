const mongoose = require('mongoose')
// mongoose.connect('mongodb://localhost/timelapsed');
const Schema = mongoose.Schema;
// Just boilerplate stuff now, fill out later. 


const userSchema = new mongoose.Schema({
  UserName: String,
  Comment: String,
  Likes: {type : Number, default : 0},
  Card_ID: Number,

});



module.exports =  mongoose.model('User', userSchema);
