`|Redis Documentation| <index.html>`_
**SubstrCommand: Contents**
  `SUBSTR \_key\_ \_start\_ \_end\_ <#SUBSTR%20_key_%20_start_%20_end_>`_
  `GETRANGE \_key\_ \_start\_ \_end\_ <#GETRANGE%20_key_%20_start_%20_end_>`_
    `Return value <#Return%20value>`_
    `Examples <#Examples>`_
SubstrCommand
=============

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
SUBSTR \_key\_ \_start\_ \_end\_
================================

GETRANGE \_key\_ \_start\_ \_end\_
==================================

*Time complexity: O(start+n) (with start being the start index and n the total length of the requested range). Note that the lookup part of this command is O(1) so for small strings this is actually an O(1) command.***Warning:**
this command was renamed into GETRANGE. SUBSTR will be taken as an
alias until the next major release of Redis.
    Return a subset of the string from offset *start* to offset
    *end*(both offsets are inclusive).Negative offsets can be used in
    order to provide an offset starting fromthe end of the string. So
    -1 means the last char, -2 the penultimate andso forth.

    The function handles out of range requests without raising an
    error, butjust limiting the resulting range to the actual length of
    the string.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
Examples
--------

::

    redis> set s "This is a string"
    OK
    redis> substr s 0 3
    "This"
    redis> substr s -3 -1
    "ing"
    redis> substr s 0 -1
    "This is a string"
    redis> substr s 9 100000
    " string"

.. |Redis Documentation| image:: redis.png