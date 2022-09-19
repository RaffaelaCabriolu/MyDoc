.. _Grid:

===========================
Grid system (Linux cluster)
===========================


Resource description
====================
..
  _Key numbers about the New cluster: compute nodes, node interconnect, operating system, and storage configuration.

The Grid system, also known as Linux cluster or Old cluster, is built up from a collection of 30 office destkops PCs (202 CPUs) that depend on different central servers/services. Those 30 PCs are located among the campus and belong to NTNU staff members or computer labs. The system is caracterized by centralized storage directories hosted in a heterogenous enviroment with different compilers, scientific libraries and licences. Fedora distributions in different version are installed on the PCs, in particular, version 26-31, depending on the host. There is not scheduler and the age of the hardware and softwares are varying. You can find  a list of all available softwares and relative host in the following description.

For technical questions please refer to the responsibles of the Grid system:, i.e. `Terje Rørsten <terje.rosten@ntnu.no>`_ and `Bogdan Voadais <bogdan.voaidas@ntnu.no>`_.

Connect to the HPC cluster
==========================

You can find detailed instruction on how to request access to the system on the page :doc:`/clusters/getting_started`.
The system can be reached through via ssh on the host that are listed in the ganglia interface. 
Example: ``ssh username@hpc-1.phys.ntnu.no`` or ``ssh username@hpc-2.phys.ntnu.no``.


Computing budget
================

There is not computing budged associated to this resource system, the user is allowed to use the resource up their account expiration date. 

Policies
========

The code of conduct aims to outline the responsibilities and the proper practices for the user community. Since this computing system is made of different workstations that staff and member of the university is using on daily basis, we are asking to strictly follow the rules in order to avoid perturbations to the main owner of the machine.  

The User Regulations define the basic guidelines for the usage of the computing resources. The right to access those resources may be revoked to whoever breaks any of the user regulations.

There is not a scheduling system and the number of jobs that a user can submit dependence on the resource available. Therefore users are not supposed to submit arbitrary amounts jobs and commands at the same time, as doing so would infringe our fair usage policy.

Let us also remind you that heavy processes disturbing the owner of the machine will be terminated without notice.
In the following link, you can find some suggestions and commands you can use to avoid disruption of others' users work :doc:`/clusters/cautions_grid`.
To have basic instructions to use a Linux system and its shell scripting refer to the link :doc:`/account/linux`
