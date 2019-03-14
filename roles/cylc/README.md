Role Name
=========

Installs the cylc workflow engine with its own user and group

Requirements
------------

- Cylc runs using python 2 and is not compatible with python 3

Role Variables
--------------

Rhe default variables are:
```yaml
# Version of cylc to install
cylc_version: cylc-7.8.1
# Version of forecast docker to install
forecast_docker_verson: dda6d2d2170df223c3f8ee200970bb153ee60d3e
```

Dependencies
------------

- none

Example Playbook
----------------

    - hosts: servers
      tasks:
        - name: Cylc
          include_role:
          name: cylc

License
-------

Apache2

Author Information
------------------

Berend Weel

b.weel@esciencecenter.nl

www.ewatercycle.org