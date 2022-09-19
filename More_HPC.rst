.. _HPC:

====================
Local HPC facilities
====================

Resource description
====================

The Department of physics is setting an High Performance Computing (HPC) system for debugging and testing purposes in vision of longer production projects that would be eventually carried out in national, i.e. IDUN or NOTUR, or international infrastructures, i.e. PRACE production access. Despite to be developed for computational projects that have a limited running time, IFY decided to not limit in the accessibility to the cluster.
The cluster is administred according to a queing system and the SLURM scheduler.The OSDebian distribution is installed on the machines along with Intel compilers, debuggin tools and several licensed softwares.  

.. In addition, there are certain rules and boundaries to be respected.    
   

+-------------------------+----------------------------------------------+----------------------------------------+
|                         | Cumulative                                   | Per node                               |
+=========================+==============================================+========================================+
| Peak performance        |                                              |                                        |
+-------------------------+----------------------------------------------+----------------------------------------+
|  |                      |  |   2-3 x login, master nodes               |  ?????                                 | 
|  |                      |  |   5 x Dell PowerEdge R740                 |  ?????                                 |
|  |                      |  |   5 x Dell PowerEdge R640 [PoreLab]       |  ?????                                 |
|  |  # Nodes             |  |   6 x Dell PowerEdge R640                 |  ?????                                 | 
+-------------------------+----------------------------------------------+----------------------------------------+
|  |                      |  |   24/?????                                |  | ?????                               |
|  |                      |  |   32/?????                                |  | ?????                               |
|  | # CPU's / # Cores    |  |   40/?????                                |  | ?????                               |
+-------------------------+----------------------------------------------+----------------------------------------+
|  |                      |  | 24 x 2.30 GHz Intel(R) Xeon(R) Gold 5218  |  | 2 x 2.30 GHz Intel                  |
|  | Processors           |  | 32 x 2.30 GHz Intel(R) Xeon(R) Gold 5218  |  | 2 x 2.30 Ghz Intel                  | 
|  |                      |  | 40 x 2.10 GHz Intel(R) Xeon(R) Gold 5218  |  | 2 x 2.10 Ghz Intel                  |
+-------------------------+----------------------------------------------+----------------------------------------+
| Total memory            | ????? TB                                     | ?? GB (?? nodes with ?? GB)            |
+-------------------------+----------------------------------------------+----------------------------------------+
| Internal storage        | ????? TB ?                                   | ?? GB (??nodes ) ?                     |
+-------------------------+----------------------------------------------+----------------------------------------+
| Centralized storage     | ???? TB  ?                                   | ?? TB                                  |
+-------------------------+----------------------------------------------+----------------------------------------+
| Interconnect            | 10 Gigabit Ethernet :sup:`1`                 | 10 Gigabit Ethernet :sup:`1`           |
+-------------------------+----------------------------------------------+----------------------------------------+

+-------------------------------------+-----------------------+
| Compute racks                       | 1                     |
+-------------------------------------+-----------------------+
 

1) All nodes in the cluster are connected with Gigabit Ethernet 

 
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
