`|Redis Documentation| <index.html>`_
**HgetallCommand: Contents**
  `HKEYS \_key\_ (Redis > <#HKEYS%20_key_%20(Redis%20%3E>`_
  `HVALS \_key\_ (Redis > <#HVALS%20_key_%20(Redis%20%3E>`_
  `HGETALL \_key\_ (Redis > <#HGETALL%20_key_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
HgetallCommand
==============

ï»¿#sidebar `HashCommandsSidebar <HashCommandsSidebar.html>`_
HKEYS \_key\_ (Redis >
======================

1.3.10)=
HVALS \_key\_ (Redis >
======================

1.3.10)=
HGETALL \_key\_ (Redis >
========================

1.3.10)=
*Time complexity: O(N), where N is the total number of fields in the hash*
    HKEYS returns all the fields names contained into a hash, HVALS all
    the associated values, while HGETALL returns both the fields and
    values in the form of *field1*, *value1*, *field2*, *value2*, ...,
    *fieldN*, *valueN*.

Return value
------------

`Multi Bulk Reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png