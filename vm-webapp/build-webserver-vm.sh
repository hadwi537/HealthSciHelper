#!/bin/bash

apt-get update

# for developing node.js
sudo apt-get install -y nodejs

# this install NodeSource Node.js repo onto a debian or ubunutu system
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

# refresh changes
apt-get update

# copy over folder
cp -r /vagrant/vm-webserver /home/vagrant/

# install all current dependices
npm install

# to start and forever run the webapp
nohup npm start &



