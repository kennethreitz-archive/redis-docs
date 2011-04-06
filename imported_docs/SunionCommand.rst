`|Redis Documentation| <index.html>`_
**SunionCommand: Contents**
  `SUNION \_key1\_ \_key2\_ ... \_keyN\_ <#SUNION%20_key1_%20_key2_%20...%20_keyN_>`_
    `Return value <#Return%20value>`_
SunionCommand
=============

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SUNION \_key1\_ \_key2\_ ... \_keyN\_
=====================================

*Time complexity O(N) where N is the total number of elements in all the provided sets*
    Return the members of a set resulting from the union of all thesets
    hold at the specified keys. Like in LRANGE the result is sent tothe
    client as a multi-bulk reply (see the protocol specification
    formore information). If just a single key is specified, then this
    commandproduces the same result as
    `SMEMBERS <SmembersCommand.html>`_.

    Non existing keys are considered like empty sets.

Return value
------------

`Multi bulk reply <ReplyTypes.html>`_, specifically the list of
common elements.
.. |Redis Documentation| image:: redis.png