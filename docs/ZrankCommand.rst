`|Redis Documentation| <index.html>`_
**ZrankCommand: Contents**
  `ZRANK \_key\_ \_member\_ (Redis > <#ZRANK%20_key_%20_member_%20(Redis%20%3E>`_
  `ZREVRANK \_key\_ \_member\_ (Redis > <#ZREVRANK%20_key_%20_member_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZrankCommand
============

ZRANK \_key\_ \_member\_ (Redis >
=================================

1.3.4) =
ZREVRANK \_key\_ \_member\_ (Redis >
====================================

1.3.4) = *Time complexity: O(log(N))*
    ZRANK returns the rank of the member in the sorted set, with scores
    ordered from low to high. ZREVRANK returns the rank with scores
    ordered from high to low. When the given member does not exist in
    the sorted set, the special value 'nil' is returned. The returned
    rank (or index) of the member is 0-based for both commands.

Return value
------------

`Integer reply <ReplyTypes.html>`_ or a nil
`bulk reply <ReplyTypes.html>`_, specifically:
::

    the rank of the element as an integer reply if the element exists.
    A nil bulk reply if there is no such element.

.. |Redis Documentation| image:: redis.png