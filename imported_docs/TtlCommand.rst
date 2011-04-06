`|Redis Documentation| <index.html>`_
**TtlCommand: Contents**
  `TTL \_key\_ <#TTL%20_key_>`_
    `Return value <#Return%20value>`_
TtlCommand
==========

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
TTL \_key\_
===========

    The TTL command returns the remaining time to live in seconds of a
    key that has an `EXPIRE <ExpireCommand.html>`_ set. This
    introspection capability allows a Redis client to check how many
    seconds a given key will continue to be part of the dataset. If the
    Key does not exists or does not have an associated expire, -1 is
    returned.

Return value
------------

`Integer reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png