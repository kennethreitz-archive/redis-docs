`|Redis Documentation| <index.html>`_
**SremCommand: Contents**
  `SREM \_key\_ \_member\_ <#SREM%20_key_%20_member_>`_
    `Return value <#Return%20value>`_
SremCommand
===========

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SREM \_key\_ \_member\_
=======================

*Time complexity O(1)*
    Remove the specified *member* from the set value stored at *key*.
    If\_member\_ was not a member of the set no operation is performed.
    If *key*does not hold a set value an error is returned.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the new element was removed
    0 if the new element was not a member of the set

.. |Redis Documentation| image:: redis.png