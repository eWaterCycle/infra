# SURF Research cloud developer

This chapter is dedicated for catalog item and component developers.

- [SURF Research cloud developer](#surf-research-cloud-developer)
  - [Component registration](#component-registration)
  - [Catalog item registration](#catalog-item-registration)

A new workspace (aka Virtual Machine) can be made by choosing a catalog item.
A catalog item consists out of a list of components and other configuration.

To register new catalog items in SURF Research cloud you 
need to [appoint a developer](https://servicedesk.surf.nl/wiki/display/WIKI/Appoint+a+CO-member+a+developer).

The generic steps to make your own catalog item are documented [here](https://servicedesk.surf.nl/wiki/display/WIKI/Create+your+own+catalog+items).

## Component registration

On [Components page](https://portal.live.surfresearchcloud.nl/catalog/components)
create a eWatercycle component with following specialization:

- Component script
  - Component script type: Ansible playbook
  - Repository URL: https://github.com/eWaterCycle/infra.git
  - Path: research-cloud-plugin.yml
  - Tag: dcache-or-samba
- Name & description
  - Name: eWaterCycle dache or samba
  - Subtitle: eWaterCycle teaching platform in a box
  - Description: Welcome page + JupyterHub + nbgitpuller + nbgrader + eWaterCycle Python packages + dcache or samba
  - Logo: Organization avatar/logo from https://github.com/eWaterCycle/ewatercycle
- Parameters, all configured parameters should be source type is fixed, required and overwitable unless otherwise stated
  - shared_data_source:
    - description: Source of shared data. Set to `dcache` or `samba`.
    - initial value: dcache
  - samba_password:
    - source_type: Co-Secret
    - overwritable: false
    - initial value: {"key": "samba_password"}
  - dcache_ro_token: parameter for dcache read-only token aka macaroon.
      The token can be found in the eWaterCycle password manager.
      This token has an expiration date, so it needs to be updated every now and then.
    - source_type: Co-Secret
    - description: Macaroon with read permission for dcache.
    - initial value: {"key": "dcache_ro_token"}
    - overwritable: false
  - rclone_cache_dir:
    - description: Path where rclone cache is stored. Set to `/data/<storage item name for rclone cache>`.
    - initial value: /data/volume_3
  - alt_home_location:
    - description: Path where home directories are stored. Set to `/data/<storage item name for homes>`.
    - initial value: /data/volume_2
  - grader_user:
    - description: User who will be grading. User should be created on sram. This user will also be responsible for setting up the course and assignments.
    - initial value: ==USERNAME==
      (==USERNAME== which will be replaced by the actual username of the user creating the workspace)   
  - students:
    - description: List of student user name and passwords. Format '<username1>:<password1>,<username2>:<password2>'. Use empty string for no students. Use strong passwords as anyone on the internet can access the machine.
    - required: false
  - course_repo:
    - description: Git repository url with the course source material.
    - initial value: https://github.com/eWaterCycle/teaching.git
  - course_version
    - description: The version, branch or tag of the course repository to use.
    - initial value: nbgrader-quickstart
- Owner & support
  - Owner: ewatercycle-nlesc
  - Documentation URL: https://github.com/eWaterCycle/infra
- Access
  - Allow every org to use this component.

## Catalog item with dcache as shared data source

On [Catalog items page](https://portal.live.surfresearchcloud.nl/catalog/catalogItems)
create an eWatercycle catalog item with following specialization:

- Components, select the following components (use live version for all of them):
  1. SRC-OS
  2. SRC-CO
  3. SRC-Nginx
  4. SRC-External plugin
  5. eWaterCycle dache or samba
- Name & description
  - Name: eWaterCycle dcache
  - Subtitle: eWaterCycle teaching platform in a box
  - Description: Welcome page + JupyterHub + nbgitpuller + nbgrader + eWaterCycle Python packages + dcache as shared data source
  - Logo: Organization avatar/logo from https://github.com/eWaterCycle
- Owner & support
  - Owner: ewatercycle-nlesc
  - Documentation URL: https://github.com/eWaterCycle/infra
- Access, Select the organizations (CO) that are allowed to use the catalog item.
  - Allowed Collaborative Organisations: Select all organizations with eWaterCycle in the name
- Cloud settings
  - Add `SURF HPC Cloud` as cloud provider
    - Operating Systems: Ubuntu 22.04
    - Sizes: all non-gpu and non-disabled sizes
- Parameters, keep all values as is except
  - Set `co_irods` to `false` as we do not use irods
  - Set `co_research_drive` to `false` as we do not use research drive
  - Set `shared_data_source` to `dcache`
  - As interactive parameters expose following:
    - rclone_cache_dir:
      - label: Rclone cache directory
    - alt_home_location:
      - label: Homes path
    - grader_user:
      - label: Username of grader
    - students
      - label: Students
    - course_repo
      - label: Course repository
    - course_version
      - label: Course version
- Workspace settings
  - Set boot disk size to 50Gb,
  as default size will be mostly used by the conda environment and will trigger out of space warnings.
  - Set workspace acces button behavior to `Webinterface (https:)`,
  so clicking on `ACCESS` button will open up the eWatercycle experiment explorer web interface

## Catalog item with Samba as shared data source

On [Catalog items page](https://portal.live.surfresearchcloud.nl/catalog/catalogItems)
create an eWatercycle catalog item with following specialization:

1. Find `eWaterCycle dcache` component item
2. Click on Actions -> Clone
3. Then re-configure the following

- Name & description
  - Name: eWaterCycle samba
  - Description: Welcome page + JupyterHub + nbgitpuller + nbgrader + eWaterCycle Python packages + samba as shared data source
- Parameters
  - rclone_cache_dir:
    - action: keep value
  - shared_data_source:
    - initial value: samba
