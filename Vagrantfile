# -*- mode: ruby -*-
# vi: set ft=ruby :

# A Vagrant File to setup two VMs, a websever and a database server
# connected using an internal network with manually assigned 
# IP addresses for the VMs
Vagrant.configure("2") do |config|

  # Box type to use
  config.vm.box = "ubuntu/focal64"
  
  #Web server VM configuration (front end)
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
  webserver.vm.provision "shell", path: "build-webserver-vm.sh"
end

#Section that defines the database backend
config.vm.define "dbserver" do |dbserver|
  dbserver.vm.hostname = "dbserver"

  # Note differnet IP from webserver
  dbserver.vm.network "private_network", ip: "192.168.2.14"

  dbserver.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=777"]
  
  # provisioning script
  dbserver.vm.provision "shell", path: "build-dbserver-vm.sh"
  end

  # this section will define the VM that runs the scaper and upadates the database.
  config.vm.define "scraper" do |scraper|
    scraper.vm.hostname = "scraper"

    # Private server to allow vms to communicate
    scraper.vm.network "private_network", ip: "192.168.2.15"

    scraper.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant", mount_options: ["dmode=775,fmode=777"]

    # configure virtualbox provider
    scraper.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = '2048'
    end

    scraper.vm.provision "shell", path: "build-scraper-vm.sh"

  end
end




# LocalWords: webserver focal64


