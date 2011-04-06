`|Redis Documentation| <index.html>`_
**Pipelining: Contents**
  `Pipelining (DRAFT) <#Pipelining%20(DRAFT)>`_
Pipelining
==========

Pipelining (DRAFT)
==================

A client library can use the same connection in order to issue
multiple commands. But Redis supports **pipelining**, so multiple
commands can be sent to the server with a single write operation by
the client, without need to read the server reply in order to issue
the next command. All the replies can be read at the end.
Usually Redis server and client will have a very fast link so this
is not very important to support this feature in a client
implementation, still if an application needs to issue a very large
number of commands in s short time, using pipelining can be much
faster.
Please read the
`ProtocolSpecification <ProtocolSpecification.html>`_ if you want
to learn more about the way Redis
`clients <SupportedLanguages.html>`_ and the server communicate.
Pipelining is one of the `Speed <Speed.html>`_
`Features <Features.html>`_ of Redis, you can also check the
support for
`send and receive multiple values in a single command <MultiBulkCommands.html>`_.
.. |Redis Documentation| image:: redis.png