`|Redis Documentation| <index.html>`_
**RandomkeyCommand: Contents**
  `RANDOMKEY <#RANDOMKEY>`_
    `Return value <#Return%20value>`_
RandomkeyCommand
================

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
RANDOMKEY
=========

*Time complexity: O(1)*
    Return a randomly selected key from the currently selected DB.

Return value
------------

`Singe line reply <ReplyTypes.html>`_, specifically the randomly
selected key or an empty string is the database is empty.
.. |Redis Documentation| image:: redis.png