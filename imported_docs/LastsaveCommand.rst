`|Redis Documentation| <index.html>`_
**LastsaveCommand: Contents**
  `LASTSAVE <#LASTSAVE>`_
    `Return value <#Return%20value>`_
LastsaveCommand
===============

ï»¿#sidebar `ControlCommandsSidebar <ControlCommandsSidebar.html>`_
LASTSAVE
========

    Return the UNIX TIME of the last DB save executed with success.A
    client may check if a `BGSAVE <BgsaveCommand.html>`_ command
    succeeded reading the LASTSAVEvalue, then issuing a
    `BGSAVE <BgsaveCommand.html>`_ command and checking at regular
    intervalsevery N seconds if LASTSAVE changed.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically an UNIX time
stamp.
.. |Redis Documentation| image:: redis.png