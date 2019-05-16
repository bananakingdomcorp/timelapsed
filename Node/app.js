const express = require('express')
const app = express()
var router = express.Router()
const port = 3000
var http = require('http').Server(app);
var io = require('socket.io')(http);




router.get('/', (req, res) => res.send('Hello World!'))


http.listen(3000, function(){
  console.log(`listening on ${port}`);
});