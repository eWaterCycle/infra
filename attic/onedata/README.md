Create a VM on https://ui.hpccloud.surfsara.nl

VM has
* OneData connection

# Create VM
1. Create `(nc)wms server for cesium` template from App called `Ubuntu-16.04.4-Server (2018-05-01)`
2. Set persistent=yes for it's image
3. Configure template with 8Gb and 2 cpus
4. Add 100GB disk for storage on ceph
5. Instantiate as `ncwms`, so hostname is ncwms.ewatercycle2-nlesc.surf-hosted.nl


# Setup VM

Check `inventory` file for correct hostname.

Use ansible

```bash
pip install ansible
ansible-playbook -i inventory playbook.yml
```

if ansible gives this error: 'ERROR! Unexpected Exception, this is probably a bug: 'module' object has no attribute 'SSL_ST_INIT''
do the following: 'sudo -H pip2 install -U pyOpenSSL'

# Next steps

* Runs at https://ncwms.ewatercycle2-nlesc.surf-hosted.nl
