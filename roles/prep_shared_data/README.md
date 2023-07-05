Role Name
=========

Performs data preperations steps from [system setup](https://ewatercycle.readthedocs.io/en/latest/system_setup.html) so the data can be uploaded to dCache.

A virtual machine will mount dCache so data can be used in notebooks.

Requirements
------------

To download ERA5 data files an uid and api key from the [Climate Data Store](https://cds.climate.copernicus.eu) are needed.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Required variables:

```yaml
# Creds from https://cds.climate.copernicus.eu Climate Data Store to download ERA5 data
cds_uid: null # Must be filled from other place
cds_api_key: null # Must be filled from other place
```

Optional variables to select climate data

```yaml
# Start year for which climate data should be prepared
climate_begin_year: 1990
# End year for which climate data should be prepared
climate_end_year: 1990
era5_variables:
  - total_precipitation
  - mean_sea_level_pressure
  - 2m_temperature
  - minimum_2m_temperature_since_previous_post_processing
  - maximum_2m_temperature_since_previous_post_processing
  - 2m_dewpoint_temperature
  - 10m_u_component_of_wind
  - 10m_v_component_of_wind
  - surface_solar_radiation_downwards
  - toa_incident_solar_radiation
  - orography
```

Variables for hydrological models

```yaml
# Docker container images that will be downloaded and converted to Apptainer image files
grpc4bmi_images:
    # - docker: ewatercycle/walrus-grpc4bmi
    #   apptainer: ewatercycle-walrus-grpc4bmi.sif
    - docker: ewatercycle/pcrg-grpc4bmi:setters
      apptainer: ewatercycle-pcrg-grpc4bmi_setters.sif
    - docker: ewatercycle/wflow-grpc4bmi:2020.1.1
      apptainer: ewatercycle-wflow-grpc4bmi_2020.1.1.sif
    - docker:  ewatercycle/marrmot-grpc4bmi:2020.11
      apptainer: ewatercycle-marrmot-grpc4bmi_2020.11.sif
    # - docker: ewatercycle/hype-grpc4bmi
    #   apptainer: ewatercycle-hype-grpc4bmi.sif
    - docker: ewatercycle/lisflood-grpc4bmi:20.10
      apptainer: ewatercycle-lisflood-grpc4bmi_20.10.sif
```

Other optional variables

```yaml
# Where all data should be put
data_root: /mnt/data
# Directory where apptainer sif files can be stored and read by other
apptainer_image_root: '{{ data_root }}/singularity-images'
# Location where conda is installed
conda_root: /opt/conda
# Name of conda environment to use
conda_environment: ewatercycle
# Path to conda environments bin directory
conda_environment_bin: '{{ conda_root}}/envs/{{ conda_environment }}/bin'
# Location where climate data should be placed
climate_data_root_dir: '{{ data_root }}/climate-data'
# Location where esmvaltool aux data should be placed
auxiliary_data_dir: '{{ climate_data_root_dir }}/aux'
# Version of https://github.com/eWaterCycle/recipes_auxiliary_datasets to checkout to {{ auxiliary_data_dir }}
esmvaltool_aux_version: dde5fcc78398ff3208589150b52bf9dd0b3bfb30
# Location where eWatercycle example parameter sets will be downloaded to
parameter_set_root_dir: '{{ data_root }}/parameter-sets'
# Location where eWatercycle example forcings will be downloaded to
example_forcing_root_dir: '{{ data_root }}/forcing'
```

Dependencies
------------

Requires installation of eWaterCycle python package, ESMValTool, era5cli. Those can be installed by running the [../ewatercycle](../ewatercycle) role.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache-2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
