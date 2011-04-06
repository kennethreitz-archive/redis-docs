`|Redis Documentation| <index.html>`_
**ExistsCommand: Contents**
  `EXISTS \_key\_ <#EXISTS%20_key_>`_
    `Return value <#Return%20value>`_
ExistsCommand
=============

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
EXISTS \_key\_
==============

*Time complexity: O(1)*
    Test if the specified key exists. The command returns"0" if the key
    exists, otherwise "1" is returned.Note that even keys set with an
    empty string as value willreturn "1".

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the key exists.
    0 if the key does not exist.

.. |Redis Documentation| image:: redis.png