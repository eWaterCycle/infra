Role Name
=========

Ansible role for [terria](https://terria.io) web application for eWaterCycle project.

Requirements
------------

Will install in the `/mnt/apps` directory.

Role Variables
--------------

```yaml
terriamap_version: ewa_1.0
teriajs_version: ewa_1.0
```

Dependencies
------------

To launcher experiment the experiment launcher web service should be present. The experiment launcher is installed with the launcher role.

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
