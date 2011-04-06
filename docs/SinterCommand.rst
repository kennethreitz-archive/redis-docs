`|Redis Documentation| <index.html>`_
**SinterCommand: Contents**
  `SINTER \_key1\_ \_key2\_ ... \_keyN\_ <#SINTER%20_key1_%20_key2_%20...%20_keyN_>`_
    `Return value <#Return%20value>`_
SinterCommand
=============

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SINTER \_key1\_ \_key2\_ ... \_keyN\_
=====================================

*Time complexity O(NM) worst case where N is the cardinality of the smallest set and M the number of sets*
    Return the members of a set resulting from the intersection of all
    thesets hold at the specified keys. Like in LRANGE the result is
    sent tothe client as a multi-bulk reply (see the protocol
    specification formore information). If just a single key is
    specified, then this commandproduces the same result as SMEMBERS.
    Actually SMEMBERS is just syntaxsugar for SINTERSECT.

    Non existing keys are considered like empty sets, so if one of the
    keys ismissing an empty set is returned (since the intersection
    with an emptyset always is an empty set).

Return value
------------

`Multi bulk reply <ReplyTypes.html>`_, specifically the list of
common elements.
.. |Redis Documentation| image:: redis.png