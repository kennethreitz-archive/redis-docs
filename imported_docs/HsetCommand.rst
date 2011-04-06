`|Redis Documentation| <index.html>`_
**HsetCommand: Contents**
  `HSET \_key\_ \_field\_ \_value\_ (Redis > <#HSET%20_key_%20_field_%20_value_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
HsetCommand
===========

ï»¿#sidebar `HashCommandsSidebar <HashCommandsSidebar.html>`_
HSET \_key\_ \_field\_ \_value\_ (Redis >
=========================================

1.3.10)= *Time complexity: O(1)*
    Set the specified hash *field* to the specified *value*.

    If *key* does not exist, a new key holding a hash is created.

    If the field already exists, and the HSET just produced an update
    of thevalue, 0 is returned, otherwise if a new field is created 1
    is returned.

Return value
------------

`Integer reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png