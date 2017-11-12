//this is the starting file

const express = require('express'); //essentially import
const app = express(); //we can attach routes to this app

//this is a route. get is a route handler
app.get('/', (req, res) => {
  res.send({ hi: 'there' }); //this is what the app will send back as a response
});

//Dynamic port binding here
const PORT = process.env.PORT || 5000; //This is the port that heroku will give us
app.listen(PORT); //listens on port 5000
