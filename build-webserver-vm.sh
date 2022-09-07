#!/bin/bash

apt-get update
apt-get install -y apache2 php libapache2-mod-php php-mysql

# Change VM's webserver's configuration to use the shared folder.
# See test-website.conf for details
cp /vagrant/test-website.conf /etc/apache2/sites-available/

# folder to build visualisation from
cp -r /vagrant/visualise /home/vagrant/

chmod +x /home/vagrant/visualise/plot_graph.py


#Install custom web config 
a2ensite test-website
# Disable default website
a2dissite 000-default
# reload webserver config and pick up changes
systemctl reload apache2
service apache2 reload

npm install mongodb

# Need this to get 3.10
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# install python and pip with yes to all prompts
apt-get install -y python3
apt-get install -y python3-pip
apt-get install -y python3.8-venv
apt-get install -y pipenv
sudo apt install -y python3.10

# for dsplot
# get the library
apt-get install -y graphviz libgraphviz-dev 

cd visualise

# # install package
sudo pipenv install dsplot

sudo pipenv install pymongo

