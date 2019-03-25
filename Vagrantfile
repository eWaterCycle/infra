# -*- mode: ruby -*-
# vi: set ft=ruby :

domain = '.local'

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.network "public_network"
  
  config.vm.provision "shell", inline: <<-SHELL
    #disable ipv6
    echo "disabling ipv6"
    sudo echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf
    sudo echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf
    sudo echo "net.ipv6.conf.lo.disable_ipv6 = 1" >> /etc/sysctl.conf
  SHELL
  config.vm.provision "fix-no-tty", type: "shell" do |s|
    s.privileged = false
    s.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
  end

  config.vm.persistent_storage.enabled = true
  config.vm.persistent_storage.size = 80000
  config.vm.persistent_storage.mountname = 'mnt'
  config.vm.persistent_storage.filesystem = 'xfs'
  config.vm.persistent_storage.mountpoint = '/mnt'
  config.vm.persistent_storage.volgroupname = 'extra'
  # Xenial wrong disk fix, see https://github.com/kusnier/vagrant-persistent-storage/issues/59
  config.vm.persistent_storage.diskdevice = '/dev/sdc'
  
  config.vm.define "lab" do |lab|
    lab.vm.hostname = "lab", domain
	lab.persistent_storage.location = "lab-extra.vdi"
    lab.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
	  vb.cpus = 1
    end
  end
  config.vm.define "explore" do |explore|
    explore.vm.hostname = "explore", domain
	explore.persistent_storage.location = "explore-extra.vdi"
    explore.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
	  vb.cpus = 1
    end
  end
  config.vm.define "jupyter" do |jupyter|
    jupyter.vm.hostname = "jupyter", domain
	jupyter.persistent_storage.location = "jupyter-extra.vdi"
    jupyter.vm.provider "virtualbox" do |vb|
      vb.memory = 8096
	  vb.cpus = 4
    end
  end  
  
  # Hostmanager should be set to false so it runs after provisioning
  config.hostmanager.enabled = false
  config.hostmanager.manage_guest = true
  config.hostmanager.manage_host = true
  config.hostmanager.include_offline = false
  config.hostmanager.ignore_private_ip = true
  config.hostmanager.ip_resolver = proc do |machine|
    result = ""
    machine.communicate.execute("hostname -I") do |type, data|
        result << data if type == :stdout
    end
    ip = result.split[1]
  end
  config.vm.provision :hostmanager
end
