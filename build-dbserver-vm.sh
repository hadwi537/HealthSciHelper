#!/bin/bash

apt-get update
# Create shell variable MYSQL_PWD that contains the root password
export MYSQL_PWD='insecure_mysqlroot_pw'
# Answer the password prompts
echo "mysql-server mysql-server/root_password password $MYSQL_PWD" | debconf-set-selections 
echo "mysql-server mysql-server/root_password_again password $MYSQL_PWD" | debconf-set-selections

#Install the database server
apt-get -y install mysql-server
# Create database
echo "CREATE DATABASE fvision;" | mysql
# Create a database user with password
echo "CREATE USER 'webuser'@'%' IDENTIFIED BY 'insecure_db_pw';" | mysql

# Grant all priviliges
echo "GRANT ALL PRIVILEGES ON fvision.* TO 'webuser'@'%'" | mysql
export MYSQL_PWD='insecure_db_pw'

# Run all SQL in setup-database.sql file
# Specifiy user and database
cat /vagrant/setup-database.sql | mysql -u webuser fvision

# Find bind address within mysqld.cnf config gle and then change to 127.0.0.1 so 
# accepts local connections only then accept connections from any network interface
sed -i'' -e '/bind-address/s/127.0.0.1/0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf
service mysql restart