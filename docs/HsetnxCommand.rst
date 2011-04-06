`|Redis Documentation| <index.html>`_
**HsetnxCommand: Contents**
  `HSETNX \_key\_ \_field\_ \_value\_ (Redis > <#HSETNX%20_key_%20_field_%20_value_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
HsetnxCommand
=============

HSETNX \_key\_ \_field\_ \_value\_ (Redis >
===========================================

1.3.10)= *Time complexity: O(1)*
    Set the specified hash *field* to the specified *value*, if *field*
    does not exist yet.

    If *key* does not exist, a new key holding a hash is created.

    If the field already exists, this operation has no effect and
    returns 0.Otherwise, the field is set to *value* and the operation
    returns 1.

Return value
------------

`Integer reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png