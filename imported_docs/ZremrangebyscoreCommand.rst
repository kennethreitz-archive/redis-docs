`|Redis Documentation| <index.html>`_
**ZremrangebyscoreCommand: Contents**
  `ZREMRANGEBYSCORE \_key\_ \_min\_ \_max\_ (Redis > <#ZREMRANGEBYSCORE%20_key_%20_min_%20_max_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZremrangebyscoreCommand
=======================

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
ZREMRANGEBYSCORE \_key\_ \_min\_ \_max\_ (Redis >
=================================================

1.1) =
*Time complexity: O(log(N))+O(M) with N being the number of elements in the sorted set and M the number of elements removed by the operation*
    Remove all the elements in the sorted set at key with a score
    between\_min\_ and *max* (including elements with score equal to
    min or max).

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically the number of
elements removed.
.. |Redis Documentation| image:: redis.png