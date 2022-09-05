#!/bin/bash

apt-get update && sudo apt upgrade

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



# Change VM's API's configuration to use the shared folder.
# We want to copy it across so runs with linux permissions
# and not a network folder

cp -r /vagrant/scraper /home/vagrant/

# then move into the api folder
cd scraper

Assign more swap space so conda can install packages
sudo fallocate -l 1G /swapfile 
sudo chmod 600 /swapfile 
sudo mkswap /swapfile 
sudo swapon /swapfile 
sudo cp /etc/fstab /etc/fstab.bak 
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab


# create virtal environment
pipenv install -r requirements.txt

# start the virtualenv
pipenv shell
