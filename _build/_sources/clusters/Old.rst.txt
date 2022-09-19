.. _about_OLD:

=========
About OLD
=========


Resource description
====================

Key numbers about the OLD cluster: compute nodes, node interconnect,
operating system, and storage configuration.



+-------------------------+----------------------------------------------+---------------------------------------------+
|                         | Aggregated                                   | Per node                                    |
+=========================+==============================================+=============================================+
| Peak performance        | 312 Teraflop/s                               | 332 Gigaflop/s / 448 Gigaflops/s            |
+-------------------------+----------------------------------------------+---------------------------------------------+
|  |                      |  | 304 x  HP BL460 gen8 blade servers        |  | 1 x    HP BL460 gen8 blade servers       |
|  |  # Nodes             |  | 328 x HP SL230 gen8 servers               |  | 1 x.   HP SL230 gen8 servers             |
+-------------------------+----------------------------------------------+---------------------------------------------+
|  |                      |  | 608 / 4864                                |  | 2 / 16                                   |
|  | # CPU's / # Cores    |  | 656 / 6560                                |  | 2 / 20                                   |
+-------------------------+----------------------------------------------+---------------------------------------------+
|  |                      |  | 608 x 2.60 GHz Intel Xeon E5 2670         |  | 2 x 2.60 GHz Intel Xeon E5 2670          |
|  | Processors           |  | 656 x 2.80 GHz Intel Xeon E5 2680         |  | 2 x 2.80 Ghz Intel Xeon E5 2680          | 
+-------------------------+----------------------------------------------+---------------------------------------------+
| Total memory            | 26.2 TB                                      | 32 GB (32 nodes with 128 GB)                |
+-------------------------+----------------------------------------------+---------------------------------------------+
| Internal storage        | 155.2 TB                                     | 500 GB (32 nodes with 600GB raid)           |
+-------------------------+----------------------------------------------+---------------------------------------------+
| Centralized storage     | 2000 TB                                      | 2000 TB                                     |
+-------------------------+----------------------------------------------+---------------------------------------------+
| Interconnect            | Gigabit Ethernet + Infiniband  :sup:`1`      | Gigabit Ethernet + Infiniband  :sup:`1`     |
+-------------------------+----------------------------------------------+---------------------------------------------+

+-------------------------------------+-----------------------+
| Compute racks                       | 11                    |
+-------------------------------------+-----------------------+
| Infrastructure racks                | 2                     |
+-------------------------------------+-----------------------+
| Storage racks                       | 3                     |
+-------------------------------------+-----------------------+

 

1) All nodes in the cluster are connected with Gigabit Ethernet and
QDR Infiniband.

 
.. _linux-cluster:

OLD - a Linux cluster 
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

OLD - Name etimology
====================
Name meaning. 
