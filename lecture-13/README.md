Sample node.js webserver interfacing with an SQLite database.

## Running the server

Make sure you install all the needed dependencies:
```bash
npm install
```

Run the server from the terminal using:
```bash
node server
```

Once the server is running, open this url in your browser 'http://localhost:3000/' to run the client webpage.

Warning: this is tested on node versions up to node 8. It is known not to work on node 12 due to a problem with the node-sqlite3 dependency.

## Organization of the code
* server.js : this file contains the code for the server (the intermediate layer between the client and database).
* database.sql : this is the database used. to open it, use `sqlite3 database.sql` in the command line / terminal.
* client/index.html : this is the code for the webpage that will run in the user's browsers.
