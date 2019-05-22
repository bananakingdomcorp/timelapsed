const express = require('express')
const app = express()
const port = 3000


app.use('/api', './api/comments.js')





http.listen(3000, function(){
  console.log(`listening on ${port}`);
});