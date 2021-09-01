Role Name
=========

Jupyter enviroment as used in eWaterCycle project.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Required vars:

```yaml
cull:
  # Servers and notebooks that have been idle for longer then timeout (in seconds) will be culled.
  timeout: '86400' # 1 day
  # The maximum age (in seconds) of servers that should be culled even if they are active.
  max_age: '604800' # 7 days
jupyterhub_spawner_environment:
  # Cache dir for ewatercycle.observation.usgs.get_usgs_data()
  USGS_DATA_HOME: /tmp
  # TODO needed for pymt(?) and cfunits
  UDUNITS2_XML_PATH: /usr/share/xml/udunits/udunits2.xml
# Location where conda is installed
conda_root: /opt/conda
# Name of conda environment to use
conda_environment: ewatercycle
# Path to conda environments bin directory
conda_environment_bin: '{{ conda_root}}/envs/{{ conda_environment }}/bin'
# List of posix users who should have JupyterHub admin rights
jupyterhub_admins: []
```

Dependencies
------------

The Jupyter Hub requires

* eWaterCycle Conda environment which can be installed using [ewatercycle role](../ewatercycle).

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache2

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
