Role Name
=========

Installs the cylc workflow engine with its own user and group

Requirements
------------

- Cylc runs using python 2 and is not compatible with python 3

Role Variables
--------------

- none

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