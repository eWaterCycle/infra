## Setup of eWaterCycle platform on a local test VM

Deploying a local test VM is mostly useful for developing the SURF Research Cloud applications. This vagrant setup creates a virtual machine with 8Gb memory, 4 virtual cores, and 70Gb storage. This should work on any Linux or Windows machine.

To set up an Explorer/Jupyter server on your local machine with [vagrant](https://vagrantup.com) and
[Ansible](https://docs.ansible.com/ansible/latest/index.html)

Create config file `research-cloud-plugin.vagrant.vars` with

```yaml
---
shared_data_source: dcache
# If set to samba you need to run the file server, see next chapter
# shared_data_source: samba
# When using source samba you need to also give the ip of the file server
# This can be retrieved with `vagrant ssh fileserver -c 'ip addr show eth1'`
# private_smb_server_ip:
#   - <ip of file-server>
# When using source samba you need to also give a password
# it is hardcoded in vagrant-provision-file-server.yml to samba
# samba_password: samba
dcache_ro_token: <dcache macaroon with read permission>
rclone_cache_dir: /data/volume_2
# Directory where /home should point to
alt_home_location: /data/volume_3
# Vagrant user is instructor
# The students defined below can be used to login as a student
students: 'student1:pw1,student2:pw2'
```

The token can be found in the eWaterCycle password manager.

```shell
vagrant --version
# Vagrant 2.4.1
vagrant up
```

Visit site

```shell
# Get ip of server with
vagrant ssh -c 'ifconfig eth1'
```

Go to `http://<ip of eth1>` and login with `vagrant:vagrant`.

You will get some complaints about unsecure serving, this is OK for local testing and this will not happen on Research Cloud.

### Vagrant File server

The file server can also be tested locally with Vagrant using:

```shell
vagrant up fileserver
# Pick same bridged network interface for the Jupyter server
vagrant ssh fileserver
```

And follow the steps in the [File Server](#populating-samba-file-server) section, but instead of cloning repo you can `cd /vagrant` and run ansible commands.

To clean up use

```shell
vagrant destroy fileserver
```

### Test on Windows Subsystem for Linux 2

WSL2 users should follow steps on [https://www.vagrantup.com/docs/other/wsl](https://www.vagrantup.com/docs/other/wsl).

Importantly:

- Work on a folder on the windows file system.
- Install vagrant plugin https://github.com/Karandash8/virtualbox_WSL2
- `export VAGRANT_WSL_WINDOWS_ACCESS_USER_HOME_PATH=$PWD`
- `export PATH="$PATH:C:\Program Files\Oracle\VirtualBox"`
- `vagrant up --provider virtualbox`
- Approve the firewall popup