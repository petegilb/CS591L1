//
// # SimpleServer
//

// Import packages/libraries
var http = require('http');
var path = require('path');

var express = require('express');
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('database.sql');

// Create and configure server.
var router = express();
var server = http.createServer(router);

router.configure(function(){
  router.use(express.bodyParser());
  router.use(router.router);
});

// Location for static files (html files).
router.use(express.static(path.resolve(__dirname, 'client')));

server.listen(process.env.PORT || 3000, process.env.IP || "0.0.0.0", function(){
  var addr = server.address();
  console.log("Server listening at", addr.address + ":" + addr.port);
});

// First API: /getall
// Gets all the books ordered by author then title.
router.get('/get_all', function(request, response) {
  var query = "SELECT * FROM books ORDER BY books.author ASC, books.title ASC;";
  
  db.all(query, function(err, rows) {
    var result = [];
    rows.forEach(function(row) {
      result.push(
        { "title": row.title, "author": row.author }
      );
    });
    response.send(JSON.stringify(result));
  });
});

// Second API: /by_author
// Gets all the book that match *exactly* the provided author sorted by title.
router.post('/by_author', function(request, response) {
  var query = "SELECT * FROM books WHERE books.author = '" + request.body.author + "' ORDER BY books.title ASC;";
  
  db.all(query, function(err, rows) {
    var result = [];
    rows.forEach(function(row) {
      result.push(
        { "title": row.title, "author": row.author }
      );
    });
    response.send(JSON.stringify(result));
  });
});

// Third API: /save
// Saves the given book into the database.
router.post('/save', function(request, response) {
  var book = "('"+request.body.title+"', '"+request.body.author;
  var query = "INSERT INTO books(title, author) VALUES " + book + ";";
  
  db.run(query, function(err, status) {
    if(err != null) {
      response.status(500).send(err);
    
    } else {
      response.send("Success");
    }
  })
});
