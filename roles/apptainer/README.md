Role Name
=========

Role to install [apptainer](https://apptainer.org).

Requirements
------------

none

Role Variables
--------------

```yaml
# Version of singularity release at https://github.com/apptainer/apptainer/releases
apptainer_version: '1.1.6'

```
Dependencies
------------
none

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: apptainer }

License
-------

Apache 2.0
