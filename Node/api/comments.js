const express = require('express');
const router = express.Router();


router.route('/card/:cardId')
  .get((req, res) => {
    //Get takes in a card ID and will return comments for that card.
  })
  .post((req, res) => {
    //Takes card ID and will create a comment for the card. 

  })

router.route('/comment/:commentId')
  .put((req, res) => {
    //Edits an existing comment.
  })
  .delete((req, res) => {
    //Deletes an existing comment. 
  })

router.route('/likes/:commentId')
  .post((req, res) => {
    //Likes a comment. 
  })






module.exports = router;