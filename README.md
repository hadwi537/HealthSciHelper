# HealthSciHelper
 
This project aims to promote other oppurtunities for Health Science first year 
Students at Otago University. 

 ### Build instuctions 
 To access the remote server, use the remote explorer config.
 Create new ones in the C drive (.ssh) folder 
 Use vagrant ssh-config to get details of new vms

 Opens in /home/vagrant which is different to /vagrant

Then in new Window open from wherever suits

### Usage
run 'vagrant up' in the terminal to create the application

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
http://127.0.0.1:8080

### Next Steps:

* Generate Private Keys and redifine/improve security

* Call pipenv creation in base directory (possibility)

* Initalise the Pipfiles in the root or not?
* Seems cleaner to do it on remote but is slowww
* Could add more memory/cpu to the machine?

* Note Log in as vagrant user

* Some papers require some number of 'generic' points, i.e non-specific points