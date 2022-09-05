# HealthSciHelper
 
Idea is to promote other oppurnities for Health Science first year 
Students at Otago University

A website composed of two virtual machines. One managing the site apperence 
while the other loads a MySQL database

 ### Build instuctions 
 To access the remote server, use the remote explorer config.
 Create new ones in the C drive (.ssh) folder 
 Use vagrant ssh-config to get details of new vms

Then in new Window open from wherever suits


### Usage
use vagrant up to start 

Opens in /home/vagrant which is different to /vagrant

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

API
RESTful API (flask)

public:
webserver 

Ultimetly,
Provision using ansible to allow integration with AWS 


### Next Steps:

Export the conda env so it can be repoduced:
conda env export > environment.yml

Define the API

get API vm running 

Then look to provision with ansible/aws

Generate Private Keys 

Call pipenv creation in base directory (possibility)

### OTHER

# For exporting the conda environment without build specific stuff
conda env export -n scraper -f scaper.yml --no-builds

