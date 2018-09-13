# Setup of eWatercycle system

* Runs on the [SURFSara HPC cloud](https://userinfo.surfsara.nl/systems/hpc-cloud)
* Provisioned by [Ansible](https://docs.ansible.com/ansible/latest/index.html)

# Prerequisites

Install Ansible

```bash
pipenv --three install
pipenv shell
```

On the https://ui.hpccloud.surfsara.nl add your public SSH key so you can login the Virtual Machines.

# Servers

Each server has its own directory.
