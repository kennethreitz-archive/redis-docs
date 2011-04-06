`|Redis Documentation| <index.html>`_
**HgetCommand: Contents**
  `HGET \_key\_ \_field\_ (Redis > <#HGET%20_key_%20_field_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
HgetCommand
===========

ï»¿#sidebar `HashCommandsSidebar <HashCommandsSidebar.html>`_
HGET \_key\_ \_field\_ (Redis >
===============================

1.3.10)= *Time complexity: O(1)*
    If *key* holds a hash, retrieve the value associated to the
    specified *field*.

    If the *field* is not found or the *key* does not exist, a special
    'nil' value is returned.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png