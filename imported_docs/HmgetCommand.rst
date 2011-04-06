`|Redis Documentation| <index.html>`_
**HmgetCommand: Contents**
  `HMGET \_key\_ \_field1\_ ... \_fieldN\_ (Redis > <#HMGET%20_key_%20_field1_%20...%20_fieldN_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
HmgetCommand
============

ï»¿#sidebar `HashCommandsSidebar <HashCommandsSidebar.html>`_
HMGET \_key\_ \_field1\_ ... \_fieldN\_ (Redis >
================================================

1.3.10) =
*Time complexity: O(N) (with N being the number of fields)*
    Retrieve the values associated to the specified *fields*.

    If some of the specified *fields* do not exist, nil values are
    returned.Non existing keys are considered like empty hashes.

Return value
------------

`Multi Bulk Reply <ReplyTypes.html>`_ specifically a list of all
the values associated with the specified fields, in the same order
of the request.
.. |Redis Documentation| image:: redis.png