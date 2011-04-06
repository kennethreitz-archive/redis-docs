`|Redis Documentation| <index.html>`_
**HincrbyCommand: Contents**
  `HINCRBY \_key\_ \_field\_ \_value\_ (Redis > <#HINCRBY%20_key_%20_field_%20_value_%20(Redis%20%3E>`_
    `Examples <#Examples>`_
    `Return value <#Return%20value>`_
HincrbyCommand
==============

HINCRBY \_key\_ \_field\_ \_value\_ (Redis >
============================================

1.3.10)= *Time complexity: O(1)*
    Increment the number stored at *field* in the hash at *key* by
    *value*. If *key* does not exist, a new key holding a hash is
    created. If *field* does not exist or holds a string, the value is
    set to 0 before applying the operation.

    The range of values supported by HINCRBY is limited to 64 bit
    signed integers.

Examples
--------

Since the *value* argument is signed you can use this command to
perform both increments and decrements:
::

    HINCRBY key field 1 (increment by one)
    HINCRBY key field -1 (decrement by one, just like the DECR command)
    HINCRBY key field -10 (decrement by 10)

Return value
------------

`Integer reply <ReplyTypes.html>`_ The new value at *field* after
the increment operation.
.. |Redis Documentation| image:: redis.png