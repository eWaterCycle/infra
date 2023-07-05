Role Name
=========

Role for eWatercycle platform

Creates conda environment with

- the eWaterCycle Python package dependencies
- era5cli to download ERA5 climate data
- PyMT models
- JupyterHub and Jupyter extensions and their deps
- ansible as this env will be the default python for all users including the ubuntu used for running ansible.

For the SRC application this is the only conda environment and single Jupyter kernel that can be picked. So if any extra ordifferent Python and/or Conda packages are required then `files/environment.yml` should be edited.

Role also adds /etc/ewatercycle.yaml and ~/.esmvaltool/config-user.yml config files.

Requirements
------------

This role expects `data_root` to be filled with files prepared by [../../shared-data-disk.yml](../../shared-data-disk.yml) playbook.

Role Variables
--------------

Required vars:

```yaml
---
# Location where conda is installed
conda_root: /opt/conda
# Name of conda environment to use
conda_environment: ewatercycle
# Path to conda environments bin directory
conda_environment_bin: '{{ conda_root}}/envs/{{ conda_environment }}/bin'
# Where all shared data is available
data_root: /mnt/data
# Location of climate data
climate_data_root_dir: '{{ data_root }}/climate-data'
# Location where GRDC data should be downloaded
grdc_location: '{{ data_root }}/observation/grdc/dailies'
# Location where example parameter sets should be downloaded and where any other read-only pararmeter set can be put
parameterset_dir: '{{ data_root }}/parameter-sets'
# Location where Apptainer image files (*sif) of hydrological models should be stored
apptainer_image_root: '{{ data_root }}/singularity-images'
# Location where all home-directories are located
home_root: /home
```

Dependencies
------------

Conda should be installed in `conda_root` directory. Use [../conda](../conda) role to install conda.

Requires apptainer executable which can be installed with [../apptainer](../apptainer) role.

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
