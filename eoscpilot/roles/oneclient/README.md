Role Name
=========

Installs the onedata client as a systemd service with configuration

Requirements
------------
- none

Role Variables
--------------

| | |
|---------------|-----------------|
| oneclient_mount | |
| | The location of the mountpoint default: /mnt/oneclient |
| oneclient_gid | |
| | The groupid for the oneclient group |
| oneclient_uid |
| | The userid for the oneclient user |

Dependencies
------------
- none

Example Playbook
----------------
    - hosts: servers
      tasks:
      include_role:
         name: oneclient
      vars:
        oneclient_gid: 1042
        oneclient_uid: 1043
        oneclient_mount: /mnt/one/data

License
-------

Apache2

Author Information
------------------

Berend Weel

b.weel@esciencecenter.nl

www.ewatercycle.org
