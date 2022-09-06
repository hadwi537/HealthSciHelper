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
run 'vagrant up' in the terminal to create the application

### Architecture

HealthSciHelper is based off a LAMP stack web architecture with a few differences.
First, the front end and back end are hosted on Linux virtual machines that are provisined using vagrant with virtualbox.
A public facing webserver front end controls and hosts (via apache) the display and user interaction. 
This webserver follows a typical client-server relation.

This webserver then accesses via a private network, a backend, database server.
This mySQL database contains univeristy paper information, updated every time step by the 'scraper' virtual machine.

The scraper virtual machine controls the running of the webscapers to automatically scrape data from the selected
universities site in an automated fashion using cron timers. This virtual machine then updates the database backend 
with the newly scraped paper information. 
# Useful debugging 

recommend using vsode with the remote ssh extension. 
Simply change to the directory with the Vagrantfile
and get the ssh-config using 
~/vagrant/machine$ vagrant ssh-config
Then copy and paste the ouput into an ssh config file.
(default at ~/.ssh/config)

# Current Website configuration 

(localhost)
http://127.0.0.1:8080

### Next Steps:

* Generate Private Keys and redifine/improve security

* Call pipenv creation in base directory (possibility)

* Initalise the Pipfiles in the root or not?
* Seems cleaner to do it on remote but is slowww
* Could add more memory/cpu to the machine?

* Note Log in as vagrant user