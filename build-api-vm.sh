#!/bin/bash

apt-get update
# apt-get install apache2
# apt-get install libapache2-mod-wsgi-py3 python-dev

# installing miniconda

# Create directory
mkdir -p ~/miniconda3

# download miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

# run install script
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

# delete install scripts
rm -rf ~/miniconda3/miniconda.sh

# add conda init to shell and/or zsh shell
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

# restart current shell to apply changes
exec $SHELL



# Change VM's API's configuration to use the shared folder.
# We want to copy it across so runs with linux permissions
# and not a network folder
cp -r /vagrant/api /home/vagrant/

# then move into the api folder
cd api


# TODO This currently will not work
# need to provision either more RAM or increase 
# the swap space

# create conda environment from api scaper yml 
conda env create -f scaper.yml

# activate
conda activate