`|Redis Documentation| <index.html>`_
**SetexCommand: Contents**
  `SETEX \_key\_ \_time\_ \_value\_ <#SETEX%20_key_%20_time_%20_value_>`_
    `Return value <#Return%20value>`_
SetexCommand
============

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
SETEX \_key\_ \_time\_ \_value\_
================================

*Time complexity: O(1)*
    The command is exactly equivalent to the following group of
    commands:

::

    SET _key_ _value_
    EXPIRE _key_ _time_

    The operation is atomic. An atomic
    `SET <SetCommand.html>`_+`EXPIRE <ExpireCommand.html>`_ operation
    was already providedusing `MULTI/EXEC <MultiExecCommand.html>`_,
    but SETEX is a faster alternative providedbecause this operation is
    very common when Redis is used as a Cache.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png