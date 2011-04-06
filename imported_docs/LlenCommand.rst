`|Redis Documentation| <index.html>`_
**LlenCommand: Contents**
  `LLEN \_key\_ <#LLEN%20_key_>`_
    `Return value <#Return%20value>`_
LlenCommand
===========

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
LLEN \_key\_
============

*Time complexity: O(1)*
    Return the length of the list stored at the specified key. If
    thekey does not exist zero is returned (the same behaviour as
    forempty lists). If the value stored at *key* is not a list an
    error is returned.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    The length of the list.

.. |Redis Documentation| image:: redis.png