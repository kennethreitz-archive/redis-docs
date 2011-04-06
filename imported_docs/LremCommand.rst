`|Redis Documentation| <index.html>`_
**LremCommand: Contents**
  `LREM \_key\_ \_count\_ \_value\_ <#LREM%20_key_%20_count_%20_value_>`_
    `Return value <#Return%20value>`_
LremCommand
===========

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
LREM \_key\_ \_count\_ \_value\_
================================

*Time complexity: O(N) (with N being the length of the list)*
    Remove the first *count* occurrences of the *value* element from
    the list.If *count* is zero all the elements are removed. If
    *count* is negativeelements are removed from tail to head, instead
    to go from head to tailthat is the normal behaviour. So for example
    LREM with count -2 and\_hello\_ as value to remove against the list
    (a,b,c,hello,x,hello,hello) willlave the list (a,b,c,hello,x). The
    number of removed elements is returnedas an integer, see below for
    more information about the returned value.Note that non existing
    keys are considered like empty lists by LREM, so LREMagainst non
    existing keys will always return 0.

Return value
------------

`Integer Reply <ReplyTypes.html>`_, specifically:
::

    The number of removed elements if the operation succeeded

.. |Redis Documentation| image:: redis.png