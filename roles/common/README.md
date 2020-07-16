Role Name
=========

Common tasks for the eWaterCycle lab infrastructure.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Injection public ssh keys into `~ubuntu/.ssh/authorized_keys` file can be done with the `authorized_kets` variable.
In following format:
```yaml
authorized_keys:
 - <REPLACE ME public ssh key that will be added to servers authorized_keys>
```

Format and mounting of extra disks can be done with the `extra_disks` variable. For example:
```yaml
extra_disks:
  - device: vdb
    mount: /mnt
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache v2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
