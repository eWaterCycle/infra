# Shared data
- [Shared data](#shared-data)
  - [Configured paths](#configured-paths)
  - [Populating Samba file server](#populating-samba-file-server)
  - [Populating dcache](#populating-dcache)
  - [Sync dcache with existing folder elsewhere](#sync-dcache-with-existing-folder-elsewhere)
  - [Mount dcache on local machine](#mount-dcache-on-local-machine)

This document is dedicated for application data preparer.

## Configured paths

The eWatercycle Python package (`/etc/ewatercycle.yaml`) and ESMValTool (`~/.esmvaltool/config-user.yml`) have been configured to use the following paths:

- Root is `/data/shared`
  - Climate data is in `/data/shared/climate-data`, used to generated forcings.
    - ESMValTool auxiliary data is in `/data/shared/climate-data/aux`
    - OBS6 data is in `/data/shared/climate-data/obs6`
  - Parameter sets are in `/data/shared/parameter-sets`, used to run models.
  - Apptainer images are in `/data/shared/singularity-images`, used to run containerized models.
  - GRDC observations are in `/data/shared/observation/grdc/dailies`, used `ewatercycle.observation.grdc.get_grdc_data()` function.

## Populating Samba file server

Populating the `/data/volume_2/samba-share/` directory on the Samba file server can be done with a Ansible playbook using the following commands.
<!-- 
this could be run during workspace creation, but downloads are very flaky and time consuming, also this would require maintaining another SRC compoent+catalog item so done manually after workspace is up. -->

```shell
sudo -i
git clone -b dcache-or-samba https://github.com/eWaterCycle/infra.git /opt/infra
cd /opt/infra
ansible-galaxy role install mambaorg.micromamba
# Get cds user id (uid) and api key from cds profile page
ansible-playbook populate-samba.yml -e cds_uid=... -e cds_api_key=...
# If you do not want to download ERA5 data then leave out cds_uid and cds_api_key arguments.
```

This will:
0. Harden the share, so only root can write in /data/volume_2/samba-share/ and its readonly
1. Download Apptainer images for models
3. Setup era5cli to download era5 data
5. Download raw era5 data with era5cli
6. Aggregate, cmorize and compress era5 data with custom esmvaltool script
7. Setup rclone for copying data from dcache to file server
8. Create a ewatercycle.yaml which can be used on the Jupyter machines.
   1. Create empty directory `/data/shared/observation/grdc/dailies` where GRDC data can be stored.
9.  Create a esmvaltool config file which can be used on the Jupyter machines.

If you have data elsewhere you can sync the data with this file server with

```shell
rsync -av --progress <remote user>@<remote host>/<remote location> /data/volume_2/samba-share/
```

## Populating dcache

This chapter is dedicated for application data preparer.

First gather all your data togethe on a server (like snellius or spider). 
You can use parts of the [populate-samba.yml](populate-samba.yml) playbook to download data.

Populating the dcache can be done from a server (like snellius or spider)
with the following command

```shell
# cd to directory with data
# have a rclone config with dcache macaroon
rclone copy . dcache:ewatercycle
```

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

## Mount dcache on local machine

Create the file `~/.config/rclone/rclone.conf` and add the following content:

```ini
[dcache]
type = webdav
url = https://webdav.grid.surfsara.nl:2880
vendor = other
user =
pass =
bearer_token = <dcache macaroon with read permissions>
```

Install [rclone](https://rclone.org/) and run following command to mount dcache at `~/dcache` directory.

```shell
mkdir ~/dcache
rclone mount --read-only --cache-dir /tmp/rclone-cache --vfs-cache-max-size 30G --vfs-cache-mode full dcache:/ ~/dcache
```

In ESMValTool config files you can use `~/dcache/climate-data/obs6` for `rootpath:OBS6`.