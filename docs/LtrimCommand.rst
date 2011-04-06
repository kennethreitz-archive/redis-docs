`|Redis Documentation| <index.html>`_
**LtrimCommand: Contents**
  `LTRIM \_key\_ \_start\_ \_end\_ <#LTRIM%20_key_%20_start_%20_end_>`_
    `Return value <#Return%20value>`_
LtrimCommand
============

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
LTRIM \_key\_ \_start\_ \_end\_
===============================

*Time complexity: O(n) (with n being len of list - len of range)*
    Trim an existing list so that it will contain only the
    specifiedrange of elements specified. Start and end are zero-based
    indexes.0 is the first element of the list (the list head), 1 the
    next elementand so on.

    For example LTRIM foobar 0 2 will modify the list stored at
    foobarkey so that only the first three elements of the list will
    remain.

    \_start\_ and *end* can also be negative numbers indicating
    offsetsfrom the end of the list. For example -1 is the last element
    ofthe list, -2 the penultimate element and so on.

    Indexes out of range will not produce an error: if start is overthe
    end of the list, or start > end, an empty list is left as value.If
    end over the end of the list Redis will threat it just likethe last
    element of the list.

    Hint: the obvious use of LTRIM is together with LPUSH/RPUSH. For
    example:

::

            LPUSH mylist <someelement>
            LTRIM mylist 0 99

    The above two commands will push elements in the list taking care
    thatthe list will not grow without limits. This is very useful when
    usingRedis to store logs for example. It is important to note that
    when usedin this way LTRIM is an O(1) operation because in the
    average casejust one element is removed from the tail of the list.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png