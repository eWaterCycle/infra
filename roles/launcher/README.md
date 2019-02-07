Role Name
=========

Ansible role to install eWaterCycle experiment launcher.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Required vars:
```yaml
launcher_token: '297cee229574135ae2f6721d9b3f0b9dd138c831cc15084c01d68f145b70b5b2'
hub_domain: hub.ewatercycle2-nlesc.surf-hosted.nl
```

Dependencies
------------

The experiment launcher communicates with a Jupter Hub server, which is part of the `jupyter` role.

The experiment launcher requires https certificate pair, which is generated in `letsencrypt` role.

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
