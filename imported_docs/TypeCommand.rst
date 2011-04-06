`|Redis Documentation| <index.html>`_
**TypeCommand: Contents**
  `TYPE \_key\_ <#TYPE%20_key_>`_
    `Return value <#Return%20value>`_
    `See also <#See%20also>`_
TypeCommand
===========

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
TYPE \_key\_
============

*Time complexity: O(1)*
    Return the type of the value stored at *key* in form of astring.
    The type can be one of "none", "string", "list", "set"."none" is
    returned if the key does not exist.

Return value
------------

`Status code reply <ReplyTypes.html>`_, specifically:
::

    "none" if the key does not exist
    "string" if the key contains a String value
    "list" if the key contains a List value
    "set" if the key contains a Set value
    "zset" if the key contains a Sorted Set value
    "hash" if the key contains a Hash value

See also
--------


-  `Redis Data Types <DataTypes.html>`_

.. |Redis Documentation| image:: redis.png