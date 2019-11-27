var express = require('express');
var app = express();
var http = require('http').Server(app);
const jiff = require('./jiff/lib/jiff-server');

jiff.make_jiff(http, { logs:true });

http.listen(3000, function () {
  console.log('listening on *:3000');
});
