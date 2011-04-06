`|Redis Documentation| <index.html>`_
**GetCommand: Contents**
  `GET \_key\_ <#GET%20_key_>`_
    `Return value <#Return%20value>`_
GetCommand
==========

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
GET \_key\_
===========

*Time complexity: O(1)*
    Get the value of the specified key. If the keydoes not exist the
    special value 'nil' is returned.If the value stored at *key* is not
    a string an erroris returned because GET can only handle string
    values.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png