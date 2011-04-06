`|Redis Documentation| <index.html>`_
**ZremCommand: Contents**
  `ZREM \_key\_ \_member\_ (Redis > <#ZREM%20_key_%20_member_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZremCommand
===========

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
ZREM \_key\_ \_member\_ (Redis >
================================

1.1) =
*Time complexity O(log(N)) with N being the number of elements in the sorted set*
    Remove the specified *member* from the sorted set value stored at
    *key*. If\_member\_ was not a member of the set no operation is
    performed. If *key*does not not hold a set value an error is
    returned.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the new element was removed
    0 if the new element was not a member of the set

.. |Redis Documentation| image:: redis.png