import mongoose from 'mongoose';

//this is just a placeholder for now. 




const userSchema = new mongoose.Schema({
  UserName: String,
  Comment: String,
  Likes: {type : Number, default : 0},
  Card_ID: Number,

});

const User = mongoose.model('User', userSchema);

export default User;