`|Redis Documentation| <index.html>`_
**GetbitCommand: Contents**
  `GETBIT \_key\_ \_offset\_ (Redis > <#GETBIT%20_key_%20_offset_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
GetbitCommand
=============

GETBIT \_key\_ \_offset\_ (Redis >
==================================

2.1.8) = *Time complexity: O(1)*
    Returns the bit value at *offset* in the string value stored at
    *key*.

When *offset* is beyond the string length, the string is assumed to
be a contiguous space with 0 bits. When *key* does not exist it is
assumed to be an empty string, so *offset* is always out of range
and the value is also assumed to be a contiguous space with 0 bits.
Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically: the bit value
stored at *offset*.
.. |Redis Documentation| image:: redis.png