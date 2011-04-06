`|Redis Documentation| <index.html>`_
**Speed: Contents**
  `Speed (ROUGH DRAFT) <#Speed%20(ROUGH%20DRAFT)>`_
    `TODO <#TODO>`_
Speed
=====

Speed (ROUGH DRAFT)
===================

TODO
----


-  Written in ANSI C
-  Pipelining
-  MultiBulkCommands
-  epoll >= 1.1
-  Benchmarks

Redis takes the whole dataset in memory and
`writes asynchronously to disk <Persistence.html>`_ in order to be
very fast, you have the best of both worlds: hyper-speed and
`persistence <Persistence.html>`_ for your data.
Establishing a new connection to a Redis Server is *simple* and
*fast* nothing more that a TCP three way handshake. There is no
authentication or other handshake involved
(`Google Group: Can we use connection pool in Redis? <http://groups.google.com/group/redis-db/browse_thread/thread/1adb93f0b6a1460a>`_)
You can read more about the way Redis clients communicate with
servers in the
`Protocol Specification <ProtocolSpecification.html>`_.
On most commodity hardware it takes about 45 seconds to restore a 2
GB database, without fancy RAID. This can give you some kind of
feeling about the order of magnitude of the time needed to load
data when you restart the server, so restarting a server is fast
too.
Also `Replication <Replication.html>`_ is fast, benchamarks will
give you the the same order of magnitude a restart does
(`Google Group: Replication speed benchmak <http://groups.google.com/group/redis-db/browse_thread/thread/3ab1c8b2126f1b8/29bdb6c5973f0388?lnk=gst&q=replication+#29bdb6c5973f0388>`_)
.. |Redis Documentation| image:: redis.png