`|Redis Documentation| <index.html>`_
**SaddCommand: Contents**
  `SADD \_key\_ \_member\_ <#SADD%20_key_%20_member_>`_
    `Return value <#Return%20value>`_
SaddCommand
===========

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SADD \_key\_ \_member\_
=======================

*Time complexity O(1)*
    Add the specified *member* to the set value stored at *key*. If
    *member*is already a member of the set no operation is performed.
    If *key*does not exist a new set with the specified *member* as
    sole member iscreated. If the key exists but does not hold a set
    value an error isreturned.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the new element was added
    0 if the element was already a member of the set

.. |Redis Documentation| image:: redis.png