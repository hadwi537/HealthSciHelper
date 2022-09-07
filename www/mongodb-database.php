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
        $command = escapeshellcmd('/home/vagrant/visualise/plot_graph.py');
        $output = shell_exec($command);
        echo $output;
        ?>
    </body>
</html>