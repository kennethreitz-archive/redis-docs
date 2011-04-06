`|Redis Documentation| <index.html>`_
**SetbitCommand: Contents**
  `SETBIT \_key\_ \_offset\_ \_value\_ (Redis > <#SETBIT%20_key_%20_offset_%20_value_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
SetbitCommand
=============

SETBIT \_key\_ \_offset\_ \_value\_ (Redis >
============================================

2.1.8) = *Time complexity: O(1)*
    Sets or clears the bit at *offset* in the string value stored at
    *key*.

The bit is either set or cleared depending on *value*, which can be
either 0 or 1. When *key* does not exist, a new string value is
created. The string is grown to make sure it can hold a bit at
*offset*. The *offset* argument is required to be greater than or
equal to 0, and is limited to
2\ :sup:`32-1 (which limits bitmaps to 512MB). When the string at *key* is grown, added bits are set to 0.**Warning**: When setting the last possible bit (*offset* equal to 2`\ 32-1)
and the string value stored at *key* does not yet hold a string
value, or holds a small string value, Redis needs to allocate all
intermediate memory which can block the server for some time. On a
2010 Macbook Pro, setting bit number
2\ :sup:`32-1 (512MB allocation) takes ~300ms, setting bit number 2`\ 30-1
(128MB allocation) takes ~80ms, setting bit number
2\ :sup:`28-1 (32MB allocation) takes ~30ms and setting bit number 2`\ 26-1
(8MB allocation) takes ~8ms. Note that once this first allocation
is done, subsequent calls to SETBIT for the same *key* will not
have the allocation overhead.
Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically: the original bit
value stored at *offset*.
.. |Redis Documentation| image:: redis.png