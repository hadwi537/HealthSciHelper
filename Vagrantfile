# -*- mode: ruby -*-
# vi: set ft=ruby :

# A Vagrant File to setup two VMs, a websever and a database server
# connected using an internal network with manually assigned 
# IP addresses for the VMs
Vagrant.configure("2") do |config|

  # Box type to use
  config.vm.box = "ubuntu/focal64"
  
  #Web server VM configuration
  config.vm.define "webserver" do |webserver|
    webserver.vm.hostname = "webserver"

    # allows host computer to connect to IP address 127.0.0.1 port 8080, and that network
    # request will reach the webserver VM's port 80
    webserver.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

    # Setup a private network to allow VMs to communicate with each other
    # a form such as 192.168.2.x for x 
    webserver.vm.network "private_network", ip: "192.168.2.11"

    # Required for some environments
    webserver.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=777"]




  # Shell commands that specifiy the provisioning of the webserver VM.
  # Note the file test-website.conf is copied from this host to the VM
  # through the shared folder mounted in the VM at /vagrant
  webserver.vm.provision "shell", inline: <<-SHELL
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
  SHELL
end

#Section that defines the database server
config.vm.define "dbserver" do |dbserver|
  dbserver.vm.hostname = "dbserver"

  # Note differnet IP from webserver
  dbserver.vm.network "private_network", ip: "192.168.2.14"

  dbserver.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=777"]
  
  # provisioning script
  dbserver.vm.provision "shell", inline: <<-SHELL
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
  SHELL
  end

end

# LocalWords: webserver focal64