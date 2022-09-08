# HealthSciHelper
 
This project aims to inform on the paper options at the university of otago
to allow better informed desicion making with respect to study.

This application is composed of three Vagrant virtual machines provisioned with 
virtualbox and follows a MERN stack archicture. the vm-webapp VM hosts a paper information webapp written using React.
This virtual machine interacts with a database server in order to retrieve and 
consequently, diplay, said paper information. 

The database virtal machine hosts a node.js server that is connected to a 
mongoDB database. An express.js API is connected to this server to define access.

The final virtual machine hosts a webscraper implimented in python 
to get data from the university of otago webpage, process it and update
the database with this information monthly.

## Getting started

### Prerequites 

* Download and install Vagrant from https://www.vagrantup.com/downloads
* Download and install VirtualBox from https://www.virtualbox.org/wiki/Downloads

please follow the instructions provided on the respective pages to progress

 ### Setup & Build

After the prerequites have been installed, open your IDE of choice (I used Visual Studio Code https://code.visualstudio.com/download) and create the folder you wish to associate with this project.
Then, clone the project from the url: https://github.com/hadwi537/HealthSciHelper. If your using visual studio code I recommend using the git plugin otherwise, you can use GitHub desktop or the command line 'git clone url' 

Once cloned, running `vagrant up` in the terminal will run the project

The webapp can then be viewed on local http://localhost:3001

### file sizes and timing details

* size of downloads dependinces during provisioning

* box file 

* zipped

* clean v new

* vagrant up execture time from clean

* vagrant up execute from existing 

## Development

* Ensure that the firewalls are turned off on host to ensure the application runs. For example,
windows defender and that there are no vms in the vm folder other than the ones currently running/building as these may cause port collisions.

### The webserver

The webserver can be run locally by `cd vm-webapp` and then `npm start`. This will open an instance that can be viewed at 
http://127.0.0.1:3001
Note that a useful feature of this design means that everytime a change is made to the webapp, the results are instantly updated in the browser making development relatviely sraightforward.

### The Database

The database can also be started locally by `cd vm-db` followed by `npm start server.js`. The database can be accessed from the command line use mongosh "mongodb://vagrant:vagrant@192.168.2.14:3000/admin"

in this mode you can use you can type 'db.enableFreeMonitoring()' which will allow you to monitor the database via a GUI webpage if you so desire.

A helpful command is `systemctl status mongod` which will indicate wether or not the database is running.

### The scraper

The scraper is fully written in python. Use pipenv run python <script.py> in order to run and develop scripts whose dependices will be resolved and added automatically by pipenv.

### Diagram of architecture 
![alt text](https://github.com/hadwi537/HealthSciHelper/blob/main/docs-assets/architecture.PNG?raw=true)

### Data Structure

Simple data structure - just one table of papers 

![alt text](https://github.com/hadwi537/HealthSciHelper/blob/main/docs-assets/paper_erd.PNG?raw=true)

However, the fact that the paper objects form a network of nodes is why a NoSQL database (mongodb) was used.

### Deployment

At any time, the webserver can be deployed to "https://hadwi537.github.io/HealthSciHelper/". To do this, change directory to vm-webapp and run:

`npm run build` followed by
`npm run deploy`

### Next Steps:

* Generate Private Keys and redifine/improve security

* add echarts to the webapp, i.e a radial tree of paper dependentcies
(see visualisation code for inspiration)

* replace direct access of scraper with express api

* Some papers require some number of 'generic' points, i.e non-specific points, how can this be effectively captured?

* add CI/CD pipelines

## Utilised Technologies

(MERN Stack)
* MongoDB: the database
* Node: Backend Javascript runtime 
* Express: Server and routing API for the web app
* React: Front end Javascript library 
* Bootstrap: Frontend framework for webapp
* Ubuntu Xenial: VM images 

## Author
William Hadden - *All work*