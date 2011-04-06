`|Redis Documentation| <index.html>`_
**SdiffCommand: Contents**
  `SDIFF \_key1\_ \_key2\_ ... \_keyN\_ <#SDIFF%20_key1_%20_key2_%20...%20_keyN_>`_
    `Return value <#Return%20value>`_
SdiffCommand
============

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SDIFF \_key1\_ \_key2\_ ... \_keyN\_
====================================

*Time complexity O(N) with N being the total number of elements of all the sets*
    Return the members of a set resulting from the difference between
    the firstset provided and all the successive sets. Example:

::

    key1 = x,a,b,c
    key2 = c
    key3 = a,d
    SDIFF key1,key2,key3 => x,b

    Non existing keys are considered like empty sets.

Return value
------------

`Multi bulk reply <ReplyTypes.html>`_, specifically the list of
common elements.
.. |Redis Documentation| image:: redis.png