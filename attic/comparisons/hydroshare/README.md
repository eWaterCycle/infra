Local installation of Hydroshare

1. https://github.com/hydroshare/hydroshare/wiki/getting_started
2. https://github.com/hydroshare/hydroshare/tree/develop/irods

* Without irods works
* With irods fails to start of 
  * develop branch
  * 1.15.4 tag + persist

# Test

1. Uploaded netcdf file, edit it and publish
2. Cleanup uploaded file from test irods server using 
https://github.com/hydroshare/hydroshare/blob/develop/hydroshare/local_settings.py#L110-L121 config and `irods/icommands` docker container.
