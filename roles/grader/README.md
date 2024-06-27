Role Name
=========

Setup [nbgrader](https://nbgrader.readthedocs.io/).

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Required vars:

```yaml
grader_user: vagrant
```

Optional vars:

```yaml
students: [["<username1>","<password1>"]]
```

Dependencies
------------

Requires `jupyter` role to be run first.

License
-------

Apache-2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
