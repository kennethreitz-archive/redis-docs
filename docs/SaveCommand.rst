`|Redis Documentation| <index.html>`_
**SaveCommand: Contents**
      `SAVE <#SAVE>`_
    `Return value <#Return%20value>`_
SaveCommand
===========

ï»¿#sidebar `ControlCommandsSidebar <ControlCommandsSidebar.html>`_
SAVE
~~~~

    Save the whole dataset on disk (this means that all the databases
    are saved, as well as keys with an EXPIRE set (the expire is
    preserved). The server hangs while the saving is notcompleted, no
    connection is served in the meanwhile. An OK codeis returned when
    the DB was fully stored in disk.

    The background variant of this command is
    `BGSAVE <BgsaveCommand.html>`_ that is able to perform the saving
    in the background while the server continues serving other
    clients.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png