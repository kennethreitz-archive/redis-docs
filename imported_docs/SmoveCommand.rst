`|Redis Documentation| <index.html>`_
**SmoveCommand: Contents**
  `SMOVE \_srckey\_ \_dstkey\_ \_member\_ <#SMOVE%20_srckey_%20_dstkey_%20_member_>`_
    `Return value <#Return%20value>`_
SmoveCommand
============

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
SMOVE \_srckey\_ \_dstkey\_ \_member\_
======================================

*Time complexity O(1)*
    Move the specifided *member* from the set at *srckey* to the set at
    *dstkey*.This operation is atomic, in every given moment the
    element will appear tobe in the source or destination set for
    accessing clients.

    If the source set does not exist or does not contain the specified
    elementno operation is performed and zero is returned, otherwise
    the element isremoved from the source set and added to the
    destination set. On successone is returned, even if the element was
    already present in the destinationset.

    An error is raised if the source or destination keys contain a non
    Set value.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the element was moved
    0 if the element was not found on the first set and no operation was performed

.. |Redis Documentation| image:: redis.png