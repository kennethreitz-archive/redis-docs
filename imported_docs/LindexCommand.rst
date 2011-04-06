`|Redis Documentation| <index.html>`_
**LindexCommand: Contents**
  `LINDEX \_key\_ \_index\_ <#LINDEX%20_key_%20_index_>`_
    `Return value <#Return%20value>`_
LindexCommand
=============

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
LINDEX \_key\_ \_index\_
========================

*Time complexity: O(n) (with n being the length of the list)*
    Return the specified element of the list stored at the
    specifiedkey. 0 is the first element, 1 the second and so on.
    Negative indexesare supported, for example -1 is the last element,
    -2 the penultimateand so on.

    If the value stored at key is not of list type an error is
    returned.If the index is out of range a 'nil' reply is returned.

    Note that even if the average time complexity is O(n) asking forthe
    first or the last element of the list is O(1).

Return value
------------

`Bulk reply <ReplyTypes.html>`_, specifically the requested
element.
.. |Redis Documentation| image:: redis.png