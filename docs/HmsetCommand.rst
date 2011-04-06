`|Redis Documentation| <index.html>`_
**HmsetCommand: Contents**
  `HMSET \_key\_ \_field1\_ \_value1\_ ... \_fieldN\_ \_valueN\_ (Redis > <#HMSET%20_key_%20_field1_%20_value1_%20...%20_fieldN_%20_valueN_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
HmsetCommand
============

HMSET \_key\_ \_field1\_ \_value1\_ ... \_fieldN\_ \_valueN\_ (Redis >
======================================================================

1.3.10) =
*Time complexity: O(N) (with N being the number of fields)*
    Set the respective fields to the respective values. HMSET replaces
    old values with new values.

    If *key* does not exist, a new key holding a hash is created.

Return value
------------

`Status code reply <ReplyTypes.html>`_ Always +OK because HMSET
can't fail
.. |Redis Documentation| image:: redis.png