Role Name
=========

Role to install [singularity](https://www.sylabs.io/singularity/) v3.
Tested on Ubuntu 18.04.

Requirements
------------

none

Role Variables
--------------

| | |
|---------------|-----------------|
| singularity_version | Singularity version |
| singularity_sha256sum | sha256 checksum of Singularity release tarball |
| go_version | Go version |

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      tasks:
          include_role:
            name: singularity

License
-------

Apache 2.0
