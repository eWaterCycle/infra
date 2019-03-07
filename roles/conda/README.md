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
conda_tarball_checksum: sha256:e5e5b4cd2a918e0e96b395534222773f7241dc59d776db1b9f7fedfcb489157a
# Location where conda tarball is downloaded to
conda_tarball_root: /mnt/apps
# Location where conda will be installed
conda_root: /mnt/apps/conda
# Whether to register the default conda environment as a kernel in jupyter
conda_jupyter_kernel: true
# Location where Jupyter is installed
conda_jupyter_prefix: /usr/local
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