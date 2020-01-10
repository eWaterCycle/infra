Role Name
=========

Ansible role to install [ESMValtool](https://github.com/ESMValGroup/ESMValTool).

Installation of ESMValTool, downloads CMORIZED data files from cartesius.surfsara.nl and downloads Lorentz data files.

Requirements
------------

Requires a conda environment.

Role Variables
--------------

```yml
---
# Location of esmvaltool repo
esmvaltool_app: /mnt/apps/ESMValTool
# Version of esmvaltool
esmvaltool_version: 0084e806287417604ef84bfa5ab86063d5d6da26
# Location of input data
esmvaltool_rootpath: /mnt/data/esmvaltool
# Branches that must be merged into default branch
esmvaltool_pullrequests: []
# Location where conda is installed
conda_root: /mnt/apps/conda
```

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: esmvaltool, x: 42 }

License
-------

Apache v2.

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
