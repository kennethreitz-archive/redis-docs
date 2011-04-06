`|Redis Documentation| <index.html>`_
**RpushCommand: Contents**
      `RPUSH \_key\_ \_string\_ <#RPUSH%20_key_%20_string_>`_
      `LPUSH \_key\_ \_string\_ <#LPUSH%20_key_%20_string_>`_
    `Return value <#Return%20value>`_
RpushCommand
============

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
RPUSH \_key\_ \_string\_
~~~~~~~~~~~~~~~~~~~~~~~~

LPUSH \_key\_ \_string\_
~~~~~~~~~~~~~~~~~~~~~~~~

*Time complexity: O(1)*
    Add the *string* value to the head (LPUSH) or tail (RPUSH) of the
    liststored at *key*. If the key does not exist an empty list is
    created just beforethe append operation. If the key exists but is
    not a List an erroris returned.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically, the number of
elements inside the list after the push operation.
.. |Redis Documentation| image:: redis.png