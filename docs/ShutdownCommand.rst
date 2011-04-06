`|Redis Documentation| <index.html>`_
**ShutdownCommand: Contents**
  `SHUTDOWN <#SHUTDOWN>`_
    `Return value <#Return%20value>`_
ShutdownCommand
===============

ï»¿#sidebar `ControlCommandsSidebar <ControlCommandsSidebar.html>`_
SHUTDOWN
========

    Stop all the clients, save the DB, then quit the server. This
    commandsmakes sure that the DB is switched off without the lost of
    any data.This is not guaranteed if the client uses simply "SAVE"
    and then"QUIT" because other clients may alter the DB data between
    the twocommands.

Return value
------------

`Status code reply <ReplyTypes.html>`_ on error. On success nothing
is returned since the server quits and the connection is closed.
.. |Redis Documentation| image:: redis.png