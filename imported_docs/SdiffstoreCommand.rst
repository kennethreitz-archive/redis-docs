`|Redis Documentation| <index.html>`_
**SdiffstoreCommand: Contents**
  `SDIFFSTORE \_dstkey\_ \_key1\_ \_key2\_ ... \_keyN\_ <#SDIFFSTORE%20_dstkey_%20_key1_%20_key2_%20...%20_keyN_>`_
    `Return value <#Return%20value>`_
SdiffstoreCommand
=================

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SDIFFSTORE \_dstkey\_ \_key1\_ \_key2\_ ... \_keyN\_
====================================================

*Time complexity O(N) where N is the total number of elements in all the provided sets*
    This command works exactly like SDIFF but instead of being returned
    the resulting set is stored in *dstkey*.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png