var app = require("express")();
var http = require('http').Server(app);
var bodyParser = require('body-parser');
require('dotenv').config();

 app.use(bodyParser.json())
 app.post('/',function(req,res){
    var msg=req.body.msg;
    console.log("python: " + msg);
    res.status(201).json({ 'msg': 'received' });
 });

  http.listen(3500, function(){
    console.log('listening...');
  });