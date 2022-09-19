.. _hpc:


Local HPC
~~~~~~~~~

Resource description
====================

The Department of Physics, IFY, retains an High Performance Computing (HPC) system, HPC_IFY, for debugging, testing purposes and, small projects. For long production projects we suggest to apply to national, i.e. IDUN or NOTUR, or international infrastructures, i.e. PRACE production access. Despite to be developed for small computational projects that have a limited running time, IFY decided to not limit the accessibility to the cluster.
The cluster is administred according to a queing system, the `Slurm <https://slurm.schedmd.com/documentation.html>`_ scheduler, and, the `Lmod <https://lmod.readthedocs.io/en/latest/index.html>`_ module system. Further explanation on the Slurm and Lmod commands are in the sessions :doc:`/jobs/slurm_parameter` and :doc:`/help/tutorials`. 
The OSDebian distribution is installed on the machines along with Intel compilers, debugging tools and several licensed softwares.  

..
  In addition, there are certain rules and boundaries to be respected.    
   

+----------------------+---------------------------------------------+----------------------------------------------+
|                      | Cumulative                                  | Per node                                     |
+======================+=============================================+==============================================+
| |                    | |   5 x Dell  PowerEdge R740                | | 1 x Dell  PowerEdge R740                   |
| | #Nodes             | |   5 x Dell  PowerEdge R640                | | 1 x Dell  PowerEdge R640                   |
| |                    | |   6 x Dell  PowerEdge R640                | | 1 x Dell  PowerEdge R640                   | 
+----------------------+---------------------------------------------+----------------------------------------------+
| |                    | |   10/80                                   | | 2/16                                       |
| | #CPU's/# Cores     | |   10/80                                   | | 2/16                                       |
| |                    | |   12/120                                  | | 2/20                                       |
+----------------------+---------------------------------------------+----------------------------------------------+
| |                    | | 10xIntel(R) Xeon(R) Gold                  | | 2xIntel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz |
| | Processors         | | 10xIntel(R) Xeon(R) Gold                  | | 2xIntel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz | 
| |                    | | 12xIntel(R) Xeon(R) Gold                  | | 2xIntel(R) Xeon(R) Gold 5218R CPU @ 2.10GHz| 
+----------------------+---------------------------------------------+----------------------------------------------+
| Total memory         |   2 TB                                      |  128   GB                                    |
+----------------------+---------------------------------------------+----------------------------------------------+
| Internal storage     |   7 TB                                      |  447   GB  (SSD disk)                        |
+----------------------+---------------------------------------------+----------------------------------------------+
| Centralized storage  |   3.5 TB                                    |    3.5 TB                                    |
+----------------------+---------------------------------------------+----------------------------------------------+
| Interconnect         | 10 Gigabit Ethernet                         | 10 Gigabit Ethernet                          |
+----------------------+---------------------------------------------+----------------------------------------------+

+-------------------------------------+-----------------------+
| Compute racks                       | 1                     |
+-------------------------------------+-----------------------+
 

All nodes in the cluster are connected with Gigabit Ethernet and hyperthreading is enabled. 

For further information and technical assistance, refer to the technical responsible of the HPC Local cluster,
Egil Holvik at support-kongull@hpc.ntnu.no.

Connect to the HPC cluster
==========================

To request access to the HPC local cluster contact `Egil Holvik <https://www.ntnu.no/ansatte/egil.holvik>`_.  
The HPC system can be reached through ssh via: ``ssh username@hpc-1.phys.ntnu.no`` or ``ssh username@hpc-2.phys.ntnu.no``. Refer to the session 
:doc:`/account/login` for examples and further explanation on the ssh protocol. 

File Systems and data Back-up
=============================
Different file systems are supported and summarized in the following table:

+----------------------+-----------+------------+-----------+------------+
|                      |   /home   |   /worko   |   /work   |  /scratch  |
+======================+===========+============+===========+============+
|   Type               |    NFS    |    NFS     |    NFS    |   NFS      |
+----------------------+-----------+------------+-----------+------------+
|   Data-Backup        |    Daily  |    None    |    None   |   None     |
+----------------------+-----------+------------+-----------+------------+
|   Access Speed       |    Slow   |    Slow    |    Fast   |   Fast     |
+----------------------+-----------+------------+-----------+------------+
  
Data belonging to active accounts in the file system /home are under-backup. There is no backup for data under the /work, /worko and /scratch filesystem, therefore no data recovery is possible in case of accidental loss or for data deleted due to the cleaning policy implemented on this filesystem. The user should use /scratch and /work for computing while /home and /worko as storage and processing folders. Additionally, /home is a backed-up shared folder to which you can access on whatever ntnu login system you use, this mean it is particularly handy to save your definitive data there.  
To move files from your computer to the Local HPC or vice versa, you may use any tool that works with *ssh*. On Linux and OSX, these are scp, rsync, or similar programs. On Windows, you may use WinSCP. Follow the session :doc:`/storage/file_transfer` for more details.


