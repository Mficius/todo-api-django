# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "bento/ubuntu-24.04"

  config.vm.define "todo" do |todo|
    todo.vm.network "private_network", ip: "192.168.56.2"
    # port forwarding
    #todo.vm.network "forwarded_port", guest: 80, host: 8080
    todo.vm.hostname = "todo"
    todo.vm.provider "virtualbox" do |vb|
      vb.name = "todo"
      vb.memory = "2048"
      vb.cpus = 2

    end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    #install docker
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    # ajout user to docker group
    sudo groupadd docker
    sudo usermod -aG docker $USER
    # install apache
    apt-get install -y apache2

  SHELL

  end

end
