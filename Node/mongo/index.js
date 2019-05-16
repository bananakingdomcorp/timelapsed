import mongoose from 'mongoose';

//this is just a placeholder for now. 


const userSchema = new mongoose.Schema({
  username: {
    type: String,
    unique: true,
  },
});

const User = mongoose.model('User', userSchema);

export default User;