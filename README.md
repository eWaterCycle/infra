# Setup of eWaterCycle system on Research cloud

![Ansible Lint](https://github.com/eWaterCycle/infra/workflows/Ansible%20Lint/badge.svg)

On the [SURF ResearchCloud](https://researchclouddocs.readthedocs.io/en/latest/about.html) a eWatercycle application will be available that when started will give

* Explorer: web visualization of available models / parameter sets combinations and a way to generate Jupyter notebooks
* Jupyter Hub: to interactivly generate forcings and perform experiments on hydrological models using the [eWatercycle Python package](https://ewatercycle.readthedocs.io/)
* ERA5 and ERA-Interim global climate data, which can be used to generate forcings
* Installed models and their example parameter sets

Previously the eWatercycle platform consisted of multiple VM on SURF HPC cloud, see [v0.1.2 release](https://github.com/eWaterCycle/infra/releases/tag/v0.1.2) for that code.

## Local test VM

This chapter is dedicated for application developers.

To setup a Explore/Jupyter server on your local machine with [vagrant](https://vagrantup.com) and
 [Ansible](https://docs.ansible.com/ansible/latest/index.html)

```shell
vagrant --version
# Vagrant 2.2.18
vagrant plugin install vagrant-vbguest
# Installed the plugin 'vagrant-vbguest (0.30.0)'
vagrant up
vagrant ssh
sudo -i
ansible-playbook -e launcher_jupyterhub_token=somesecret -e dcache_ro_token=<a macaroon from password manager> research-cloud-plugin.yml
```

Visit site

```shell
vagrant ssh
# Get ip of server with
ifconfig eth1
```

Go to `http://<ip of eth1>` and login with `vagrant:vagrant`.

## Application registration

This chapter is dedicated for application developers.

On the Research cloud the application developer can add an application for other people to use.
The steps to do this are documented [here](https://servicedesk.surfsara.nl/wiki/display/WIKI/Create+your+own+applications).

For eWatercycle application following specialization was done

* Set `research-cloud-plugin.yml` file in [this repo](https://github.com/eWaterCycle/infra) as plugin script source
* Set a fixed plugin parameter for dcache read-only token
* Set a fixed plugin parameter for launchers jupyter hub token
* Set application paremeter `co_roles_enabled` to False
* Set application offer flavours to Ubuntu 20.04 operating system

## Research cloud VM deployment

This chapter is dedicated for application deployers.

1. Log into Research Cloud
1. Create new workspace
1. Select eWaterCycle application
1. Select collaborative organisation (CO) `ewatercycle-nlesc`
1. Select size of VM (cpus/memory) based on use case
1. Select data and home storage items
1. Wait for machine to be running
1. Visit URL/IP
1. When done delete machine

For a new CO make sure

* application is allowed to be used by CO.
* data storage item and home dir are created for the CO

End user should be invited to CO and then

1. to login to Jupyter, he/she should setup TOTP on SRC dashboard profile page
2. optionally to ssh into machine, the ssh pub key must be added to https://sbs.sram.surf.nl/profile

### Example notebooks

To get example notebooks end users should use following URL (with `<workspace id>` with your currently running workspace)

```html
https://<workspace id>.workspaces.live.surfresearchcloud.nl/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FeWaterCycle%2Fewatercycle&urlpath=lab%2Ftree%2Fewatercycle%2Fdocs%2Fexamples%2FMarrmotM01.ipynb&branch=main
```

TODO add this link to home page of server at

This link uses [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/) to sync a git repo and open a notebook in it.

## Fill shared data disk

This chapter is dedicated for application data preparer.

The [eWatercycle system setup](https://ewatercycle.readthedocs.io/en/latest/system_setup.html) requires a lot of data files.
For the Research cloud virtual machines we will mount a dcache bucket.

To fill the dcache bucket you can run

```shell
ansible-playbook \
  -e cds_uid=1234 -e cds_api_key <cds api key> \
  -e dcache_rw_token=<dcache macaroon with read/write permissions>
  research-cloud-plugin.yml
```

Runnig this script will download all data files to /mnt/data and upload them to dcache.

## Docker images

In the eWaterCycle project we make Docker images. The images are hosted on [Docker Hub](https://hub.docker.com/u/ewatercycle) . A project member can create issues here for permisison to push images to Dockuer Hub.
