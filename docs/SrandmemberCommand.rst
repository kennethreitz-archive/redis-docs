`|Redis Documentation| <index.html>`_
**SrandmemberCommand: Contents**
  `SRANDMEMBER \_key\_ <#SRANDMEMBER%20_key_>`_
    `Return value <#Return%20value>`_
SrandmemberCommand
==================

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SRANDMEMBER \_key\_
===================

*Time complexity O(1)*
    Return a random element from a Set, without removing the element.
    If the Set is empty or the key does not exist, a nil object is
    returned.

    The `SPOP <SpopCommand.html>`_ command does a similar work but the
    returned elementis popped (removed) from the Set.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png