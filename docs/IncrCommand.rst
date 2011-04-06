`|Redis Documentation| <index.html>`_
**IncrCommand: Contents**
  `INCR \_key\_ <#INCR%20_key_>`_
  `INCRBY \_key\_ \_integer\_ <#INCRBY%20_key_%20_integer_>`_
  `DECR \_key\_ \_integer\_ <#DECR%20_key_%20_integer_>`_
  `DECRBY \_key\_ \_integer\_ <#DECRBY%20_key_%20_integer_>`_
    `Return value <#Return%20value>`_
IncrCommand
===========

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
INCR \_key\_
============

INCRBY \_key\_ \_integer\_
==========================

DECR \_key\_ \_integer\_
========================

DECRBY \_key\_ \_integer\_
==========================

*Time complexity: O(1)*
    Increment or decrement the number stored at *key* by one. If the
    key doesnot exist or contains a value of a wrong type, set the key
    to thevalue of "0" before to perform the increment or decrement
    operation.

    INCRBY and DECRBY work just like INCR and DECR but instead
    toincrement/decrement by 1 the increment/decrement is *integer*.

    INCR commands are limited to 64 bit signed integers.

Note: this is actually a string operation, that is, in Redis there
are not "integer" types. Simply the string stored at the key is
parsed as a base 10 64 bit signed integer, incremented, and then
converted back as a string.
Return value
------------

`Integer reply <ReplyTypes.html>`_, this commands will reply with
the new value of *key* after the increment or decrement.
.. |Redis Documentation| image:: redis.png