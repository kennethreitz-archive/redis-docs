`|Redis Documentation| <index.html>`_
**Redis0100ChangeLog: Contents**
  `Redis 0.100 Changelog <#Redis%200.100%20Changelog>`_
Redis0100ChangeLog
==================

Redis 0.100 Changelog
=====================

::

    - SUNION, SDIFF, SUNIONSTORE, SDIFFSTORE commands implemented. (Aman Gupta, antirez)
    - Non blocking replication. Now while N slaves are synchronizing, the master will continue to ask to client queries. (antirez)
    - PHP client ported to PHP5 (antirez)
    - FLUSHALL/FLUSHDB no longer sync on disk. Just increment the dirty counter by the number of elements removed, that will probably trigger a background saving operation (antirez)
    - INCRBY/DECRBY now support 64bit increments, with tests (antirez)
    - New fields in INFO command, bgsave_in_progress and replication related (antirez)
    - Ability to specify a different file name for the DB (... can't remember ...)
    - GETSET command, atomic GET + SET (antirez)
    - SMOVE command implemented, atomic move-element across sets operation (antirez)
    - Ability to work with huge data sets, tested up to 350 million keys (antirez)
    - Warns if /proc/sys/vm/overcommit_memory is set to 0 on Linux. Also make sure to don't resize the hash tables while the child process is saving in order to avoid copy-on-write of memory pages (antirez)
    - Infinite number of arguments for MGET and all the other commands (antirez)
    - CPP client (Brian Hammond)
    - DEL is now a vararg, IMPORTANT: memory leak fixed in loading DB code (antirez)
    - Benchmark utility now supports random keys (antirez)
    - Timestamp in log lines (antirez)
    - Fix SINTER/UNIONSTORE to allow for &=/|= style operations (i.e. SINTERSTORE set1 set1 set2) (Aman Gupta)
    - Partial qsort implemented in SORT command, only when both BY and LIMIT is used (antirez)
    - Allow timeout=0 config to disable client timeouts (Aman Gupta)
    - Alternative (faster/simpler) ruby client API compatible with Redis-rb (antirez)
    - S*STORE now return the cardinality of the resulting set (antirez)
    - TTL command implemented (antirez)
    - Critical bug about glueoutputbuffers=yes fixed. Under load and with pipelining and clients disconnecting on the middle of the chat with the server, Redis could block. (antirez)
    - Different replication fixes (antirez)
    - SLAVEOF command implemented for remote replication management (antirez)
    - Issue with redis-client used in scripts solved, now to check if the latest argument must come from standard input we do not check that stdin is or not a tty but the command arity (antirez)
    - Warns if using the default config (antirez)
    - maxclients implemented, see redis.conf for details (antirez)
    - max bytes of a received command enlarged from 1k to 32k (antirez)

.. |Redis Documentation| image:: redis.png