Role Name
=========

NGINX Web server which acts as reverse proxy and encryption.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Location + proxy_pass pairs can be set using the `locations` variable. For example

```yaml
locations:
  - name: /launcher
    proxy_pass: http://localhost:8888/
  - name: /
    proxy_pass: http://localhost:3001/
# Stop nginx while certbot is renewing certs
pause_cert_renew: false
```

Make sure the most specific location is before the least specific location.

Dependencies
------------

Depends on letsencrypt role to provide https certificate pair.

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
