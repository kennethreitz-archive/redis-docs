`|Redis Documentation| <index.html>`_
**RenameCommand: Contents**
  `RENAME \_oldkey\_ \_newkey\_ <#RENAME%20_oldkey_%20_newkey_>`_
    `Return value <#Return%20value>`_
RenameCommand
=============

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
RENAME \_oldkey\_ \_newkey\_
============================

*Time complexity: O(1)*
    Atomically renames the key *oldkey* to *newkey*. If the source
    anddestination name are the same an error is returned. If
    *newkey*already exists it is overwritten.

Return value
------------

`Status code repy <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png