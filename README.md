# Setup of eWaterCycle system on Research cloud

![Ansible Lint](https://github.com/eWaterCycle/infra/workflows/Ansible%20Lint/badge.svg)
[![Concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1462548.svg)](https://doi.org/10.5281/zenodo.1462548)

On the [SURF ResearchCloud](https://researchclouddocs.readthedocs.io/en/latest/about.html) an eWatercycle application will be available that when started will give

* Explorer: web visualization of available models / parameter sets combinations and a way to generate Jupyter notebooks
* Jupyter Hub: to interactivly generate forcings and perform experiments on hydrological models using the [eWatercycle Python package](https://ewatercycle.readthedocs.io/)
* ERA5 and ERA-Interim global climate data, which can be used to generate forcings
* Installed models and their example parameter sets

For people who got access to eWatercycle server can read the [User guide](USER.md), the rest of this document is aimed at eWatercycle developers and deployers.

Previously the eWatercycle platform consisted of multiple VM on SURF HPC cloud, see [v0.1.2 release](https://github.com/eWaterCycle/infra/releases/tag/v0.1.2) for that code.

## Technical specs

An application on the SURF Research cloud is provisioned by running an Ansible playbook (research-cloud-plugin.yml).

In addition to the standard VM storage, additional read-only datasets are mounted at `/mnt/data` from dCache using rclone. They may contain things like:

* climate data, see <https://ewatercycle.readthedocs.io/en/latest/system_setup.html#download-climate-data>
* observation
* parameter-sets, example use cases and bigger ones
* singularity-images of hydrological models wrapped in grpc4bmi servers

## Local test VM

This chapter is dedicated for application developers.

To set up an Explorer/Jupyter server on your local machine with [vagrant](https://vagrantup.com) and
 [Ansible](https://docs.ansible.com/ansible/latest/index.html)

Create config file `research-cloud-plugin.vagrant.vars` with

```yaml
---
dcache_ro_token: <dcache macaroon with read permission>
rclone_cache_dir: /data/volume_2
# Directory where /home should point to
alt_home_location: /data/volume_3
```

The token can be found in the eWaterCycle password manager.

```shell
vagrant --version
# Vagrant 2.2.18
vagrant plugin install vagrant-vbguest
# Installed the plugin 'vagrant-vbguest (0.30.0)'
export VAGRANT_EXPERIMENTAL="disks"
vagrant up
```

Visit site

```shell
# Get ip of server with
vagrant ssh -c 'ifconfig eth1'
```

Go to `http://<ip of eth1>` and login with `vagrant:vagrant`.

You will get some complaints about unsecure serving, this is OK for local testing and this will not happen on Research Cloud.

### Test on Windows Subsystem for Linux 2

WSL2 users should follow steps on [https://www.vagrantup.com/docs/other/wsl](https://www.vagrantup.com/docs/other/wsl).

Importantly:

* Work on a folder on the windows file system.
* Export VAGRANT_WSL_WINDOWS_ACCESS_USER_HOME_PATH="/mnt/c/.../infra"
* Install [virtualbox_WSL2 vagrant plugin](https://github.com/Karandash8/virtualbox_WSL2)
* Approve the firewall popup

## Application registration

This chapter is dedicated for application developers.

On the Research cloud the application developer can add an application for other people to use.
The steps to do this are documented [here](https://servicedesk.surfsara.nl/wiki/display/WIKI/Create+your+own+applications).

For eWatercycle application following specialization was done

* Set `research-cloud-plugin.yml` file in [this repo](https://github.com/eWaterCycle/infra) as plugin script source
* Set a fixed plugin parameter called `dcache_ro_token` for dcache read-only token. The token can be found in the eWaterCycle password manager.
* Set a fixed plugin parameter called `alt_home_location` to `/data/volume_2` for mount point of the storage item which should hold homes
mounted.
* Set a fixed plugin parameter called `rclone_cache_dir` to `/data/volume_3` for directory where rclone can store its cache.
* Set a fixed plugin parameter called `rclone_max_gsize` to `45`.
* Set application parameter `co_roles_enabled` to False
    TODO use a group members in SRAM (https://github.com/SURFscz/SBS#api or https://wiki.surfnet.nl/display/SRAM/Connect+a+service+to+LDAP) to define who can do sudo and who can admin JupyterHub
* Set application offer flavours to Ubuntu 20.04 operating system

## Research cloud VM deployment

This chapter is dedicated for application deployers.

1. Log into Research Cloud
1. Create new storage item for home directories
    * To store user files
    * Use 50Gb size for simple experiments or bigger when required for experiment.
    * As each storage item can only be used by a single workspace, give it a name and description so you to which workspace you want to connect later.
1. Create new storage item for cache
    * To store cached files from dCache by rclone
    * Use 50GB size as size
    * As each storage item can only be used by a single workspace, give it a name and description so you to which workspace you want to connect later.
1. Create new workspace
1. Select eWaterCycle application
1. Select collaborative organisation (CO) for example `ewatercycle-nlesc`
1. Select size of VM (cpus/memory) based on use case
1. Select home storage item.
    * Order in which the storage items are select is important, make sure to select home before cache storage item.
1. Select cache storage item
1. Wait for machine to be running
1. Visit URL/IP
1. When done delete machine

For a new CO make sure

* application is allowed to be used by CO.
* data storage item and home dir are created for the CO

End user should be invited to CO so they can login.

See [User guide](USER.md) to see what users have to do to login or use GitHub repository.

### Example notebooks

To get example notebooks end users should use following URL (with `<workspace id>` with your currently running workspace)

```html
https://<workspace id>.workspaces.live.surfresearchcloud.nl/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FeWaterCycle%2Fewatercycle&urlpath=lab%2Ftree%2Fewatercycle%2Fdocs%2Fexamples%2FMarrmotM01.ipynb&branch=main
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

In the eWaterCycle project we make Docker images. The images are hosted on [Docker Hub](https://hub.docker.com/u/ewatercycle) . A project member can create issues here for permisison to push images to Docker Hub.

## Logs

All services are running with systemd. Their logs can be viewed with `journalctl`.
The log of the Jupyter server for each user can be followed with

```shell
journalctl -f -u jupyter-vagrant-singleuser.service
```

(replace `vagrant` with own username)
