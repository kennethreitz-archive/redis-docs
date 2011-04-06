`|Redis Documentation| <index.html>`_
**ZcardCommand: Contents**
  `ZCARD \_key\_ (Redis > <#ZCARD%20_key_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZcardCommand
============

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
ZCARD \_key\_ (Redis >
======================

1.1) = *Time complexity O(1)*
    Return the sorted set cardinality (number of elements). If the
    *key* does notexist 0 is returned, like for empty sorted sets.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    the cardinality (number of elements) of the set as an integer.

.. |Redis Documentation| image:: redis.png