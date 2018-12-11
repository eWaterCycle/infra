Researchdrive
=========

Creates directories for researchdrive and install rclone to synchronize

Requirements
------------

None

Role Variables
--------------

```yaml
researchdrive:
  user: 'username'
  password: 'password'
```

Dependencies
------------

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      - name: Researchdrive
          include_role:
            name: researchdrive
          vars:
            username: 'myuser'
            password: 'mypassword'

License
-------

Apache2

Author Information
------------------

Berend Weel

b.weel@esciencecenter.nl

www.ewatercycle.org
