Role Name
=========

Role for eWatercycle platform

Contains:

* ewatercycle conda environment
* JupyterHub installation with bunch of extensions
* task files to perform [system setup](https://ewatercycle.readthedocs.io/en/latest/system_setup.html) steps so the data can be uploaded to dCache.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Required vars:

```yaml
# Location where conda is installed
conda_root: /mnt/apps/conda
# Location of input data
esmvaltool_data: /mnt/data/esmvaltool
# Version of https://github.com/eWaterCycle/recipes_auxiliary_datasets to checkout to {{ esmvaltool_data }}/aux
esmvaltool_aux_version: dde5fcc78398ff3208589150b52bf9dd0b3bfb30
# Location where GRDC data should be downloaded
grdc_location: /mnt/data/observation/grdc/dailies
# Location where example parameter sets should be downloaded and where any other read-only pararmeter set can be put
parameterset_dir: /mnt/data/parameter-sets
# Location where Singularity image files (*sif) of hydrological models should be stored
singularity_dir: /mnt/data/singularity-images
# Location where all home-directories are located
home_root: /home
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache2

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
