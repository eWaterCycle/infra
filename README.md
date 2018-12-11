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

# Authorized keys

To allow multiple users to ssh into servers the Ansible playbooks will inject the public keys listed in `authorized_keys.yml` file into `~/authorized_keys`.
The `authorized_keys.yml` file is in the following format:
```yaml
authorized_keys:
- <ssh public key 1>
- <ssh public key 2>
```
