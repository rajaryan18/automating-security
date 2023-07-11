var app = require("express")();
var http = require('http').Server(app);
var bodyParser = require('body-parser');
require('dotenv').config();


app.use(bodyParser.json())

app.post('/alarm', function(req, res) {
  const msg = req.body.msg;
  // returns an array of possible alarms. Use key 'values'
  res.status(201).json({
    'values' : msg['values']
  });

  // upload on blockchain with event id = 1
});

http.listen(process.env.PORT, function(){
  console.log(`Connected to port ${process.env.PORT}`);
});