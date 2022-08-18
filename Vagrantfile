# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"


  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # needed for CS labs
  config.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=777"]


  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y apache2 php libapache2-mod-php php-mysql

    export MYSQL_PWD='insecure_mysqlroot_pw' 
    echo "mysql-server mysql-server/root_password password $MYSQL_PWD" | debconf-set-selections
    echo "mysql-server mysql-server/root_password_again password $MYSQL_PWD" | debconf-set-selections
    apt-get -y install mysql-server
    echo "CREATE DATABASE fvision;" | mysql
    echo "CREATE USER 'webuser'@'%' IDENTIFIED BY 'insecure_db_pw';" | mysql
    echo "GRANT ALL PRIVILEGES ON fvision.* TO 'webuser'@'%'" | mysql

    export MYSQL_PWD='insecure_db_pw'
    cat /vagrant/setup-database.sql | mysql -u webuser fvision

    # Change VM's webserver's configuration to use the shared folder.
    # See test-website.conf for details
    cp /vagrant/test-website.conf /etc/apache2/sites-available/
    #Install custom web config and disable the defualt
    a2ensite test-website
    a2dissite 000-default
    systemctl reload apache2
    service apache2 reload
  SHELL
end
