.. _about_GRO:

============
About GRO
============


Resource description
====================

Key numbers about the GRO cluster: compute nodes, node interconnect,
operating system, and storage configuration.

Compute nodes

+-------------------------+-----------------+------------------------------------+--------+-----------+------------------+
| Node                    | Model           | CPUs                               | #Cores | Memory GB | /scratch GB      |
+=========================+=================+====================================+========+===========+==================+
| compute-[0-4]           | Dell PER740xd   | 2x Intel® Xeon® Gold 5118 2.3GHz   | 24     | 128       | 355              |
+-------------------------+-----------------+------------------------------------+--------+------------------------------+
| compute-[11-15]         | Dell PER640     | 2x Intel® Xeon® Gold 5218 2.3GHz   | 32     | 128       | 355              |
+-------------------------+-----------------+------------------------------------+--------+------------------------------+
| compute-[16-21]         | Dell PER640     | 2x Intel® Xeon® Gold 5218R 2.1GHz  | 40     | 128       | 355              |
+-------------------------+-----------------+------------------------------------+--------+------------------------------+


All nodes in the cluster are connected with Gigabit Ethernet

 
.. _linux-cluster:

GRO - a Linux cluster 
========================

This is just a quick and brief introduction to the general features of Linux Clusters.

A Linux Cluster - one machine, consisting of many machines
----------------------------------------------------------

On one hand you can look at large Linux Clusters as rather large and powerful supercomputers, but on the other hand you can look at them as just a large bunch of servers and some storage system(s) connected with each other through a (high speed) network. Both of these views are fully correct, and it's therefore important to be aware of the strengths and the limitations of such a system.

Clusters vs. SMP’s
------------------

Until July 2004, most of the supercomputers available to Norwegian HPC users were more or less large Symmetric Multi Processing (SMP's)  systems; like the HP Superdome's  at UiO and UiT, the IBM Regatta at UiB and the SGI Origion and IBM p575 systems at NTNU.

On SMP systems most of the resources (CPU, memory, home disks, work disks, etc) are more or less uniformly accessible for any job running on the system. This is a rather simple picture to understand, it’s nearly as your desktop machine – just more of everything: More users, more CPU’s, more memory, more disks etc.

On a Linux Cluster the picture is quite different. The system consists of several independent compute nodes (servers) connected with each other through some (high speed) network and maybe hooked up on some storage system. So the HW resources (like CPU, memory, disk, etc) in a cluster are in general distributed and only locally accessible at each server.


Linux operating system (Rocks): `<http://www.rocksclusters.org/>`_
==================================================================

Since 2003, the HPC-group at has been one of five international
development sites for the Linux operating system Rocks. Together with
people in Singapore, Thailand, Korea and USA, we have developed a tool
that has won international recognition, such as the price for "Most
important software innovation  " both in 2004 and 2005 in HPCWire. Now
Rocks is a de-facto standard for cluster-management in Norwegian
supercomputing.

GRO - name etymology
========================

Why the cluster has this name? 