Partitions
==========

In the HPC_IFY we have the following partitions:

+----------------+-----------------+---------+-----------+
|   Partition    |  Time-limit     |  Nodes  |    Job    |
|                | (dd-hs:min:sec) |         |   size    |
+================+=================+=========+===========+
|   normal*      |    7-00:00:00   |    5    |    1-inf  |
+----------------+-----------------+---------+-----------+
|   norma2       |    5-00:00:00   |    6    |    1-inf  |
+----------------+-----------------+---------+-----------+
|   short        |    1:00:00      |    15   |    1-inf  |
+----------------+-----------------+---------+-----------+
|   long         |   25-00:00:0    |    5    |    1-3    |
+----------------+-----------------+---------+-----------+
|   PoreLab      |   14-00:00:0    |    5    |    1-inf  |
+----------------+-----------------+---------+-----------+

To have more informations about the different partitions, you can type ``sinfo -l`` after having logged to the HPC_IFY machines.

There are no limitations on the number of running jobs per user for all except for the partition long. For the rest, CPUs, jobs and memory are limited by the batch system in function of the available resources. The PoreLab nodes belong to the `PoreLab <https://porelab.no/>`_ center of excellence and their affiliated members have priority on those nodes. 

Available modules and software
==============================

There are many softwares and modules pre-installed. After having login into a machine, you may get a list of all modules by typing ``module avail`` in the terminal. You can also search for a specific module using the spider tool, e.g. ``module spider intel`` will search for the available intel compilers. Once found the module of choice, you may load it using ``module load intel-compilers/2021.1.2``. For more details on the module system refer to the documentation `Lmod <https://lmod.readthedocs.io/en/latest/index.html>`_ .
Once you have loaded the necessary modules, all files and dependencies will now be available, i.e. you can now simply call ``python -version`` to run python and check the loaded version. You can also compile your own software, if necessary, following the instructions in :doc:`/software/modules`. 
To search for a program, utility or function you can use the interface `man <https://man7.org/linux/man-pages/man1/man.1.html>`_ typing ``man python``. 

Perform Numerical calculations
==============================
 
To launch your program, you can use the interactive mode, or you need to write a job script (see the section :doc:`/jobs/slurm_parameter`). In either modes, you define for how long your job (i.e. the program) will reserve the requested resources and how much memory and compute cores it needs. To use the cluster a basic knowledge of the Linux shell scripting is necessary; refer to the session :doc:`/account/linux` for a very short introduction on it.
Furthermore, refer to the sessions :doc:`/jobs/batch` and :doc:`/jobs/examples` for more instructions on the batch system.
Every job that gets started will be charged to your quota. Your quota is calculated in hours of CPU time and is connected to your specific project. 
To see the status of your quota account(s), you can type ``sacct``.

..
  _and refer to the session: :doc:`/account/accounting`.  

Computing budget 
================

Compute time is accounted in CPU/hours and it is organized on semester pricing bill. 
Please note that resources are assigned over a defined time-windows. Quotas are reset on deadlines base, therefore please make sure to use thoroughly your compute budget within the corresponding time frame. Resources unused in the alloted period are not transferred to the next allocation period but are forever lost.

Policies
========
The `IFY computational resources` code of conduct aims to outline the responsibilities and the proper practices for the IFY-NV user community. The User Regulations define the basic guidelines for the usage of the computing resources. The right to access those resources may be revoked to whoever breaches any of the user regulations.

Data Retention Policies
=======================
Please note that the long term storage service is granted as far as your project is active and the data will be removed without further notice 3 months after the expiration of the project: please check the applicable filesystem policies for the grace period granted after the expiration of the project.
Furthermore, as soon as your project expires, the backup of the data belonging to the project will be disabled immediately: therefore no data backup will be available anymore after the final data removal.

Fair Usage of Shared Resources
==============================
The Slurm scheduling system is a shared resource that can handle a limited amount of batch jobs and interactive commands simultaneously. Therefore users are not supposed to submit arbitrary amounts of Slurm jobs and commands at the same time, as doing so would infringe our fair usage policy.
Let us also remind you that running applications on the login nodes is not allowed, as they are a shared resource too. Please submit your simulations with the Slurm scheduler, in order to allocate and run your jobs on a compute node: heavy processes running on the login nodes will be terminated.
