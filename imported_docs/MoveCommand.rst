`|Redis Documentation| <index.html>`_
**MoveCommand: Contents**
  `MOVE \_key\_ \_dbindex\_ <#MOVE%20_key_%20_dbindex_>`_
    `Return value <#Return%20value>`_
MoveCommand
===========

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
MOVE \_key\_ \_dbindex\_
========================

    Move the specified key from the currently selected DB to the
    specifieddestination DB. Note that this command returns 1 only if
    the key wassuccessfully moved, and 0 if the target key was already
    there or if thesource key was not found at all, so it is possible
    to use MOVE as a lockingprimitive.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the key was moved
    0 if the key was not moved because already present on the target DB or was not found in the current DB.

.. |Redis Documentation| image:: redis.png