<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html>
    <head>
        <title>Interact with database in a more useful manner</title>
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

        <h2>Enter custom SQL to query database</h2>
                <form action="" method="post">
            Enter SQL Query:
            <input type=text name="t1">
            <br>
            <br>
            <input type=submit name="s">
            <?php
            if(isset($_POST['s']))
            {
                $a=$_POST['t1']; //accessing value from the text field
                echo "SQL query is: ".$a; //displaying result
            }
            ?>
        </form>

        <h1>Database test page</h1>

        <p>Showing contents of SQL query:</p>

        <table border="1">
            <tr><th>Paper code</th><th>Paper name</th></tr>

            <?php
                $db_host   = '192.168.2.14';
                $db_name   = 'fvision';
                $db_user   = 'webuser';
                $db_passwd = 'insecure_db_pw';

                $pdo_dsn = "mysql:host=$db_host;dbname=$db_name";

                $pdo = new PDO($pdo_dsn, $db_user, $db_passwd);

                
                $a=$_POST['t1']; //accessing value from the text field
          

                $q = $pdo->query($a);

                while($row = $q->fetch()){
                echo "<tr><td>".$row["code"]."</td><td>".$row["name"]."</td></tr>\n";
                }
            ?>
        </table>
    </body>
</html>