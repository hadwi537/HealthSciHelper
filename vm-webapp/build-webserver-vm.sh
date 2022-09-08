#!/bin/bash

# get release
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

# for developing node.js
sudo apt-get install -y nodejs

# refresh
apt-get update

# copy over folder
cp -r /vagrant/vm-webapp /home/vagrant/

cd /home/vagrant/vm-webapp

# install all current dependices
npm install

# to start and forever run the webapp
nohup npm start &

apt install net-tools


