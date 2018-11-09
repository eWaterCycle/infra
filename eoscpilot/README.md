# Cylc + Notebook server

The playbook in this directory creates two servers. One with a notebook server and the ewatercylce forecast website
The other is a cylc server to run long running cylc tasks on.

Create two VMs on https://ui.hpccloud.surfsara.nl using the ewatercycle2 group.

Notebookserver VM has
* ncWMS docker container running forecast frontend
* JupyterHub with OS accounts, see https://github.com/eWaterCycle/experiment-launcher/blob/master/README.md#jupyterhub-server on port 443
* Onedata mount
* Use Let's encrypt cert for all servers to run them encrypted

Cylc server VM has
* Cylc installed
* Cylc Web interface
* Forecast-docker installed
* Onedata mount
* Uses Let's encrypt cert for all servers to run them encrypted

# Create VMs

1. Create `eoscpilot` template from App called `Ubuntu-18.04.1-Server (...)`
    1. Select the ssd datastore for the image
2. Update `eoscpilot` template
    1. Set to 8Gb RAM and 2 cpus/vcpus
    2. Add Volatile disk of 1000Gb, type=FS and format=raw
5. Instantiate once as `eoscpilot`, so hostname is eoscpilot.ewatercycle2-nlesc.surf-hosted.nl
5. Instantiate once as `eoscpilot-cylc`, so hostname is eoscpilot-cylc.ewatercycle2-nlesc.surf-hosted.nl

For hostname see log tab of the Virtual machine.

# Setup VMs

Create a `inventory.yml` file based on `inventory.yml.example`.
Create a `vars.yml` file based on `vars.yml.example`.

Install stuff on VMs with

```bash
ansible-playbook -i inventory.yml playbook.yml
```

After installation a `eoscpilot.ewatercycle2-nlesc.surf-hosted.nl/letsencrypt/` and `eoscpilot-cylc.ewatercycle2-nlesc.surf-hosted.nl/letsencrypt/` directories have been copied to local machine with the Let's encrypt configuration and http certificate of the forecast/hub and cylc servers.

# Next steps

First register and run the cylc suite use the following commands:

```bash
# login to the cylc server
ssh ubuntu@eoscpilot-cylc.ewatercycle2-nlesc.surf-hosted.nl

# Become the cylc user
sudo su cylc

# Register the forecast suite
cylc register ewatercycle_forecast /mnt/home/cylc/forecast-docker

# Run the suite
cylc run ewatercycle_forecast
```

You can visit the Cylc web ui at https://eoscpilot-cylc.ewatercycle2-nlesc.surf-hosted.nl
Login for the web ui can be found in `vars.yml`.

The notebook server has:
* JupyterHub at https://eoscpilot.ewatercycle2-nlesc.surf-hosted.nl:8886
* eWatercylce Forecast at https://eoscpilot.ewatercycle2-nlesc.surf-hosted.nl

Login for the JupyterHub can be found in `vars.yml` file.
