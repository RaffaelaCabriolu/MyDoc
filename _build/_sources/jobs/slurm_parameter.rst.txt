.. _slurm:

======================
SLURM Workload Manager
======================

Slurm is a queing system and a job scheduler installed in the Local HPC at IFY and in IDUN. Lmod is a module system that manages the dependencies of modules and softwares. 

There are two ways of starting jobs with SLURM; either interactively with ``srun``
or as a script with ``sbatch``.

Interactive jobs are a good way to test your setup before you put it into a script
or to work with other applications like python.
You immediately see the results and can check if all parts behave as you expected.

Starting an interactive job
---------------------------
An interactive job can be started wuth the following line:

  $ srun --nodes=1 --ntasks-per-node=1 --time=00:10:00 --pty bash -i

This line asks for a single core on one interactive node for ten minutes with the
default amount of memory. The command prompt will appear as soon as
the job starts.

Once the interactive job starts, it will appear a meassage similar to the following::

  srun: job 10345 queued and waiting for resources
  srun: job 10345 has been allocated resources

To end the job digit exit in the bash shell. If the job exceeds the time or memory
limits, it will abort.

Interactive jobs have the same policies as normal batch jobs, there
are no extra restrictions. Consider that you might be
sharing the node with other users.

.. _slurm_parameter:

SLURM Parameter
-----------------

SLURM supports a multitude of different parameters that can enable tailoring your resources requests to your computational needs, however, if not used appropriately, those parameters can cause a waisting of computational resources and time. 

The following parameters can be used as command line parameters with ``sbatch`` and
``srun`` or in jobscript. To use a parameter in a jobscript, start a newline with ``#SBATCH`` followed by the parameter, refer to :ref:`job_script_examples` for more examples.
In the following, you can replace <....> with the value you want, e.g. ``--job-name=test-job``, either in the jobscript approach or in the interactive approach.


Basic settings
+++++++++++++++

=============================    ================================================================================
Parameter                        Function
=============================    ================================================================================
--job-name=<name>                Job name to be displayed by for example ``squeue``
--output=<path>                  Path to the file where the job (error) output is written to 
--mail-type=<type>               Turn on mail notification; type can be one of BEGIN, END, FAIL, REQUEUE or ALL
--mail-user=<email_address>      Email address to send notifications to
=============================    ================================================================================


Requesting Resources
+++++++++++++++++++++

=============================   ============================================================================================================================
Parameter                       Function
=============================   ============================================================================================================================
--time=<d-hh:mm:ss>             Time limit for job. Job will be killed by SLURM after time has run out. Format days-hours:minutes:seconds
--nodes=<num_nodes>             Number of nodes. Multiple nodes are only useful for jobs with distributed-memory (e.g. MPI).
--mem=<MB>                      Memory (RAM) per node. Number followed by unit prefix, e.g. 16G
--mem-per-cpu=<MB>              Memory (RAM) per requested CPU core
--ntasks-per-node=<num_procs>   Number of (MPI) processes per node. More than one useful only for MPI jobs. Maximum number depends nodes (number of cores)
--cpus-per-task=<num_threads>   CPU cores per task. For MPI use one. For parallelized applications benchmark this is the number of threads.
--exclusive                     Job will not share nodes with other running jobs.
=============================   ============================================================================================================================


Accounting
+++++++++++++++++++++
For the partitions in HPC_IFY refer to :doc:`/clusters/hpc`.

==================      ====================================================================================================================
--account=<name>        Project (not user) account the job. HPC_FY is not an account-based for now. You should use this in the IDUN cluster. 
--partition=<name>      Partition/queue in which o run the job. Select that in base of the needs.
==================      ====================================================================================================================


Advanced Job Control
+++++++++++++++++++++

==========================   ==================================================================================================================================================================
Parameter                    Function
==========================   ==================================================================================================================================================================
--array=<indexes>            Submit a collection of similar jobs, e.g. ``--array=1-10``. (sbatch command only). See official `SLURM documentation <https://slurm.schedmd.com/job_array.html>`_
--dependency=<state:jobid>   Wait with the start of the job until specified dependencies have been satified. E.g. --dependency=afterok:123456
--ntasks-per-core=2          Enables hyperthreading per core. Only useful in special circumstances.
==========================   ==================================================================================================================================================================

Differences between CPUs and tasks
-------------------------------------

As a new user writing your first SLURM job script, the difference between
``--ntasks`` and ``--cpus-per-taks`` is typically quite confusing.
You may wonder, for example, which SLURM parameters to use to run your program on a single node with 10 cores. 

The answer is it depends whether the your application supports MPI.
MPI (message passing protocol) is a communication interface used for developing 
parallel computing programs on distributed memory systems.
This is necessary for applications running on multiple computers (nodes) to be able to
share (intermediate) results between the nodes.

To decide which set of parameters you should use, check if your application utilizes
MPI and therefore would benefit from running on multiple nodes simultaneously.
On the other hand you have an non-MPI enables application or made a mistake in 
your setup, it doesn't make sense to request more than one node.

.. _slurm_recommendations:

Settings for OpenMP and MPI jobs
--------------------------------

Single node jobs
++++++++++++++++

