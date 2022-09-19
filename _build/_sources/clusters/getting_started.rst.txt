===============
Getting started
===============

This section presents the basic knowledge needed to use efficiently the different computational facilities in Physics that include three computing systems:

.. toctree::
   :maxdepth: 1

   hpc.rst
   idun.rst  
   grid.rst

login-accounts
--------------

Every one that is associated with the Physics Department can be granted an account to the Physics computing systems. To set up an account at the :doc:`grid` and :doc:`idun` facilities contact `Bogdan Voadais <bogdan.voaidas@ntnu.no>`_, or `Terje Rørsten <terje.rosten@ntnu.no>`_, while for having access to the :doc:`hpc` contact `Egil Holvik <egil.holvik@ntnu.no>`_.

Connect to a cluster
--------------------

You can connect to the facilities via the *SSH* protocol. You may refer to sections :doc:`hpc`, :doc:`idun`, and, :doc:`grid` to have the detailed instructions for each computing system.
In general, on Linux and OSX you may directly connect by opening a terminal and writing ``ssh username@host_ip_adress``. From Windows, you may connect using `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_. It is possible to perform the X-forwarding for graphical applications. Please, follow the link for details on all mentioned methods and on the ssh protocol in general: :doc:`/account/login`

On login nodes
--------------
Once you have performed the login, your will be on a login node. Do *not* lunch any long-lasting programs on the login nodes of the HPC local cluster and of the IDUN system! In general, the login nodes of a cluster shall only be used for job preparation and simple file operations. Once you login on the HPC local and on the Grid system, you will be in your home directory ``/home/username``. For now, there is not quota or strage limitation on your home folder, but, as a rule of thumbs, your files should not occupy more than 50 GB. The Physics Department will impose some restrictions on storage soon. Please remove non necessary files regularly. 
Your home folder is shared among the Grid system and the Local HPC cluster, since they refer to common login nodes. There is a backup system for your home directory and it is managed by the central IT system. 
Regarding the Idun system, you can get more details on the administration of storage and back up system at the following link `IDUN <https://www.hpc.ntnu.no/idun/how-to-become-a-shareholder-and-partner-in-idun/>`_. 

Get help
--------

Feedback regarding this documentation, any other suggestion concerning the computational resources at NTNU in Physics are welcomed and those should be adressed to the people in the session :doc:`/help/staff`.
To get technical guidance and help on a particular computing system refer to the relative specific session. Furthermore, you can refer to the sessions :doc:`/help/faq`, :doc:`/help/hpc-qa-sessions`, and, :doc:`/help/tutorials` for practical examples and common technical issues. To get updates on the status of the computing system refer to the session :doc:`/news/news`. 


Happy researching!
