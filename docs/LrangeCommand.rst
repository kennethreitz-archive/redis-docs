`|Redis Documentation| <index.html>`_
**LrangeCommand: Contents**
  `LRANGE \_key\_ \_start\_ \_end\_ <#LRANGE%20_key_%20_start_%20_end_>`_
    `Consistency with range functions in various programming languages <#Consistency%20with%20range%20functions%20in%20various%20programming%20languages>`_
    `Out-of-range indexes <#Out-of-range%20indexes>`_
    `Return value <#Return%20value>`_
LrangeCommand
=============

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
LRANGE \_key\_ \_start\_ \_end\_
================================

*Time complexity: O(start+n) (with n being the length of the range and start being the start offset)*Return
the specified elements of the list stored at the specified key.
Start and end are zero-based indexes. 0 is the first element of the
list (the list head), 1 the next element and so on.
For example LRANGE foobar 0 2 will return the first three elements
of the list.
*start* and *end* can also be negative numbers indicating offsets
from the end of the list. For example -1 is the last element of the
list, -2 the penultimate element and so on.
Consistency with range functions in various programming languages
-----------------------------------------------------------------

Note that if you have a list of numbers from 0 to 100, LRANGE 0 10
will return 11 elements, that is, rightmost item is included. This
**may or may not** be consistent with behavior of range-related
functions in your programming language of choice (think Ruby's
Range.new, Array#slice or Python's range() function).
LRANGE behavior is consistent with one of Tcl.
Out-of-range indexes
--------------------

Indexes out of range will not produce an error: if start is over
the end of the list, or start ``>`` end, an empty list is returned.
If end is over the end of the list Redis will threat it just like
the last element of the list.
Return value
------------

`Multi bulk reply <ReplyTypes.html>`_, specifically a list of
elements in the specified range.
.. |Redis Documentation| image:: redis.png