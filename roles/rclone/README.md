Role Name
=========

Role to install rclone, upload files to dCache and mount dCache.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Required for uploading

```yaml
# dCache token for mounting shared data
# Must be filled from external place like var config file or SRC
dcache_rw_token: null
```

Required for mounting

```yaml
# dCache token for mounting shared data
# Must be filled from external place like var config file or SRC
dcache_ro_token: null
```

Optional for mounting

```yaml
# Location where rlcone stores it cached files
# if a storage item is attached for cache then change this var
rclone_cache_dir: /tmp/rclone
# Maximum size of rclone cache in Gigabytes
rclone_max_gsize: 500
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

Apache-2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
