`|Redis Documentation| <index.html>`_
**SpopCommand: Contents**
  `SPOP \_key\_ <#SPOP%20_key_>`_
    `Return value <#Return%20value>`_
SpopCommand
===========

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SPOP \_key\_
============

*Time complexity O(1)*
    Remove a random element from a Set returning it as return value.If
    the Set is empty or the key does not exist, a nil object is
    returned.

    The `SRANDMEMBER <SrandmemberCommand.html>`_ command does a similar
    work butthe returned element is not removed from the Set.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png