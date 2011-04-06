`|Redis Documentation| <index.html>`_
**SmembersCommand: Contents**
  `SMEMBERS \_key\_ <#SMEMBERS%20_key_>`_
    `Return value <#Return%20value>`_
SmembersCommand
===============

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SMEMBERS \_key\_
================

*Time complexity O(N)*
    Return all the members (elements) of the set value stored at *key*.
    Thisis just syntax glue for `SINTER <SintersectCommand.html>`_.

Return value
------------

`Multi bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png