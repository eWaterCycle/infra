Role Name
=========

Ansible role to install [HyMUSE](https://github.com/eWaterCycle/HyMUSE).

Requirements
------------

Installs amuse and HyMUSE in already existing /mnt/apps directory.

Role Variables
--------------

```yaml
---
amuse_version: muse
hymuse_version: HEAD
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: hymuse
      include_role:
        name: hymuse
```

License
-------

Apache2
