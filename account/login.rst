.. _login:

=============================
Logging in for the first time
=============================


Log in with SSH
===============

An *SSH* client (Secure SHell) is the required tool to connect to one of the computing system. Here you can find a basic knowledge of the ssh protocol. An *SSH* client provides secure encrypted communications between two hosts over an insecure network. 
If you already have *ssh* installed on your UNIX-like system, have a user account and password, login may be as easy as typing

::

 ssh <host _ip_address>         (for instance: ssh hpc-1.phys.ntnu.no)
 
If your user name on the machine differs from your user name on the local machine, you need to specify the user name on the machine to which you connect. For example:

::

 ssh <username@host _ip_address>         (for instance: ssh username@hpc-1.phys.ntnu.no)

into a terminal window.

And if you need X-forwarding (for instance, if you like to run Emacs in it's own window) or Y-forwarding,  you must log in like this:

::

 ssh -X -Y <machine name>

No matter how you login, you will need to confirm that the connection shall be trusted. Ex. if the SHA256 key fingerprint of the machine, i.e hpc-1.phys.ntnu.no, you are using is:

::

 SHA256:BLABLIBLU

You should get precisely this message the first time you login via ssh:

::

 The authenticity of host 'hpc-1.phys.ntnu.no (nn.nnn.nn)' can't be established.
 RSA key fingerprint is SHA256:YBLABLIBLU.
 Are you sure you want to continue connecting (yes/no)?

If you see this message with precisely this code, you can continue by typing ``yes`` and pressing *Enter*. If you connect for the first time and ssh does *not* show you this key, please contact support center.


Log in with an ssh key
----------------------

To avoid entering your password every time you login and to increase security, you can log in with an ssh keypair. This keypair consists of a private key that you have to store on your computer and a public key that you can store. On Linux or OSX simply type:

::

 ssh-keygen

and follow the instructions on the screen. Please use a good passphrase. You will have to enter this passphrase the first time you log in after a reboot of the computer, but not anymore afterwards. To copy the public key to hpc-1.phys, type:

::

 ssh-copy-id <username>@hpc-1.phys.ntnu.no

To learn more about ssh keys, have a look at `this <https://wiki.archlinux.org/index.php/SSH_keys>`_ page.

On Windows, you can use PuTTYgen that comes with PuTTY. More information on `ssh.com <https://www.ssh.com/ssh/putty/windows/puttygen>`_.


SSH clients for Windows and Mac
-------------------------------

At the `OpenSSH page <https://www.openssh.com>`_ you will find several *SSH* alternatives for both Windows and Mac.

Mac OS X comes with its own implementation of *OpenSSH*, so you don't need to install any third-party software to take advantage of the extra security *SSH* offers. You can use it right away. 


Learning more about SSH
-----------------------

To learn more about using SSH, please also consult the `OpenSSH page <https://www.openssh.com>`_ page and take a look at the manual page on your system (*man ssh*).

Logging on the compute nodes
============================

Information on how to log in on a compute node.

Some times you may want to log on a compute node (for instance to check
out output files on the local work area on the node), and this is also
done by using SSH. From hpc-1.phys.ntnu.no, for example, log into 
the compute-x in the following way:

::

    ssh -Y compute-x     (for instance: ssh compute-2)


If you don't need display forwarding you can omit the "-Y" option
above.

If you for instance want to run a program interactively on a compute
node, and with display forwarding to your desktop you should do
something like this:

Below is an example:

::

    1) Log in on hpc-1.phys.ntnu.no with display forwarding.

       $ ssh -Y hpc-1.phys.ntnu.no             

    2) Reserve and log in on a compute node with display forwarding.
       (start an interactive job.)

       $ srun -N 1 -t 1:0:0 --pty bash -i

    3) Open a new terminal window, type squeue -j <jobid> (it shows you which node(s) was allocated
       to that specific job). Then ssh -Y <nodename> to that node and start your preferred gui.
