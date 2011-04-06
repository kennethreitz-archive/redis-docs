`|Redis Documentation| <index.html>`_
**SismemberCommand: Contents**
  `SISMEMBER \_key\_ \_member\_ <#SISMEMBER%20_key_%20_member_>`_
    `Return value <#Return%20value>`_
SismemberCommand
================

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SISMEMBER \_key\_ \_member\_
============================

*Time complexity O(1)*
    Return 1 if *member* is a member of the set stored at *key*,
    otherwise0 is returned.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the element is a member of the set
    0 if the element is not a member of the set OR if the key does not exist

.. |Redis Documentation| image:: redis.png