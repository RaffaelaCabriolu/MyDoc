..
  .. figure:: ???
   :scale: 57 %
..
   HPC


.. _news:

News and notifications
======================

News about planned/unplanned downtime, changes in hardware, and important
changes in software will be published in this page and on the login screen of the computing systems. 
For more information on the different situations see below.


System status and activity
--------------------------

For information on the system load, queued jobs, and node states for the HPC local cluster please refer to the first message passed as a first thing when you have logged into it. As alternative, you can digit ``sinfo -l``  to get the status of partitions and nodes, as in every standard linuc HPC system. 
For the IDUN system please refer to the general `link <https://www.hpc.ntnu.no/unplanned-idun-downtime-2/>`_.

You can get a quick overview of the system load for the Grid cluster in the grafical interface `ganglia`_ and from the initial message once you have loggin into it.  

.. :xref:`ganglia_interface`. Solve this

.. _ganglia: http://bird.phys.ntnu.no/ganglia/?r=4hr&cs=&ce=&m=load_one&tab=ch&vn=&hide-hf=false&hreg%5B%5D=phys

Those links are only visible from within the NTNU network.

Planned/unplanned downtime
--------------------------

In the case of a planned downtime, a reservation will be made in the
queuing system, so new jobs, that would not finish until the downtime,
won't start. If the system goes down, running jobs will be restarted,
if possible. 

Upgrades and Changes
--------------------

