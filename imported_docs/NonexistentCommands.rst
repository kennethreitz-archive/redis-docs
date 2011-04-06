`|Redis Documentation| <index.html>`_
**NonexistentCommands: Contents**
  `HGETSET <#HGETSET>`_
  `SET with expire <#SET%20with%20expire>`_
  `ZADDNX <#ZADDNX>`_
NonexistentCommands
===================

A list of commands that don't exist in Redis, but can be
accomplished in a different way.
This is a list of commands that don't exist in Redis, but can be
accomplished in a different way, usually by means of
`WATCH/MULTI/EXEC <MultiExecCommand.html>`_.
For better performance, you can pipeline multiple commands.
HGETSET
=======

`GETSET <GetsetCommand.html>`_ for Hashes.
::

    WATCH foo
    old_value = HGET foo field
    MULTI
    HSET foo field new_value
    EXEC

SET with expire
===============

See `SETEX <SetexCommand.html>`_.
ZADDNX
======

Add an element to a sorted set, only if the element doesn't already
exist (by default, `ZADD <ZaddCommand.html>`_ would update the
element's score if it already exists).
`See thread <http://groups.google.com/group/redis-db/browse_thread/thread/fc4c79d72e5bd346/6cdc07ecc36b81e7>`_.
::

    WATCH foo
    score = ZSCORE foo bar
    IF score != NIL
      MULTI
      ZADD foo 1 bar
      EXEC
    ENDIF

.. |Redis Documentation| image:: redis.png