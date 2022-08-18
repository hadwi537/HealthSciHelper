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
    apt-get install -y apache2

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
