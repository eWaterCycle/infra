# Setup of eWatercycle system

* Runs on the [SURFSara HPC cloud](https://userinfo.surfsara.nl/systems/hpc-cloud)
* Provisioned by [Ansible](https://docs.ansible.com/ansible/latest/index.html)

# Prerequisites

Install Ansible

```bash
pipenv --three install
pipenv shell
```

Install roles from [galaxy](https://galaxy.ansible.com/)
```bash
ansible-galaxy install -r requirements.yml
```

On the https://ui.hpccloud.surfsara.nl add your public SSH key so you can login the Virtual Machines.

# Servers

* lab.ewatercycle.org - entry page to select other servers
* explore.ewatercycle.org - terriajs with models+datasets and launcher
* jupyter.ewatercycle.org - jupyterhub
* analytics.ewatercycle.org - 
* experiments.ewatercycle.org - cylc web interface
* forecast.ewatercycle.org - visualization of global low res PCR-GLOBWB model

# Create VMs

All VMs are based on the same template which should be created as follows:

1. Create `lab` template from App called `Ubuntu-18.04.1-Server (...)`
    1. Select the ssd datastore for the image
2. Update `lab` template
    1. Set to 8Gb RAM and 2 cpus/vcpus
    2. Add Volatile disk of 500Gb, type=FS and format=raw, for storage of apps, docker and homedirs

Create the following Virtual Machines based on the `lab` template with the following settings:

|VM name   | Memory (GB) | VCPU  | DISK 0 (GB) | DISK 1 (GB)  |
|---|---|---|---|---|
| lab  | 1  | 1  | 10  | 10  |
| explore  | 1  | 1  | 10  | 10  |
| jupyter  | 8  | 2  | 50  | 1500  |
| analytics  | 1  | 1  | 2 | 10  |
| experiments  | 8  | 2  | 50  | 500 |
| forecast  | 8  | 2  | 50  | 500 |

# Setup domain names

In the DNS admin interface of the `ewatercycle.org` domain setup sub domains for all machines.

# Configure

## Inventory

Make a copy of `inventory.yml.template` to `inventory.yml` and update if needed.

## Variables

Make a copy of all the `group_vars/*.yml.template` to `group_vars/*.yml`.
Fields with `REPLACE ME` in the value need to be replaced.

### Authorized keys

To allow multiple users to ssh into servers the Ansible playbooks will inject the public keys listed in `group_vars/all.yml:authorized_keys` file into `~/authorized_keys`.

# Provision VMs

After the VMs haven been created, the subdomain are setup and configuration has been performed then you are ready to provision the VMs with:

```bash
ansible-playbook -i inventory.yml site.yml
```
Or to provision a group of machines
```bash
ansible-playbook -i inventory.yml jupyter.yml
```

# Backup certificates

The servers have let's encrypt https certficates.
During provisioning the certificates are backuped to the ansible client in the `letsencrypt/<hostname>` directory.
The certs are automaticly renewed when they expire (cert has 90 day lifetime).
To backup the renewed certs run the following command:

```bash
ansible remote -i inventory.yml -m synchronize -a 'src=/etc/letsencrypt/ dest="letsencrypt/{{ inventory_hostname }}/" recursive=yes mode=pull'
```
