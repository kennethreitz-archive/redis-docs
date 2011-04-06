`|Redis Documentation| <index.html>`_
**SunionstoreCommand: Contents**
  `SUNIONSTORE \_dstkey\_ \_key1\_ \_key2\_ ... \_keyN\_ <#SUNIONSTORE%20_dstkey_%20_key1_%20_key2_%20...%20_keyN_>`_
    `Return value <#Return%20value>`_
SunionstoreCommand
==================

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SUNIONSTORE \_dstkey\_ \_key1\_ \_key2\_ ... \_keyN\_
=====================================================

*Time complexity O(N) where N is the total number of elements in all the provided sets*
    This command works exactly like SUNION but instead of being
    returned the resulting set is stored as *dstkey*. Any existing
    value in *dstkey* will be over-written.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png