`|Redis Documentation| <index.html>`_
**Redis\_2\_0\_Whats\_new: Contents**
  `Redis 2.0: What's new? <#Redis%202.0:%20What's%20new?>`_
      `MULTI/EXEC <#MULTI/EXEC>`_
      `Blocking pop <#Blocking%20pop>`_
      `Publish/subscribe <#Publish/subscribe>`_
      `Hashes <#Hashes>`_
      `Virtual Memory <#Virtual%20Memory>`_
    `Contributors <#Contributors>`_
Redis\_2\_0\_Whats\_new
=======================

Redis 2.0: What's new?
======================

The release of Redis 2.0 marks a major milestone in Redis
development. Apart from an endless list of new features, there are
some major ones that deserve to be highlighted.
MULTI/EXEC
~~~~~~~~~~

The MULTI/EXEC family of commands were added to fulfill the need to
execute multiple commands as a single atomic block. Because all
commands inside a MULTI/EXEC block are serialized and executed
sequentially, it is not possible that another client request is
served in the middle of executing this block. All commands are
executed one after the other when EXEC is called, which makes sure
either **all** or **no** commands are executed, independent of the
state of the client connection.
More on MULTI/EXEC:

-  `http://code.google.com/p/redis/wiki/MultiExecCommand <http://code.google.com/p/redis/wiki/MultiExecCommand>`_

Blocking pop
~~~~~~~~~~~~

The commands BLPOP and BRPOP were added to support popping from a
list in a blocking fashion. This means the client connection will
be blocked for a certain amount of time until another client pushes
an item on a list. These commands are frequently used in
producer/consumer scenarios.
More on blocking pop:

-  `http://code.google.com/p/redis/wiki/BlpopCommand <http://code.google.com/p/redis/wiki/BlpopCommand>`_

Publish/subscribe
~~~~~~~~~~~~~~~~~

The family of publish/subscribe commands let clients publish
messages onto channels and subscribe to receive all messages that
are published on channels. Also included are commands to receive
all messages for which the channel matches a given pattern.
More on publish/subscribe:

-  `http://code.google.com/p/redis/wiki/PublishSubscribe <http://code.google.com/p/redis/wiki/PublishSubscribe>`_
-  `http://antirez.com/post/redis-weekly-update-3-publish-submit.html <http://antirez.com/post/redis-weekly-update-3-publish-submit.html>`_
-  `http://rediscookbook.org/pubsub\_for\_asynchronous\_communication.html <http://rediscookbook.org/pubsub_for_asynchronous_communication.html>`_

Hashes
~~~~~~

This new datatype allows to store multiple key/value pairs on a
single key. Together with the list of regular commands you would
expect for such a datatype (HSET, HGET, HDEL, HLEN, HKEYS, ...), it
is also possible to use the values *inside* a hash for any SORT
operation.
More on hashes:

-  `http://code.google.com/p/redis/wiki/HsetCommand <http://code.google.com/p/redis/wiki/HsetCommand>`_
-  `http://antirez.com/post/redis-weekly-update-1.html <http://antirez.com/post/redis-weekly-update-1.html>`_

Virtual Memory
~~~~~~~~~~~~~~

Redis Virtual Memory allows users to grow their dataset beyond the
limits of their RAM.
More on virtual memory:

-  `http://code.google.com/p/redis/wiki/VirtualMemoryUserGuide <http://code.google.com/p/redis/wiki/VirtualMemoryUserGuide>`_
-  `http://antirez.com/post/redis-virtual-memory-story.html <http://antirez.com/post/redis-virtual-memory-story.html>`_

Contributors
------------


-  Salvatore Sanfilippo
-  Pieter Noordhuis
-  Antonio Ognio
-  Alex McHale
-  Michel Martens
-  Damian Janowski
-  Bruno Deferrari
-  Ashley Martens
-  Derek Collison
-  Damian Janowski
-  Jeremy Zawodny
-  Konstantin Merenkov
-  Michel Martens
-  Sam Hendley

.. |Redis Documentation| image:: redis.png