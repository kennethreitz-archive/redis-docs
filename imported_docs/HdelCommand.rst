`|Redis Documentation| <index.html>`_
**HdelCommand: Contents**
  `HDEL \_key\_ \_field\_ (Redis > <#HDEL%20_key_%20_field_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
HdelCommand
===========

ï»¿#sidebar `HashCommandsSidebar <HashCommandsSidebar.html>`_
HDEL \_key\_ \_field\_ (Redis >
===============================

1.3.10)= *Time complexity: O(1)*
    Remove the specified *field* from an hash stored at *key*.

    If the *field* was present in the hash it is deleted and 1 is
    returned, otherwise 0 is returned and no operation is performed.

Return value
------------

`Integer reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png