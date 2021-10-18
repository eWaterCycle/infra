Role Name
=========

Role to install [singularity](https://www.sylabs.io/singularity/) v3.
Tested on Ubuntu 18.04.

Requirements
------------

none

Role Variables
--------------

```yaml
# Version of singularity release at https://github.com/hpcng/singularity
singularity_version: '3.8.3'
# Version of go release at https://golang.org/dl/
go_version: '1.17.1'
# SHA256 Checksum of linux-amd64 os-arch version of go at https://golang.org/dl/
go_sha256sum: 'dab7d9c34361dc21ec237d584590d72500652e7c909bf082758fb63064fca0ef'
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      tasks:
          include_role:
            name: singularity

License
-------

Apache 2.0
