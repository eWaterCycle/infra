Role Name
=========

Ansible role to install [eWaterCycle experiment launcher](https://github.com/eWaterCycle/experiment-launcher).

Requirements
------------

Role Variables
--------------

Optional variables

```yaml
# URL of JupyterHub server
jupyterhub_url: /jupyter
# version|commit of https://github.com/eWaterCycle/experiment-launcher
launcher_version: '71eccf537f1e32bf0569b975fdf2e7a8a46a0a94'
# Under which uri path the launcher is running
launcher_base_path: /
```

Dependencies
------------

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
