## Catalog item registration

This chapter is dedicated for catalog item developers.

On the Research cloud the [developer](https://servicedesk.surf.nl/wiki/display/WIKI/Appoint+a+CO-member+a+developer) can add an catalog item for other people to use.
The generic steps to do this are documented [here](https://servicedesk.surf.nl/wiki/display/WIKI/Create+your+own+catalog+items).

For eWatercycle component following specialization was done

- Use Ansible playbook as component script type
  - Use `https://github.com/eWaterCycle/infra.git` as repository URL
  - Use `research-cloud-plugin.yml` as script path
  - Use `dcache-or-samba` as tag
  - Name: eWaterCycle
  - Subtitle: eWaterCycle teaching platform in a box
  - Description: welcome page + jupyter + nbgrader + eWaterCycle python packages + dcache or samba
  - Select cloud providers:
    - SURF HPC Cloud, with all non-gpu sizes selected
    - SURF HPC Cloud cluster, with all non-gpu sizes selected
- Component parameters, all fixed source type, required and overwitable unless otherwise stated
  - shared_data_source: parameter for shared data source. 
    -  default: dcache
    -  description: Source of shared data. Set to `dcache` or `samba`. TODO list which parameter are required for each source.
  - dcache_ro_token: parameter for dcache read-only token aka macaroon.
      The token can be found in the eWaterCycle password manager.
      This token has an expiration date, so it needs to be updated every now and then.
    - description: Macaroon with read permission for dcache
  - alt_home_location:
    - default: /data/volume_2
    - description: Path where home directories are stored. Set to `/data/<storage item name for homes>`.
  - rclone_cache_dir:
    - default: /data/volume_3
    - description: Path where rclone cache is stored. Set to `/data/<storage item name for rclone cache>`.
  - rclone_max_gsize:
    - default: 45
    - description: For maximum size of cache on `rclone_cache_dir` volume. In Gb.
  - grader_user:
    - description: User who will be grading. User should be created on sram. This user will also be responsible for setting up the course and assignments.
    - default: ==USERNAME==
      (==USERNAME== which will be replaced by the actual username of the user creating the workspace)   
  - students:
    - default: []
    - description: List of student user name and passwords. Format '<username1>:<password1>,<username2>:<password2>'. Use '' for no students. Use strong passwords as anyone on the internet can access the machine.
  - course_repo:
    - default: https://github.com/eWaterCycle/teaching.git
    - description: Git repository url with the course source material.
  - course_version
    - description: The version, branch or tag of the course repository to use.
    - default: nbgrader-quickstart
  - samba_password:
    - source_type: Co-Secret
    - value: {"key": "samba_password","sensitive": 1}
- Set documentation URL to `https://github.com/eWaterCycle/infra`
- Do not allow every org to use this component.
- Select the organizations (CO) that are allowed to use the component. Data on the dcache should not be made public.

For eWatercycle catalog item following specialization was done

- Select the following components:
  1. SRC-OS
  2. SRC-CO
  3. SRC-Nginx
  4. SRC-External plugin
  5. eWaterCycle
- Set documentation URL to `https://github.com/eWaterCycle/infra`
- Select the organizations (CO) that are allowed to use the catalog item.
- In cloud provider and settings step:
  - Add `SURF HPC Cloud` as cloud provider
    - Set Operating Systems to Ubuntu 22.04
    - Set Sizes to all non-gpu and non-disabled sizes
- In parameter settings step keep all values as is except
  - Set `co_irods` to `false` as we do not use irods
  - Set `co_research_drive` to `false` as we do not use research drive
  - As interactive parameters expose following:
   - shared_data_source:
      - label: Shared data source
      - description: Source of shared data. Set to `dcache` or `samba`. When samba is picked then you need to have a Samba server running inside the organization and filling rclone_cache_dir parameter is not needed.
    - rclone_cache_dir:
      - label: Rclone cache directory
      - description: Path where rclone cache is stored. Set to `/data/<storage item name for rclone cache>`.
    - alt_home_location:
      - label: Homes path
      - description: Path where home directories are stored. Set to `/data/<storage item name for homes>`.
    - grader_user:
      - label: Username of grader
      - description: User who will be grading. User should be created on sram.
      - default: empty string
    - students
      - label: Students
      - description: List of student user name and passwords. Format '<username1>:<password1>,<username2>:<password2>'. Use '' for no students. Use secure passwords as anyone on the internet can access the machine.
- Set boot disk size to 150Gb,
  as default size will be mostly used by the conda environment and will trigger out of space warnings.
- Set workspace acces button behavior to `Webinterface (https:)`,
  so clicking on `ACCESS` button will open up the eWatercycle experiment explorer web interface
