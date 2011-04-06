`|Redis Documentation| <index.html>`_
**ZaddCommand: Contents**
  `ZADD \_key\_ \_score\_ \_member\_ (Redis > <#ZADD%20_key_%20_score_%20_member_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZaddCommand
===========

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
ZADD \_key\_ \_score\_ \_member\_ (Redis >
==========================================

1.1) =
*Time complexity O(log(N)) with N being the number of elements in the sorted set*
    Add the specified *member* having the specifeid *score* to the
    sortedset stored at *key*. If *member* is already a member of the
    sorted setthe score is updated, and the element reinserted in the
    right position toensure sorting. If *key* does not exist a new
    sorted set with the specified\_member\_ as sole member is crated.
    If the key exists but does not hold asorted set value an error is
    returned.

    The score value can be the string representation of a double
    precision floatingpoint number.

    For an introduction to sorted sets check the
    `Introduction to Redis data types <IntroductionToRedisDataTypes.html>`_
    page.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the new element was added
    0 if the element was already a member of the sorted set and the score was updated

.. |Redis Documentation| image:: redis.png