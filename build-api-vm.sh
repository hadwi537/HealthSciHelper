#!/bin/bash

apt-get update
# apt-get install apache2
# apt-get install libapache2-mod-wsgi-py3 python-dev

# Change VM's API's configuration to use the shared folder.
# We want to copy it across so runs with linux permissions
# and not a network folder
cp -r /vagrant/api /home/vagrant/

# then move into the api folder
cd api

