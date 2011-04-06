`|Redis Documentation| <index.html>`_
**MgetCommand: Contents**
  `MGET \_key1\_ \_key2\_ ... \_keyN\_ <#MGET%20_key1_%20_key2_%20...%20_keyN_>`_
    `Return value <#Return%20value>`_
    `Example <#Example>`_
MgetCommand
===========

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
MGET \_key1\_ \_key2\_ ... \_keyN\_
===================================

*Time complexity: O(1) for every key*
    Get the values of all the specified keys. If one or more keys dont
    existor is not of type String, a 'nil' value is returned instead of
    the valueof the specified key, but the operation never fails.

Return value
------------

`Multi bulk reply <ReplyTypes.html>`_
Example
-------

::

    $ ./redis-cli set foo 1000
    +OK
    $ ./redis-cli set bar 2000
    +OK
    $ ./redis-cli mget foo bar
    1. 1000
    2. 2000
    $ ./redis-cli mget foo bar nokey
    1. 1000
    2. 2000
    3. (nil)
    $ 

.. |Redis Documentation| image:: redis.png