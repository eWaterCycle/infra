Role Name
=========

Jupyter enviroment as used in eWaterCycle project.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Required vars:

```yaml
launcher_jupyterhub_token: '297cee229574135ae2f6721d9b3f0b9dd138c831cc15084c01d68f145b70b5b2'
jupyterhub_url: https://jupyter.ewatercycle.org
posix_users:
  - name: student1
    password: <generated using `mkpasswd --method=sha-512`>
  - name: admin
    password: <generated using `mkpasswd --method=sha-512`>
```

Dependencies
------------

The Jupyter Hub requires

* eWaterCycle Conda environment

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache2

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
