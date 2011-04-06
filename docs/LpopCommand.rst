`|Redis Documentation| <index.html>`_
**LpopCommand: Contents**
  `LPOP \_key\_ <#LPOP%20_key_>`_
  `RPOP \_key\_ <#RPOP%20_key_>`_
    `Return value <#Return%20value>`_
LpopCommand
===========

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
LPOP \_key\_
============

RPOP \_key\_
============

*Time complexity: O(1)*
    Atomically return and remove the first (LPOP) or last (RPOP)
    elementof the list. For example if the list contains the elements
    "a","b","c" LPOPwill return "a" and the list will become "b","c".

    If the *key* does not exist or the list is already empty the
    specialvalue 'nil' is returned.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png