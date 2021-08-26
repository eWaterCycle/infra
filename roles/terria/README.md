Role Name
=========

Ansible role for [terria](https://terria.io) web application for eWaterCycle project.

Uses forks (https://github.com/eWaterCycle/TerriaMap + https://github.com/eWaterCycle/terriajs) of terria repos as the web application.

Requirements
------------

Will install in the `/mnt/apps` directory.

Role Variables
--------------

```yaml
# Version of https://github.com/eWaterCycle/TerriaMap to use
terriamap_version: 92bb1c1b45607d5fe40127b8da38d5dd3b1e4e8b
# Version of https://github.com/eWaterCycle/terriajs to use
terriajs_version: c6e3cc1df26fbebafa1950b588628a85c4318a18
# Location of experiment launcher web service. Launcher is called when start experiment button is pressed
launcher_url: /launcher
# Location of JupyterHub, sets link of JH button in upper right corner of explorer
jupyterhub_url: https://jupyter.ewatercycle.org
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

Apache-2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
