const express = require("express");

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const recordRoutes = express.Router();

// This section  get a list of all the documents on papers page
// gets first 50 results from papers collection
recordRoutes.route("/papers").get(async function (req, res) {
    const dbConnect = dbo.getDb();
  
    dbConnect
      .collection("papers")
      .find({}).limit(50)
      .toArray(function (err, result) {
        if (err) {
          res.status(400).send("Error fetching papers!");
       } else {
          res.json(result);
        }
      });
  });

  // This section will help you create a new document.
recordRoutes.route("/papers/recordSwipe").post(function (req, res) {
    const dbConnect = dbo.getDb();
    const matchDocument = {
      listing_id: req.body.id,
      last_modified: new Date(),
      session_id: req.body.session_id,
      direction: req.body.direction
    };
  
    dbConnect
      .collection("papers")
      .insertOne(matchDocument, function (err, result) {
        if (err) {
          res.status(400).send("Error inserting matches!");
        } else {
          console.log(`Added a new match with id ${result.insertedId}`);
          res.status(204).send();
        }
      });
  });

  module.exports = recordRoutes;