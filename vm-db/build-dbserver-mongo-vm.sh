#!/bin/sh


curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
apt-get update

cp -r /vagrant/vm-db /home/vagrant/


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
# use cutom config to setup ports 

cp /vagrant/vm-db/mongod.conf /etc/


echo "-------------------------- RESTARTED MONGOD --------------------------"
sudo systemctl restart mongod

cd vm-db
npm install

npm i -g forever

service mongod start &

forever start server.js &



