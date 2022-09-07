#!/bin/sh


# Adding Repo
echo "-------------------------- ADDING REPO -------------------------------------"
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Updating Package Index and Installing MongoDB-4.4
echo "-------------------------- UPDATING PACKAGE INDEX -------------------------------------"
sudo apt update

echo "-------------------------- INSTALL PACKAGES --------------------------"
apt-get install -y mongodb-org=4.4.8 mongodb-org-server=4.4.8 mongodb-org-shell=4.4.8 mongodb-org-mongos=4.4.8 mongodb-org-tools=4.4.8
apt-get install -y mongodb-mongosh

# Start and Enable Mongod - not work  - CPU not support this version
echo "-------------------------- START & ENABLE MONGOD --------------------------"
sudo systemctl enable --now mongod

sleep 20

echo "-------------------------- CREATE VAGRANT USER --------------------------"
mongosh << BLK
use admin
db.createUser(
{
    user: "vagrant",
    pwd: "vagrant",
    roles: [
              { role: "userAdminAnyDatabase", db: "admin" },
              { role: "readWriteAnyDatabase", db: "admin" },
              { role: "dbAdminAnyDatabase", db: "admin" },
              { role: "clusterAdmin", db: "admin" }
           ]
})
exit
BLK


## Enable Authorization

sudo cat << EOB >> /etc/mongod.conf
#security:
security:
    authorization: "enabled"
EOB


## Listen on any interface so webserver can connect
# use sed to search and replace bindIp variable
# connect to localhost
# sed -i "s,\\(^[[:blank:]]*bindIp:\\) .*,\\1 0.0.0.0," /etc/mongod.conf

# sed -i "s,\\(^[[:blank:]]*bindIp:\\) .*,\\1 127.0.0.1,192.168.2.11,192.168.2.15," /etc/mongod.conf
# sed -i 's/^\( *bindIp *: *\).*/\1 0.0.0.0/'

cp /vagrant/mongod.conf /etc/


echo "-------------------------- RESTARTED MONGOD --------------------------"
sudo systemctl restart mongod

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

pipenv install pymongo

# insert default values
pipenv run python /vagrant/setup-mongodb.py