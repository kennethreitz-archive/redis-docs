`|Redis Documentation| <index.html>`_
**GetsetCommand: Contents**
  `GETSET \_key\_ \_value\_ <#GETSET%20_key_%20_value_>`_
    `Return value <#Return%20value>`_
    `Design patterns <#Design%20patterns>`_
GetsetCommand
=============

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
GETSET \_key\_ \_value\_
========================

*Time complexity: O(1)*
    GETSET is an atomic *set this value and return the old value*
    command.Set *key* to the string *value* and return the old value
    stored at *key*.The string can't be longer than 1073741824 bytes (1
    GB).

Return value
------------

`Bulk reply <ReplyTypes.html>`_
Design patterns
---------------

    GETSET can be used together with INCR for counting with atomic
    reset whena given condition arises. For example a process may call
    INCR against thekey *mycounter* every time some event occurred, but
    from time totime we need to get the value of the counter and reset
    it to zero atomicallyusing ``GETSET mycounter 0``.

.. |Redis Documentation| image:: redis.png