`|Redis Documentation| <index.html>`_
**SlaveofCommand: Contents**
  `SLAVEOF \_host\_ \_port\_ <#SLAVEOF%20_host_%20_port_>`_
  `SLAVEOF no one <#SLAVEOF%20no%20one>`_
    `Return value <#Return%20value>`_
SlaveofCommand
==============

ï»¿#sidebar `ControlCommandsSidebar <ControlCommandsSidebar.html>`_
SLAVEOF \_host\_ \_port\_
=========================

SLAVEOF no one
==============

    The SLAVEOF command can change the replication settings of a slave
    on the fly.If a Redis server is arleady acting as slave, the
    command ``SLAVEOF NO ONE``will turn off the replicaiton turning the
    Redis server into a MASTER.In the proper form
    ``SLAVEOF hostname port`` will make the server a slave of
    thespecific server listening at the specified hostname and port.

    If a server is already a slave of some master,
    ``SLAVEOF hostname port`` willstop the replication against the old
    server and start the synchrnonizationagainst the new one discarding
    the old dataset.

    The form ``SLAVEOF no one`` will stop replication turning the
    server into aMASTER but will not discard the replication. So if the
    old master stop workingit is possible to turn the slave into a
    master and set the application touse the new master in read/write.
    Later when the other Redis server will befixed it can be configured
    in order to work as slave.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png