`|Redis Documentation| <index.html>`_
**ZscoreCommand: Contents**
  `ZSCORE \_key\_ \_element\_ (Redis > <#ZSCORE%20_key_%20_element_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZscoreCommand
=============

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
ZSCORE \_key\_ \_element\_ (Redis >
===================================

1.1) = *Time complexity O(1)*
    Return the score of the specified element of the sorted set at
    key.If the specified element does not exist in the sorted set, or
    the keydoes not exist at all, a special 'nil' value is returned.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
::

    the score (a double precision floating point number) represented as string.

.. |Redis Documentation| image:: redis.png