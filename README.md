# HealthSciHelper
 
Idea is to promote other oppurnities for Health Science first year 
Students at Otago University

A website composed of three virtual machines. The first hosts the webserver that deals with user interaction,
while another holds the paper data while the final one defines the RESTful-api that is used to relate the two serves  

 ### Build instuctions 
 To access the remote server, use the remote explorer config.
 Create new ones in the C drive (.ssh) folder 
 Use vagrant ssh-config to get details of new vms

 Opens in /home/vagrant which is different to /vagrant

Then in new Window open from wherever suits


### Usage
use vagrant up to start 

Running the api
python api.py


# Useful debugging 

- Error in apahce config

cd /etc/apache2

apache2ctl configtest

recommend using vsode with the remote ssh extension. 
Simply change to the directory with the Vagrantfile
and get the ssh-config using 
~/vagrant/machine$ vagrant ssh-config
Then copy and paste the ouput into an ssh config file.
(default at ~/.ssh/config)

# Current Website configuration 

(localhost)
http://127.0.0.1:8080


### Architecture

private network:
Database
Scraper vm

LAMP Stack

API
RESTful API (flask) to connect the database and the front end webserver

public:
webserver 

Uses virtualbox provisioning

### Next Steps:

Export the conda env so it can be repoduced:
conda env export > environment.yml

Define the API

get API vm running 

Then look to provision with ansible/aws

Generate Private Keys 

Call pipenv creation in base directory (possibility)

### TODO

Initalise the Pipfiles in the root or not?
Seems cleaner to do it on remote but is slowww
Could add more memory/cpu to the machine?

Note Log in as vagrant user