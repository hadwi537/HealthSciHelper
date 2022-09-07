<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html>
    <head>
        <title>Interact with mongodb database</title>
        <style>
            th { text-align: left; }

            table, th, td {
            border: 2px solid grey;
            border-collapse: collapse;
            }

            th, td {
            padding: 0.2em;
            }
        </style>
    </head>

    <body>
    <?php 
        // Establish MongoDB Connection
        $uri = "mongodb://vagrant:vagrant@localhost:27017"
        $connection = new MongoDB\Client($uri);
        $databaseMongo = $connection->selectDatabase(Config::get('admin'));
        $images = $databaseMongo->selectCollection("images");

        $image = $images->find();
        
        ?>
    </body>
</html>