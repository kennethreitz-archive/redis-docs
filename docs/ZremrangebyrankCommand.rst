`|Redis Documentation| <index.html>`_
**ZremrangebyrankCommand: Contents**
  `ZREMRANGEBYRANK \_key\_ \_start\_ \_end\_ (Redis > <#ZREMRANGEBYRANK%20_key_%20_start_%20_end_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZremrangebyrankCommand
======================

ZREMRANGEBYRANK \_key\_ \_start\_ \_end\_ (Redis >
==================================================

1.3.4) =
*Time complexity: O(log(N))+O(M) with N being the number of elements in the sorted set and M the number of elements removed by the operation*
    Remove all elements in the sorted set at *key* with rank between
    *start* and *end*. Start and end are 0-based with rank 0 being the
    element with the lowest score. Both start and end can be negative
    numbers, where they indicate offsets starting at the element with
    the highest rank. For example: -1 is the element with the highest
    score, -2 the element with the second highest score and so forth.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically the number of
elements removed.
.. |Redis Documentation| image:: redis.png