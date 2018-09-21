Create a VM on https://ui.hpccloud.surfsara.nl using the ewatercycle2 group.

VM has
* JupyterHub with OS accounts, see https://github.com/eWaterCycle/experiment-launcher/blob/master/README.md#jupyterhub-server on port 443
* Launcher, https://github.com/eWaterCycle/experiment-launcher on port 8888
* TerriaMap, http://github.com/eWaterCycle/TerriaMap on port 3001
* ~~THREDDS server with some eWatercycle 1 forecast data on port 8080~~
* Use Let's encrypt cert for all servers to run them encrypted

# Create VM

1. Create `launcher-hub` template from App called `Ubuntu-18.04.1-Server (...)`
    1. Select the ssd datastore for the image
2. Update `launcher-hub` template
    1. Set to 8Gb RAM and 2 cpus/vcpus
    2. Add Volatile disk of 500Gb, type=FS and format=raw
5. Instantiate as `hub`, so hostname is hub.ewatercycle2-nlesc.surf-hosted.nl

For hostname see log tab of the Virtual machine.

# Setup VM

Create a `inventory` file based on `inventory.example`.
Create a `vars.yml` file based on `vars.yml.example`.

Install stuff on VM with

```bash
ansible-playbook -i inventory playbook.yml
```

After installation a `letsencrypt/` directory has been copied to local machine with the Let's encrypt configuration and http certificate of the hub server.

# Next steps

* JupyterHub at https://hub.ewatercycle2-nlesc.surf-hosted.nl
* Experiment launcher at https://hub.ewatercycle2-nlesc.surf-hosted.nl:8888/ui/
* TerriaMap at http://hub.ewatercycle2-nlesc.surf-hosted.nl:3001

Login for the JupyterHub can be found in `vars.yml` file.
