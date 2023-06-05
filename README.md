# Instructions for system administrators to deploy the eWaterCycle platform

![Ansible Lint](https://github.com/eWaterCycle/infra/workflows/Ansible%20Lint/badge.svg)
[![Concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1462548.svg)](https://doi.org/10.5281/zenodo.1462548)

This repo contains (codified) instructions for deploying the eWaterCycle platform. The target audience of these instructions are system administrators. For more information on the eWaterCycle platform (and how to deploy it) see the [eWaterCycle documentation](https://ewatercycle.readthedocs.io/).

For instructions on how to use the machine as deployed by this repo see the [User guide](USER.md).

These instructions assume you have some basic knowledge of [vagrant](https://vagrantup.com) and
[Ansible](https://docs.ansible.com/ansible/latest/index.html).

## Setup of eWaterCycle platform on the SURF Research cloud

The hardware environment used by the eWaterCycle platform development team is the [SURF Research Cloud](https://servicedesk.surfsara.nl/wiki/display/WIKI/Research+Cloud+Documentation). Starting a machine on the Surf Research Cloud requires that you have research budget with SURF, for more info see the website of [SURF](https://www.surf.nl/en/research-it/apply-for-access-to-compute-services). Once running, access to the machine can be shared to anyone.

The setup instructions in this repo will create an eWaterCycle application(a sort-of VM template) that when started will create a machine with:

- Explorer: web visualization of available models / parameter sets combinations and a way to generate Jupyter notebooks
- Jupyter Hub: to interactivly generate forcings and perform experiments on hydrological models using the [eWatercycle Python package](https://ewatercycle.readthedocs.io/)
- ERA5 and ERA-Interim global climate data, which can be used to generate forcings
- Installed models and their example parameter sets

An application on the SURF Research cloud is provisioned by running an Ansible playbook (research-cloud-plugin.yml).

In addition to the standard VM storage, additional read-only datasets are mounted at `/mnt/data` from dCache using rclone. They may contain things like:

- climate data, see <https://ewatercycle.readthedocs.io/en/latest/system_setup.html#download-climate-data>
- observation
- parameter-sets
- singularity-images of hydrological models wrapped in grpc4bmi servers

Previously the eWatercycle platform consisted of multiple VM on SURF HPC cloud, see [v0.1.2 release](https://github.com/eWaterCycle/infra/releases/tag/v0.1.2) for that code.

## Setup of eWaterCycle platform on a local test VM

Deploying a local test VM is mostly useful for developing the SURF Research Cloud applications. This vagrant setup creates a virtual machine with 8Gb memory, 4 virtual cores, and 70Gb storage. This should work on any Linux or Windows machine.

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

- Work on a folder on the windows file system.
- Export VAGRANT_WSL_WINDOWS_ACCESS_USER_HOME_PATH="/mnt/c/.../infra"
- Install [virtualbox_WSL2 vagrant plugin](https://github.com/Karandash8/virtualbox_WSL2)
- Approve the firewall popup

## Catalog item registration

This chapter is dedicated for catalog item developers.

On the Research cloud the [developer](https://servicedesk.surf.nl/wiki/display/WIKI/Appoint+a+CO-member+a+developer) can add an catalog item for other people to use.
The generic steps to do this are documented [here](https://servicedesk.surf.nl/wiki/display/WIKI/Create+your+own+catalog+items).

For eWatercycle component following specialization was done

- Use Ansible playbook as component script type
  - Use `https://github.com/eWaterCycle/infra.git` as repository URL
  - Use `research-cloud-plugin.yml` as script path
  - Use `main` as tag
- Component parameters, all fixed source type and non-overwitable
  - Add `dcache_ro_token` parameter for dcache read-only token aka macaroon.
    The token can be found in the eWaterCycle password manager.
    This token has an expiration date, so it needs to be updated every now and then.
  - Add `alt_home_location` parameter with value `/data/volume_2`.
    For mount point of the storage item which should hold homes mounted.
  - Add `rclone_cache_dir` parameter with value `/data/volume_3`.
    For directory where rclone can store its cache.
  - Add `rclone_max_gsize` with value `45`.
    For maximum size of cache on `rclone_cache_dir` volume. In Gb.
- Set documentation URL to `https://github.com/eWaterCycle/infra`
- Do not allow every org to use this component. Data on the dcache should not be made public.
- Select the organizations (CO) that are allowed to use the component.

For eWatercycle catalog item following specialization was done

- Select the following components:
  1. SRC-OS
  2. SRC-CO
  3. SRC-Nginx
  4. SRC-External plugin
  5. eWatercycle
- Set documentation URL to `https://github.com/eWaterCycle/infra`
- Add `SURF HPC Cloud` as cloud provider
  - Set Operating Systems to Ubuntu 22.04
  - Set Sizes to all non-gpu and non-disabled sizes
- In parameter settings step keep all values as is except
  - Set `co_irods` to `false` as we do not use irods
  - Set `co_research_drive` to `false` as we do not use research drive
- Set boot disk size to 150Gb,
  as default size will be mostly used by the conda environment and will trigger out of space warnings.
- Set workspace acces button behavior to `Webinterface (https:)`,
  so clicking on `ACCESS` button will open up the eWatercycle experiment explorer web interface
- Select the organizations (CO) that are allowed to use the catalog item.

To become root on a VM the user needs to be member of the `src_co_admin` group on [SRAM](https://sram.surf.nl/).
See [docs](https://servicedesk.surf.nl/wiki/display/WIKI/Workspace+roles%3A+Appoint+a+CO-member+a+SRC+administrator).

## SURF Research cloud VM deployment

This chapter is dedicated for application deployers.

1. Log into Research Cloud
1. Create new storage item for home directories
   - To store user files
   - Use 50Gb size for simple experiments or bigger when required for experiment.
   - As each storage item can only be used by a single workspace, give it a name and description so you know which workspace and storage items go together.
1. Create new storage item for cache
   - To store cached files from dCache by rclone
   - Use 50GB size as size
   - As each storage item can only be used by a single workspace, give it a name and description so you know which workspace and storage items go together.
1. Create a new workspace
1. Select eWaterCycle application
1. Select collaborative organisation (CO) for example `ewatercycle-nlesc`
1. Select size of VM (cpus/memory) based on use case
1. Select home storage item.
   - Order in which the storage items are select is important, make sure to select home before cache storage item.
1. Select cache storage item
1. Wait for machine to be running
1. Visit URL/IP
1. When done delete machine

For a new CO make sure

- application is allowed to be used by CO. See [Sharing catalog items](https://servicedesk.surfsara.nl/wiki/display/WIKI/Sharing+catalog+items)
- data storage item and home dir are created for the CO

End user should be invited to CO so they can login.

See [User guide](USER.md) to see what users have to do to login or use GitHub repository.

### Example notebooks

To get example notebooks end users should use following URL (with `<workspace id>` with your currently running workspace)

```html
https://<workspace id
  >.workspaces.live.surfresearchcloud.nl/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FeWaterCycle%2Fewatercycle&urlpath=lab%2Ftree%2Fewatercycle%2Fdocs%2Fexamples%2FMarrmotM01.ipynb&branch=main</workspace
>
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
  shared-data-disk.yml
```

Runnig this script will download all data files to /mnt/data and upload them to dcache.

## Sync dcache with existing folder elsewhere

The steps above fetch the data from original sources. If you want to sync some files from
another location, say, Snellius, you can use rclone directly. In our experience, it works
better to sync entire directories than to try and copy single files.

Create the file `~/.config/rclone/rclone.conf` and add the following content:

```
[ dcache ]
type = webdav
url = https://webdav.grid.surfsara.nl:2880
vendor = other
user =
pass =
bearer_token = <dcache macaroon with read/write permissions>
```

You can verify your access by running an innocent `rclone ls  dcache:parameter-sets`.
The command to sync directories is `rclone copy somedir dcache:parameter-sets/somedir`.
Beware that this will overwrite any existing files, if different!

Note: password manager can be used for exchanging macaroons.

## Docker images

In the eWaterCycle project we make Docker images. The images are hosted on [Docker Hub](https://hub.docker.com/u/ewatercycle) . A project member can create issues here for permisison to push images to Docker Hub.

## Logs

All services are running with systemd. Their logs can be viewed with `journalctl`.
The log of the Jupyter server for each user can be followed with

```shell
journalctl -f -u jupyter-vagrant-singleuser.service
```

(replace `vagrant` with own username)
