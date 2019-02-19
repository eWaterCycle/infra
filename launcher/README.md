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
    2. Add Volatile disk of 500Gb, type=FS and format=raw, for storage of apps, docker and homedirs
5. Instantiate as `hub`, so hostname is hub.ewatercycle2-nlesc.surf-hosted.nl
    1. Resize DISK 0 to 80Gb, to prevent root disk from getting full

For hostname see log tab of the Virtual machine.

# Setup VM

Create a `inventory` file based on `inventory.example`.
Create a `vars.yml` file based on `vars.yml.example`.
Check that your public ssh key is in `../authorized.keys.yml`.

Install stuff on VM with

```bash
ansible-playbook -i inventory playbook.yml
```

After installation a `<domain>/letsencrypt/` directory has been copied to local machine with the Let's encrypt configuration and http certificate of the hub server.

## Generate users

The `vars.yml.example` has 2 users to generate a list of users run `generate_users.py`.
The script will output a `users.yml` file which can be appended to the `posix_users` list.
The script will also output a `users.md` Markdown file which contains the username password combinations.

# Next steps

* JupyterHub at https://hub.ewatercycle2-nlesc.surf-hosted.nl
* Experiment launcher at https://hub.ewatercycle2-nlesc.surf-hosted.nl:8888/ui/
* TerriaMap at http://hub.ewatercycle2-nlesc.surf-hosted.nl:3001

Login for the JupyterHub can be found in `vars.yml` file.
