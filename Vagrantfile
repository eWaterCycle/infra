# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2004"
  config.vm.synced_folder ".", "/vagrant"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  config.vm.network "public_network"
  config.vm.hostname = "ewc-explorer-jupyterhub"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = 8096
    vb.cpus = 4
  end

  config.vm.disk :disk, size: "20GB", name: "home2"
  config.vm.disk :disk, size: "50GB", name: "cache"

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "vagrant-provision.yml"
    ansible.become = true
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "research-cloud-plugin.yml"
    ansible.become = true
    ansible.extra_vars = "research-cloud-plugin.vagrant.vars"
  end
end
