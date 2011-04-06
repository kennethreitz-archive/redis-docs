`|Redis Documentation| <index.html>`_
**SinterstoreCommand: Contents**
  `SINTERSTORE \_dstkey\_ \_key1\_ \_key2\_ ... \_keyN\_ <#SINTERSTORE%20_dstkey_%20_key1_%20_key2_%20...%20_keyN_>`_
    `Return value <#Return%20value>`_
SinterstoreCommand
==================

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SINTERSTORE \_dstkey\_ \_key1\_ \_key2\_ ... \_keyN\_
=====================================================

*Time complexity O(NM) worst case where N is the cardinality of the smallest set and M the number of sets*
    This commnad works exactly like SINTER but instead of being
    returned the resulting set is sotred as *dstkey*.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png