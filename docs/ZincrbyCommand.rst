`|Redis Documentation| <index.html>`_
**ZincrbyCommand: Contents**
  `ZINCRBY \_key\_ \_increment\_ \_member\_ (Redis > <#ZINCRBY%20_key_%20_increment_%20_member_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZincrbyCommand
==============

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
ZINCRBY \_key\_ \_increment\_ \_member\_ (Redis >
=================================================

1.1) =
*Time complexity O(log(N)) with N being the number of elements in the sorted set*
    If *member* already exists in the sorted set adds the *increment*
    to its scoreand updates the position of the element in the sorted
    set accordingly.If *member* does not already exist in the sorted
    set it is added with\_increment\_ as score (that is, like if the
    previous score was virtually zero).If *key* does not exist a new
    sorted set with the specified\_member\_ as sole member is crated.
    If the key exists but does not hold asorted set value an error is
    returned.

    The score value can be the string representation of a double
    precision floatingpoint number. It's possible to provide a negative
    value to perform a decrement.

    For an introduction to sorted sets check the
    `Introduction to Redis data types <IntroductionToRedisDataTypes.html>`_
    page.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
::

    The new score (a double precision floating point number) represented as string.

.. |Redis Documentation| image:: redis.png