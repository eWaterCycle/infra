Role Name
=========

Role to install conda

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

```yaml
# Checksum of conda tarball, prevents re-download
conda_tarball_checksum: sha256:bb2e3cedd2e78a8bb6872ab3ab5b1266a90f8c7004a22d8dc2ea5effeb6a439a.
# Location where conda tarball is downloaded to
conda_tarball_root: /mnt/apps
# Location where conda will be installed
conda_root: /mnt/apps/conda
```

Dependencies
------------

Requires Jupyter to be installed when `conda_jupyter_kernel` variable is True.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache v2

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
