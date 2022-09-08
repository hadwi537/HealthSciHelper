const express = require("express");
const app = express();
const port = 5000;
const MongoClient = require("mongodb").MongoClient;
const mongo = require("mongodb");
const bodyParser = require("body-parser");

let db;



const MONGO_URI = "mongodb://vagrant:vagrant@192.168.2.14:3000/admin"

MongoClient.connect(MONGO_URI, function(err, client) {
  error = err;
  if (err) return console.log(err);
  db = client.db("admin");

  db.collection("papers")
    .find()
    .toArray(function(err, result) {
      if (err) throw err;
      if (result.length === 0) {
        console.log("Database is empty");

        db.collection("papers").insertMany(
          [
          {'paper_code': "MATH306", 'year': "2022", 'title': "Geometry of Curves and Surfaces", 'points': "18", 'teaching_period': "S2", 
                  'subject': "Mathematics", 'prereq_string': "36 points at 200 level", 'prereq_list': ['MATH203', 'MATH202'], 'dl_dict': 'none'},
          {'paper_code': "COSC343", 'year': "2022", 'title': "AI", 'points': "18", 'teaching_period': "S2", 
                  'subject': "Computer Science", 'prereq_string': "36 points at 200 level", 'prereq_list': ['COSC343', 'MATH202'], 'dl_dict': 'none'},
          {'paper_code': "MATH202", 'year': "2022", 'title': "Multivariable calculus", 'points': "18", 'teaching_period': "S1", 
                  'subject': "Mathematics", 'prereq_string': "MATH170", 'prereq_list': ['MATH170'], 'dl_dict': 'none'},
      
            ],
          (err, result) => {
            if (err) return console.log(err);
            console.log("Added initial data");
          }
        );
      } else {
        console.log("Database has contents - will not reinitalise");
      }
    });
});

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  res.header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE");
  next();
});


app.get("/", (req, res) => res.send("Hello World!\n"));


app.get("/papers", (req, res) => {
  db.collection("papers")
    .find()
    .toArray(function(err, result) {
      if (err) throw err;
      res.send(result);
      console.log(result);
    });
});

app.post("/paper", (req, res) => {
  db.collection("paper").insertOne(req.body.note, (err, result) => {
    if (err) return console.log(err);

    console.log("saved to database");
    res.send({ reply: "Paper was saved.", contents: req.body.note });
  });
});

app.listen(port, () => console.log(`App listening on port ${port}`));