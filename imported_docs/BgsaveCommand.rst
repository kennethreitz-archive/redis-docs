`|Redis Documentation| <index.html>`_
**BgsaveCommand: Contents**
  `BGSAVE <#BGSAVE>`_
    `Return value <#Return%20value>`_
BgsaveCommand
=============

ï»¿#sidebar `ControlCommandsSidebar <ControlCommandsSidebar.html>`_
BGSAVE
======

    Save the DB in background. The OK code is immediately
    returned.Redis forks, the parent continues to server the clients,
    the childsaves the DB on disk then exit. A client my be able to
    check if theoperation succeeded using the
    `LASTSAVE <LastsaveCommand.html>`_ command.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png