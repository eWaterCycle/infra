Role Name
=========

Installs the web frontend of cylc as a service with nginx in front for security

Requirements
------------

- none

Role Variables
--------------

- cylc_web_users:
    name: username
    password: password

- cylc_review_port: 8080

Dependencies
------------

- Cylc

Example Playbook
----------------

    - hosts: servers
      tasks:
        - name: Cylc Web
          include_role:
            name: cylc-web
          vars:
            cylc_web_users:
              - name: admin
                password: myverysecurepassworddonotusethisonethough
            cylc_review_port: 8080

License
-------

Apache2

Author Information
------------------

Berend Weel

b.weel@esciencecenter.nl

www.ewatercycle.org
