`|Redis Documentation| <index.html>`_
**ScardCommand: Contents**
  `SCARD \_key\_ <#SCARD%20_key_>`_
    `Return value <#Return%20value>`_
ScardCommand
============

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SCARD \_key\_
=============

*Time complexity O(1)*
    Return the set cardinality (number of elements). If the *key* does
    notexist 0 is returned, like for empty sets.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    the cardinality (number of elements) of the set as an integer.

.. |Redis Documentation| image:: redis.png