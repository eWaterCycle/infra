Role Name
=========

Role to install conda

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

```yaml
# Location where conda tarball is downloaded to
conda_tarball_root: /opt
# Location where conda will be installed
conda_root: /opt/conda
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
