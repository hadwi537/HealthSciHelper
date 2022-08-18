#!/bin/bash

apt-get update
apt-get install -y apache2 php libapache2-mod-php php-mysql

# Change VM's webserver's configuration to use the shared folder.
# See test-website.conf for details
cp /vagrant/test-website.conf /etc/apache2/sites-available/
#Install custom web config 
a2ensite test-website
# Disable default website
a2dissite 000-default
# reload webserver config and pick up changes
systemctl reload apache2
service apache2 reload