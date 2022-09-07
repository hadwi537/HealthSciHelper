const MongoClient = require("mongodb").MongoClient;
const mongo = require("mongodb");

let db

MongoClient.connect("mongodb://vagrant:vagrant@192.168.2.14:3000/admin", function(err, client) {
  error = err;
  if (err) return console.log(err);
  db = client.db("db");

  db.collection("papers")
    .find()
    .toArray(function(err, result) {
      if (err) throw err;
      if (result.length === 0) {
        console.log("Database is currently empty");

      } else { 
        console.log("Database has papers!");
      }
    });
});