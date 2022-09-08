[![](https://data.jsdelivr.com/v1/package/npm/echarts/badge)](https://www.jsdelivr.com/package/npm/echarts)

# HealthSciHelper
 
This project aims to inform on the paper options at the university of otago
to allow better informed desicion making with respect to study.

This application is composed of three Vagrant virtual machines provisioned with 
virtualbox. the vm-webapp VM hosts a paper information webapp written using React.
This virtual machine interacts with a database server in order to retrieve and 
consequently, diplay, said paper information. 

The database virtal machine hosts a node.js server that is connected to a 
mongoDB database. An express.js API is connected to this server to define access.

The final virtual machine hosts a webscraper implimented in python 
to get data from the university of otago webpage, process it and update
the database with this information monthly.

 ### Build instuctions 
 To access the remote server, use the remote explorer config.
 Create new ones in the C drive (.ssh) folder 
 Use vagrant ssh-config to get details of new vms

 Opens in /home/vagrant which is different to /vagrant

Then in new Window open from wherever suits

### Usage
run 'vagrant up' in the terminal to create the application

# Interacting with the database
vagrant ssh dbserver
run 
$ systemctl status mongod

to ensure mongodb is running

then use mongosh to enter and check mongodb. 
To see papers in collection use commands:
test> use admin
admin> db.auth('vagrant', 'vagrant')
admin> show collections
admin> db.papers.find()

to display all collections names and contents of the papers collection

you can use 'db.enableFreeMonitoring()' at this point to monitor the 
database via a GUI


# Architecture

HealthSciHelper is based off a LAMP stack web architecture with a few differences.
First, the front end and back end are hosted on Linux virtual machines that are provisined using vagrant with virtualbox.
A public facing webserver front end controls and hosts (via apache) the display and user interaction. 
This webserver follows a typical client-server relation.

This webserver then accesses via a private network, a backend, database server.
This noSQL, mongodb database contains univeristy paper information, updated every time step by the 'scraper' virtual machine.

The scraper virtual machine controls the running of the webscapers to automatically scrape data from the selected
universities site in an automated fashion using cron timers. This virtual machine then updates the database backend 
with the newly scraped paper information. 

## Diagram of architecture 
![alt text](https://github.com/hadwi537/HealthSciHelper/blob/main/docs-assets/Diagram.PNG?raw=true)

# Data Structure

Simple data structure - just one table of papers 

```mermaid
    erDiagram
    Store {
        string paper_code
        string year
        string title
        string points
        list: string teaching_period
        string subject
        list: string prerequistes
        dict more_info
    }
```
# Useful debugging 

recommend using vsode with the remote ssh extension. 
Simply change to the directory with the Vagrantfile
and get the ssh-config using 
~/vagrant/machine$ vagrant ssh-config
Then copy and paste the ouput into an ssh config file.
(default at ~/.ssh/config)

# Current Website configuration 

(localhost)
http://127.0.0.1:3001

### Next Steps:

* Generate Private Keys and redifine/improve security

* Call pipenv creation in base directory (possibility)

* Initalise the Pipfiles in the root or not?
* Seems cleaner to do it on remote but is slowww
* Could add more memory/cpu to the machine?

* Note Log in as vagrant user

* Some papers require some number of 'generic' points, i.e non-specific points

* for visualisation, for a certain paper, get all its children etc
* then show as radial tree (can do with mongodb request)

* todo: plan is to create dsplot.graph in scraper instead
i.e it will generate the data, insert it, then create the graph then pass graph to db where it can 
be quiered by webserver

* ensure that the windows defender etc is turned off and there are no vms in the vm folder as these will cause collisions

* to connect to the database using mongosh from command line use mongosh "mongodb://vagrant:vagrant@192.168.2.14:3000/admin"

* using express api (most common)

* now use npm

* bootstrapped using Create React App


## web ap commands

from the root directoruy of the web-app vm

npm start 
runs on some host

for build and deploy run:
$ npm run build
$ npm run deploy

# home page once published:
"https://hadwi537.github.io/HealthSciHelper/"

## local development

* for database use npm start


using cross-env package to avoid port collisions