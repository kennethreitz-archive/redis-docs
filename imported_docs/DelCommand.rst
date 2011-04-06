`|Redis Documentation| <index.html>`_
**DelCommand: Contents**
  `DEL \_key1\_ \_key2\_ ... \_keyN\_ <#DEL%20_key1_%20_key2_%20...%20_keyN_>`_
    `Return value <#Return%20value>`_
DelCommand
==========

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
DEL \_key1\_ \_key2\_ ... \_keyN\_
==================================

*Time complexity: O(1)*
    Remove the specified keys. If a given key does not existno
    operation is performed for this key. The command returns the number
    ofkeys removed.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    an integer greater than 0 if one or more keys were removed
    0 if none of the specified key existed

.. |Redis Documentation| image:: redis.png