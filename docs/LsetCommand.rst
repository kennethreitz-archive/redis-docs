`|Redis Documentation| <index.html>`_
**LsetCommand: Contents**
  `LSET \_key\_ \_index\_ \_value\_ <#LSET%20_key_%20_index_%20_value_>`_
    `Return value <#Return%20value>`_
LsetCommand
===========

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
LSET \_key\_ \_index\_ \_value\_
================================

*Time complexity: O(N) (with N being the length of the list)*
    Set the list element at *index* (see LINDEX for information about
    the\_index\_ argument) with the new *value*. Out of range indexes
    willgenerate an error. Note that setting the first or last elements
    ofthe list is O(1).

    Similarly to other list commands accepting indexes, the index can
    be negative to access elements starting from the end of the list.
    So -1 is the last element, -2 is the penultimate, and so forth.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png