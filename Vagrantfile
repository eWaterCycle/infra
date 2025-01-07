# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.define "jupyter", primary: true do |jupyter|
    config.vm.box = "bento/ubuntu-22.04"
    config.vm.synced_folder ".", "/vagrant"

    # Create a public network, which generally matched to bridged network.
    # Bridged networks make the machine appear as another physical device on
    # your network.
    jupyter.vm.network "public_network"
    jupyter.vm.hostname = "jupyter"

    # Provider-specific configuration so you can fine-tune various
    # backing providers for Vagrant. These expose provider-specific options.
    # Example for VirtualBox:
    #
    jupyter.vm.provider "virtualbox" do |vb|
      # Customize the amount of memory on the VM:
      vb.memory = 8096
      vb.cpus = 4
    end

    jupyter.vm.disk :disk, size: "20GB", name: "home2"
    # When shared_data_source is set to true, the disk will be unused
    jupyter.vm.disk :disk, size: "50GB", name: "cache"

    # Disable guest updates
    jupyter.vbguest.auto_update = false
    jupyter.vbguest.no_install = true

    jupyter.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "vagrant-provision.yml"
      ansible.become = true
      ansible.compatibility_mode = "2.0"
    end

    jupyter.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "research-cloud-plugin.yml"
      ansible.become = true
      ansible.extra_vars = "research-cloud-plugin.vagrant.vars"
      ansible.compatibility_mode = "2.0"
    end
  end

  config.vm.define "fileserver", autostart: false do |fileserver|
    fileserver.vm.box = "bento/ubuntu-22.04"
    fileserver.vm.synced_folder ".", "/vagrant"

    fileserver.vm.network "public_network"
    fileserver.vm.hostname = "fileserver"

    fileserver.vm.provider "virtualbox" do |vb|
      # Customize the amount of memory on the VM:
      vb.memory = 2048
      vb.cpus = 1
    end

    fileserver.vm.disk :disk, size: "500GB", name: "volume_2"

    # Disable guest updates
    fileserver.vbguest.auto_update = false
    fileserver.vbguest.no_install = true

    fileserver.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "vagrant-provision-file-server.yml"
      ansible.become = true
      ansible.compatibility_mode = "2.0"
    end
  end
end
