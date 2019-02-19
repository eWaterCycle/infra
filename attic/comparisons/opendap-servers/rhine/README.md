Data server for

* Rhine model and data
* eWaterCycle forecast

Features:

* sftp account for upload
* thredds server to host files
* esgf node if possible

# Create VM

1. Create `thredds` template from App called `Ubuntu-16.04.4-Server (2018-05-01)`
2. Set persistent=yes for it's image
3. Configure template with 8Gb and 2 cpus
4. Create a data image and attach to template
4. Instantiate as `data`, so hostname is data.ewatercycle2-nlesc.surf-hosted.nl