# Q for SRC support

I am writing my own plugin where I need to set the public URL in an application config file using an Ansible task.
In the logs of a workspace I see a `service_url` key with value `https://d08d27c8-d63d-492f-9479-70aa98b90f81.workspaces.live.surfresearchcloud.nl`.
When I try to use that var in my Ansible task, then it is not set.
Can this `service_url` var be supplied to where my plugin is being run?

I am writing my own plugin where I have 2 storage items (mainly because system disk is too small):
1. A read only disk with data
2. A scratch disk with intermediate results for all CO members
In a Ansible task how do I distinquish between them as they need to be mounted differently?
I looked at the resource_meta dict, but it only contains internal uuids, not the name I gave my storage items.

I am starting workspace with my own application+plugin. When things fail the logs show a long line with the output of my plugin.
However when my plugin completes succesfully I don't see any mention of my plugin tasks in the log.
I am printing some messages in the plugin about where parts of the application are running, but I can not see them in the logs.
Can the output of external plugins always be logged just like the internal plugins (RSC-OS, RSC-CO, RSC-Nginx)?
