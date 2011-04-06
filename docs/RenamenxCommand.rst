`|Redis Documentation| <index.html>`_
**RenamenxCommand: Contents**
  `RENAMENX \_oldkey\_ \_newkey\_ <#RENAMENX%20_oldkey_%20_newkey_>`_
    `Return value <#Return%20value>`_
RenamenxCommand
===============

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
RENAMENX \_oldkey\_ \_newkey\_
==============================

*Time complexity: O(1)*
    Rename *oldkey* into *newkey* but fails if the destination key
    *newkey* already exists.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the key was renamed
    0 if the target key already exist

.. |Redis Documentation| image:: redis.png