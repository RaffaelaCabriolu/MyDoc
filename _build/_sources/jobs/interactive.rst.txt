.. _interactive:

Interactive jobs
================

Starting an interactive job
---------------------------
An interactive job can be started wuth the following line: 

  $ srun --nodes=1 --ntasks-per-node=1 --time=00:10:00 --pty bash -i

This line asks for a single core on one interactive node for ten minutes with the
default amount of memory. The command prompt will appear as soon as
the job starts.

Once the interactive job starts it will appear a meassage similar to the following::

  srun: job 10345 queued and waiting for resources
  srun: job 10345 has been allocated resources

To end the job digit exit in the bash shell. If the job exceeds the time or memory
limits, it will abort.

Interactive jobs have the same policies as normal batch jobs, there
are no extra restrictions. Consider that you might be
sharing the node with other users.
