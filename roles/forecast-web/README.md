Role Name
=========

Installs the web frontend of the ewatercycle forecast as a service

Requirements
------------

- none

Role Variables
--------------

default parameters:
```
forecast_port: 8080
forecast_src_dir: /mnt/oneclient/eWaterCycle/forecast-results/forecasts
forecast_dest_dir: /mnt/apps/forecast
forecast_domain: localhost
forecast_public_domain: "http://{{ forecast_domain }}:{{ forecast_port }}"

forecast_admin:
  name: admin
  password: admin
```


Dependencies
------------
- docker should be installed

Example Playbook
----------------

    - hosts: forecast_server
      tasks:
        - name: Forecast Web
          include_role:
            name: forecast-web

License
-------

Apache2

Author Information
------------------

Berend Weel

b.weel@esciencecenter.nl

www.ewatercycle.org