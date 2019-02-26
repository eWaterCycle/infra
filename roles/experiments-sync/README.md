Role Name
=========

Setup cron jobs to copy forecast data to researchdrive.

Requirements
------------

Nope.

Role Variables
--------------

```yaml
---
# Mail adress where cron job results are sent to  
cron_mailto: ewatercycle-infra@esciencecenter.nl
researchdrive:
  # Rclone alias+path of remote location to sync to
  remote_dir: RD:/eWaterCycle/forecasts
  # Directory that must be synced to researchdrive
  local_dir: /mnt/researchdrive/forecasts
```

Dependencies
------------

Depends on researchdrive role.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: experiments-sync, x: 42 }

License
-------

Apache v2

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
