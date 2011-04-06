`|Redis Documentation| <index.html>`_
**AppendCommand: Contents**
  `APPEND \_key\_ \_value\_ <#APPEND%20_key_%20_value_>`_
    `Return value <#Return%20value>`_
    `Examples <#Examples>`_
AppendCommand
=============

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
APPEND \_key\_ \_value\_
========================

*Time complexity: O(1). The amortized time complexity is O(1) assuming the appended value is small and the already present value is of any size, since the dynamic string library used by Redis will double the free space available on every reallocation.*
    If the *key* already exists and is a string, this command appends
    theprovided value at the end of the string.If the *key* does not
    exist it is created and set as an empty string, soAPPEND will be
    very similar to SET in this special case.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically the total length
of the string after the append operation.
Examples
--------

::

    redis> exists mykey
    (integer) 0
    redis> append mykey "Hello "
    (integer) 6
    redis> append mykey "World"
    (integer) 11
    redis> get mykey
    "Hello World"

.. |Redis Documentation| image:: redis.png