This request is useful for applications that are not optimized for HPC (high performance computing) systems,
like simple python or R scripts and a lot of other softwares that are optimized for desktop PCs.

Simple applications and scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Many simple tools and scripts are not parallized at all and therefore won't profit from
more than one CPU core.

=============================   ============================================================================================================================
Parameter                       Function
=============================   ============================================================================================================================
--nodes=1                       Start a unparallized job on only one node
--ntasks-per-node=1             For OpenMP, only one task is necessary
--cpus-per-task=1               Just one CPU core will be used.
--mem=<MB>                      Memory (RAM) for the job. Number followed by unit prefix, e.g. 10G
=============================   ============================================================================================================================

If you are unsure if your application can benefit from more cores try a higher number of --cpus-per-task and
observe the CPU load of your job. If it stays at approximately one there is no need to ask for more than one.


OpenMP applications
^^^^^^^^^^^^^^^^^^^
OpenMP (Open Multi-Processing) is a multiprocessing library is often used for programs on
shared memory systems. Shared memory describes systems which share the memory between all 
processing units (CPU cores), so that each process can access all data on that system.

=============================   ============================================================================================================================
Parameter                       Function
=============================   ============================================================================================================================
--nodes=1                       Start a parallel job for a shared memory system on only one node
--ntasks-per-node=1             For OpenMP, only one task is necessary
--cpus-per-task=<num_threads>   Number of threads (CPU cores) to use
--mem=<MB>                      Memory (RAM) for the job. Number followed by unit prefix, e.g. 16G
=============================   ============================================================================================================================


Multiple node jobs (MPI)
+++++++++++++++++++++++++

In certain cases, one single node and/or few CPU cores are not enough. 

You can either just start a number of MPI tasks or request whole nodes.
While using whole nodes guarantees that a low latency and high bandwidth it usually results in a longer queuing time compared to cluster wide job.
With the latter the SLURM manager can distribute your task across all nodes and utilize otherwise unused cores on nodes which for example run a 16 core job on a 20 core node. This usually results in shorter queuing times but slower inter-process connection speeds.

We strongly advice all users to ask for a given set of cores when submitting
multi-core jobs.  To make sure that you utilize full nodes, you should ask for
sets that adds up to both 16 and 20 (80, 120 etc) due to the hardware specifics

This will make the best use of the resources and give the most predictable
execution times. If your job requires more than the default available memory per
core (125 GB/node gives 7,8 GB/core for 16 core nodes and 6,25 GB/core for 20 core
nodes) you should adjust this need with the following command: ``#SBATCH
--mem-per-cpu=25 GB`` When doing this, the batch system will automatically allocate
4 cores of 20 core nodes.

To use whole nodes
^^^^^^^^^^^^^^^^^^

=============================   =============================================================================================================================
Parameter                       Function
=============================   =============================================================================================================================
--nodes=<num_nodes>             Start a parallel job for a distributed memory system on several nodes
--ntasks-per-node=<num_procs>   Number of (MPI) processes per node. Maximum number depends nodes (16 on HPC_IFY)
--cpus-per-task=1               Use one CPU core per task. 
--exclusive                     Job will not share nodes with other running jobs. You don't need to specify memory as you will get all available on the node.
=============================   =============================================================================================================================


To distribute your job
^^^^^^^^^^^^^^^^^^^^^^

=============================   ============================================================================================================================
Parameter                       Function
=============================   ============================================================================================================================
--ntasks=<num_procs>            Number of (MPI) processes in total. Equals to the number of cores
--mem-per-cpu=<MB>              Memory (RAM) per requested CPU core. Number followed by unit prefix, e.g. 2G
=============================   ============================================================================================================================


Scalability
+++++++++++

You should run a few tests to see what is the best fit between minimizing
runtime and maximizing your allocated cpu. That is you should not ask for
more cpus for a job than you really can utilize efficiently. Try to run your
job on 1, 2, 4, 8, 16, etc., cores to see when the runtime for your job starts
tailing off. If you start to see less than 30% improvement in runtime when
doubling the cpu-counts you should probably not increase further the number of cores. 
Recommendations to a few of the most used applications can be found in :ref:`sw_guides`.


Job related environment variables
---------------------------------

Here we list some environment variables that are defined when you run a job
script.  These is not a complete list. Please consult the SLURM documentation
for a complete list.

Job number::

  SLURM_JOBID
  SLURM_ARRAY_TASK_ID  # relevant when you are using job arrays

List of nodes used in a job::

  SLURM_NODELIST

..
	Scratch and Work directory::
	Is $WORK directory different from /work/, what shall it be used? 

  	WORK  # defaults to /scracth/

	We recommend to **not** use $SCRATCH but to construct a variable yourself and use that in your script, e.g.::

	  SCRATCH_DIRECTORY=/scratch/${USER}/my-example/${SLURM_JOBID}

	The reason for this is that if you forget to sbatch your job script, then $SCRATCH may suddenly be undefined and you risk erasing your
	entire /global/work/${USER}.

Submit directory (this is the directory where you have sbatched your job)::

  SUBMITDIR
  SLURM_SUBMIT_DIR

Default number of threads::

  OMP_NUM_THREADS=1

Task count::

  SLURM_NTASKS
