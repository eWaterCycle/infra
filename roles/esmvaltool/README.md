Role Name
=========

Installation of ESMValTool and downloads CMORIZED data files from research drive.

Requirements
------------

Requires a conda environment.

Role Variables
--------------

```yml
---
esmvaltool_rootpath: /mnt/data/esmvaltool
esmvaltool_researchdrive_rootarchive: <filename of archive on research drive >
```

Dependencies
------------

Requires rclone and rclone research drive config to be available which is what the researchdrive role does.

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
