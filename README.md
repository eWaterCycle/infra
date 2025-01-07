# Instructions for system administrators to deploy the eWaterCycle platform

![Ansible Lint](https://github.com/eWaterCycle/infra/workflows/Ansible%20Lint/badge.svg)
[![Concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1462548.svg)](https://doi.org/10.5281/zenodo.1462548)

- [Instructions for system administrators to deploy the eWaterCycle platform](#instructions-for-system-administrators-to-deploy-the-ewatercycle-platform)
  - [Setup of eWaterCycle platform on the SURF Research cloud](#setup-of-ewatercycle-platform-on-the-surf-research-cloud)
  - [Setup of eWaterCycle platform on a local test VM](#setup-of-ewatercycle-platform-on-a-local-test-vm)
  - [SURF Reseach cloud catalog item registration](#surf-reseach-cloud-catalog-item-registration)
  - [SURF Research cloud workspace](#surf-research-cloud-workspace)
    - [Shared data source](#shared-data-source)
    - [Preparations](#preparations)
    - [File Server](#file-server)
    - [Workspace creation with dcache as shared data source](#workspace-creation-with-dcache-as-shared-data-source)
    - [Workspace creation with samba as shared data source](#workspace-creation-with-samba-as-shared-data-source)
    - [Students](#students)
    - [Example notebooks](#example-notebooks)
  - [Docker images](#docker-images)
  - [AI Disclaimer](#ai-disclaimer)

This repo contains (codified) instructions for deploying the eWaterCycle platform. The target audience of these instructions are system administrators. For more information on the eWaterCycle platform (and how to deploy it) see the [eWaterCycle documentation](https://ewatercycle.readthedocs.io/).

With grading setup is [one class, one grader](https://nbgrader.readthedocs.io/en/stable/configuration/jupyterhub_config.html#example-use-case-one-class-one-grader).

For instructions on how to use the machine as deployed by this repo see the [User guide](USER.md).

These instructions assume you have some basic knowledge of [vagrant](https://vagrantup.com) and
[Ansible](https://docs.ansible.com/ansible/latest/index.html).

## Setup of eWaterCycle platform on the SURF Research cloud

The hardware environment used by the eWaterCycle platform development team is the [SURF Research Cloud](https://servicedesk.surfsara.nl/wiki/display/WIKI/Research+Cloud+Documentation). Starting a machine on the Surf Research Cloud requires that you have research budget with SURF, for more info see the website of [SURF](https://www.surf.nl/en/research-it/apply-for-access-to-compute-services). Once running, access to the machine can be shared to anyone.

The setup instructions in this repo will create an eWaterCycle application(a sort-of VM template) that when started will create a machine with:

- Jupyter Hub: to interactivly generate forcings and perform experiments on hydrological models using the [eWatercycle Python package](https://ewatercycle.readthedocs.io/)
  - [nbgrader](https://nbgrader.readthedocs.io/en/stable/) for grading
  - [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/) to open a cloned git repository in Jupyter Lab from an [URL](https://nbgitpuller.readthedocs.io/en/latest/link.html)
- ERA5 and ERA-Interim global climate data, which can be used to generate forcings
- Installed models and their example parameter sets

An application on the SURF Research cloud is provisioned by running an Ansible playbook (research-cloud-plugin.yml).

In addition to the standard VM storage, additional read-only datasets are mounted at `/data/shared` from a file server like a samba server or a dcache server. They may contain things like:

- climate data, see <https://ewatercycle.readthedocs.io/en/latest/system_setup.html#download-climate-data>
- observation
- parameter-sets
- singularity-images of hydrological models wrapped in grpc4bmi servers

See [File server chapter](#file-server) for more information on the file server.

Previously the eWatercycle platform consisted of multiple VM on SURF HPC cloud, see [v0.1.2 release](https://github.com/eWaterCycle/infra/releases/tag/v0.1.2) for that code.

## Setup of eWaterCycle platform on a local test VM

For developing the SURF Research Cloud applications locally you can use the [Vagrant instructions](VAGRANT.md)

## SURF Reseach cloud catalog item registration

To register the eWaterCycle platform on the SURF Research cloud, follow instructions in [SURF Research cloud developer document](SRC-DEVEL.md).

## SURF Research cloud workspace 

This chapter is dedicated for application deployers. A workspace is name for a Virtual Machine (VM) on the SURF Research cloud. The workspace is created with the eWaterCycle application from the catalog.

### Shared data source

The [eWatercycle system setup](https://ewatercycle.readthedocs.io/en/latest/system_setup.html) requires a lot of data files.

Two eWaterCycle catalog items have been created:
1. eWaterCycle dcache, uses dcache as shared data source. High capacity, but high latency storage accessible via WebDAV from anywhere on the Internet. Usefull for research.
2. eWaterCycle samba, uses samba as shared data source. A low capacity, low latency file server that is only accessible from the private network of the SURF Research cloud. Usefull for teaching.

The shared data is mounted read-only `/data/shared` on the workspaces.
In the following chapters you will need to make choose which catalog item you want to use.
Depending on the choice, you need to do certain things.

### Preparations

Before you can create a workspace several steps need to be done first.

1. Log into [SURF Research Cloud](https://portal.live.surfresearchcloud.nl/)
2. Make sure you are [allowed to use eWaterCycle catalog item](https://servicedesk.surf.nl/wiki/display/WIKI/Sharing+components+and+catalog+items)
3. Create new storage item for home directories
   - To store user files
   - Use 50Gb size for simple experiments or bigger when required for experiment.
   - As each storage item can only be used by a single workspace, give it a name and description so you know which workspace and storage items go together.
4. If shared data source is dcache then create new storage item for dcache cache
   - To store cached files from dCache by rclone
   - Use 50GB size as size
   - As each storage item can only be used by a single workspace, give it a name and description so you know which workspace and storage items go together.
5. If shared data source is samba then create new storage item for data
   - To store training material like parameter sets, ready-to-use forcings, raw forcings and apptainer sif files for models.
   - This storage item should be used later in the Samba file server.
6. If shared data source is samba then create a private network
    - Name: `file-storage-network`
7. On https://portal.live.surfresearchcloud.nl/profile page in Collaborative organizations 
   - Create a secret named `samba_password` and a strong random password as value
   - Create a secret named `dcache_ro_token` and a dcache read-only token as value

To become root on a VM the user needs to be member of the `src_co_admin` group on [SRAM](https://sram.surf.nl/).
See [docs](https://servicedesk.surf.nl/wiki/display/WIKI/Workspace+roles%3A+Appoint+a+CO-member+a+SRC+administrator).

### File Server

If you want to create a eWaterCycle machine (aka workspace) that uses a Samba file server (aka shared data source is samba), you need to create a Samba file server first.

Each collaborative organization should run a single file server. This file server will be used to store read-only shared data. The file server should be created with the following steps:

1. Create a new workspace
2. Select `Samba Server` application
3. Select size with 2 cores and 16 GB RAM
4. Select data storage item, created in previous section
5. Select private network
6. Wait for machine to be running
7. Login to machine with ssh
   1. Become root with `sudo -i`
   2. Edit /etc/samba/smb.conf and in `[samba-share]` section replace `read only = no` with `read only = yes`
   3. Restart samba server with `systemctl restart smbd`
8. Populate `/data/volume_2/samba-share/` directory with training material. This directory will be shared with other machines.

See [data documentation](DATA.md#populating-samba-file-server) on how to populate the file server.

### Workspace creation with dcache as shared data source

Steps to create a eWaterCycle workspace:

1. Create a new workspace
2. Select collaborative organisation (CO) for example `ewatercycle-nlesc`
3. Select `eWaterCycle dcache` catalog item
4. Select size of VM (cpus/memory) based on use case
5. Select storage item for home directories. Remember item you picked as you will need it in the workspace parameters.
6. Select storage item for dcache cache. Remember item you picked as you will need it in the workspace parameters. 
7. Fill **all** the workspace parameters. They should look something like
   ![workspace-parameters](workspace-parameters.png)
   If you are not interested in grading then the following parameters can be left unchanged: 'Course repository', 'Course version', 'Grader user' and 'Students'.
8. Wait for machine to be running
9. Visit URL/IP
10. When done delete machine

End user should be invited to Collaborative organization in [SRAM](https://sram.surf.nl/) or [created as students](#students) so they can login.

See [User guide](USER.md) to see what users have to do to login or use GitHub repository.

### Workspace creation with samba as shared data source

Steps to create a eWaterCycle workspace:

1. Create a new workspace
2. Select collaborative organisation (CO) for example `ewatercycle-nlesc`
3. Select `eWaterCycle samba` catalog item
4. Select size of VM (cpus/memory) based on use case
5. Select home storage item. Remember items you picked as you will need them in the workspace parameters.
6. Select the private network
7. Fill **all** the workspace parameters. They should look something like
   ![workspace-parameters](workspace-parameters.png) 
   If you are not interested in grading then the following parameters can be left unchanged: 'Course repository', 'Course version', 'Grader user' and 'Students'.
8. Wait for machine to be running
9. Visit URL/IP
10. When done delete machine

End user should be invited to Collaborative organization in [SRAM](https://sram.surf.nl/) or [created as students](#students) so they can login.

See [User guide](USER.md) to see what users have to do to login or use GitHub repository.

### Students

During creation you can set the `students` parameter to create local posix accounts for students.
The format of the parameter value is `<username1>:<password1>,<username2>:<password2>`.
Use emtpy string for no students.
Make sure to use strong passwords as anyone on the internet can access the machine.

You can use the python script [create_student_passwords.py](create_student_passwords.py) to generate passwords. To use it, create a file "usernames.txt" with one username on each line. Then call the script to generate passwords. They will be stored in a new file called `students.txt`. See docs in script for more details. The passwords generated by the script should be distributed to the students.

### Example notebooks

To get example notebooks end users should goto to the machines homepage and click one of the notebook links.

These links use [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/) to sync a git repo and open a notebook in it.

## Docker images

In the eWaterCycle project we make Docker images. The images are hosted on [Docker Hub](https://hub.docker.com/u/ewatercycle) and [GitHub Container Registry](https://github.com/orgs/eWaterCycle/packages). A project member can create issues here for permisison to push images to Docker Hub or GitHub Container Registry.

## AI Disclaimer

The documentation/software code in this repository has been generated and/or refined using
GitHub CoPilot. All AI-output has been verified for correctness,
accuracy and completeness, adapted where needed, and approved by the author.
