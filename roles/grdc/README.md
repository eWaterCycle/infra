Role Name
=========

Global Runoff Data Centre, https://www.bafg.de/GRDC/EN/Home/homepage_node.html.
Downloads datasets from GRDC site.

Requirements
------------

None

Role Variables
--------------

```yml
---
# Directory to put grdc data
grdc_root_dir: /mnt/data/grdc
# Station catalogs of freely non-commercial available datasets
grdc_station_zips: 
  - ftp://ftp.bafg.de/pub/REFERATE/GRDC/catalogue/grdc_gcosgtnh_stations.zip
  - ftp://ftp.bafg.de/pub/REFERATE/GRDC/catalogue/grdc_arctichycos_stations.zip
# Archycos daily zip url
grds_archycos_day_zip: ftp://ftp.bafg.de/pub/REFERATE/GRDC/ARC_HYCOS/arc_hycos_day.zip
# Global Terrestrial Network for River Discharge (GTN-R) datasets
# https://www.bafg.de/GRDC/EN/04_spcldtbss/44_GTNR/GTN-R%20SOS2.html
grdc_gtnr:
  - id: 1
    name: WMO Region 1 (Africa)
    stations: ftp://ftp.bafg.de/pub/REFERATE/GRDC/website/GTNR_ONLINE_1.txt
    periods:
      - range: 1931_1960
        url: https://geoportal.bafg.de/grdc-gtnr?datasource=1&service=SOS&version=2.0&request=GetObservation&featureOfInterest=http://gemstat.bafg.de/stations/1104150,1104530,1159100,1159105,1160235,1160378,1160500,1160580,1160684,1160788,1160880,1255100,1257100,1259100,1445100,1732100,1733600&temporalFilter=phenomenonTime,1931-01-01T00:00:00.000Z/1960-12-31T00:00:00.000Z
      - range: 1961_1990
        url: https://geoportal.bafg.de/grdc-gtnr?datasource=1&service=SOS&version=2.0&request=GetObservation&featureOfInterest=http://gemstat.bafg.de/stations/1104150,1104530,1159100,1159105,1160235,1160378,1160500,1160580,1160684,1160788,1160880,1255100,1257100,1259100,1445100,1732100,1733600&temporalFilter=phenomenonTime,1961-01-01T00:00:00.000Z/1990-12-31T00:00:00.000Z
      - range: 1981_2010
        url: https://geoportal.bafg.de/grdc-gtnr?datasource=1&service=SOS&version=2.0&request=GetObservation&featureOfInterest=http://gemstat.bafg.de/stations/1104150,1104530,1159100,1159105,1160235,1160378,1160500,1160580,1160684,1160788,1160880,1255100,1257100,1259100,1445100,1732100,1733600&temporalFilter=phenomenonTime,1981-01-01T00:00:00.000Z/2010-12-31T00:00:00.000Z
```

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache v2.

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
