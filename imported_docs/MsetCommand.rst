`|Redis Documentation| <index.html>`_
**MsetCommand: Contents**
  `MSET \_key1\_ \_value1\_ \_key2\_ \_value2\_ ... \_keyN\_ \_valueN\_ (Redis > <#MSET%20_key1_%20_value1_%20_key2_%20_value2_%20...%20_keyN_%20_valueN_%20(Redis%20%3E>`_
  `MSETNX \_key1\_ \_value1\_ \_key2\_ \_value2\_ ... \_keyN\_ \_valueN\_ (Redis > <#MSETNX%20_key1_%20_value1_%20_key2_%20_value2_%20...%20_keyN_%20_valueN_%20(Redis%20%3E>`_
    `MSET Return value <#MSET%20Return%20value>`_
    `MSETNX Return value <#MSETNX%20Return%20value>`_
MsetCommand
===========

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
MSET \_key1\_ \_value1\_ \_key2\_ \_value2\_ ... \_keyN\_ \_valueN\_ (Redis >
=============================================================================

1.1) =
MSETNX \_key1\_ \_value1\_ \_key2\_ \_value2\_ ... \_keyN\_ \_valueN\_ (Redis >
===============================================================================

1.1) = *Time complexity: O(1) to set every key*
    Set the the respective keys to the respective values. MSET will
    replace oldvalues with new values, while MSETNX will not perform
    any operation at alleven if just a single key already exists.

    Because of this semantic MSETNX can be used in order to set
    different keysrepresenting different fields of an unique logic
    object in a way thatensures that either all the fields or none at
    all are set.

    Both MSET and MSETNX are atomic operations. This means that for
    instanceif the keys A and B are modified, another client talking to
    Redis can eithersee the changes to both A and B at once, or no
    modification at all.

MSET Return value
-----------------

`Status code reply <ReplyTypes.html>`_ Basically +OK as MSET can't
fail
MSETNX Return value
-------------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1 if the all the keys were set
    0 if no key was set (at least one key already existed)

.. |Redis Documentation| image:: redis.png