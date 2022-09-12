.. _file_transfer:

==================================
Transferring files to/from HPC_IFY
==================================

Only ssh type of access is open to the HPC in IFY. Therefore to upload or
download data only scp and sftp can be used.

To transfer data to and from HPC use the following addresses:

::

    hpc-1.phys.ntnu.no
    hpc-2.phys.ntnu.no

Standard scp command and sftp clients can be used:

::

    ssh hpc-1.phys.ntnu.no
    ssh <username>@hpc-1.phys.ntnu.no

    sftp hpc-1.phys.ntnu.no
    sftp <username>@hpc-1.phys.ntnu.no

The `rsync <https://www.freecodecamp.org/news/rsync-examples-rsync-options-and-how-to-copy-files-over-ssh/>`_ tool is also available for transferring files. 

..
	Mounting the file system on you local machine using sshfs
	---------------------------------------------------------
	For linux users::

	sshfs [user@]stallo.uit.no:[dir] mountpoint [options]

	eg.::

	sshfs steinar@stallo.uit.no:  /home/steinar/stallo-fs/

	Windows users may buy and install
	`expandrive <https://www.expandrive.com/windows>`_.


	High-performance tools
	======================

	NONE cipher
	-----------
	This cipher has the highest transfer rate. Keep in mind that data after
	authentication is NOT encrypted, therefore the files can be sniffed and
	collected unencrypted by an attacker. To use you add the following to
	the client command line:

	::

	-oNoneSwitch=yes -oNoneEnabled=yes

	Anytime the None cipher is used a warning will be printed on the screen:

	::

	    "WARNING: NONE CIPHER ENABLED"

	If you do not see this warning then the NONE cipher is not in use.

	MT-AES-CTR

	If for some reason (eg: high confidentiality) NONE cipher can't be used,
	the multithreaded AES-CTR cipher can be used, add the following to the
	client command line (choose one of the numbers):
	
	::
	
	    -oCipher=aes[128|192|256]-ctr
	
	or:
	
	::
	
	    -caes[128|192|256]-ctr.
	
	
	Subversion and rsync
	--------------------
	The tools subversion and rsync is also available for transferring files.
