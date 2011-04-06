`|Redis Documentation| <index.html>`_
**Redis\_1\_2\_0\_Changelog: Contents**
  `What's new in Redis 1.2 <#What's%20new%20in%20Redis%201.2>`_
    `New persistence mode: Append Only File <#New%20persistence%20mode:%20Append%20Only%20File>`_
    `New data type: sorted sets <#New%20data%20type:%20sorted%20sets>`_
    `Specialized integer objects encoding <#Specialized%20integer%20objects%20encoding>`_
    `MSET and MSETNX <#MSET%20and%20MSETNX>`_
    `Better Performances <#Better%20Performances>`_
    `Solaris Support <#Solaris%20Support>`_
    `Support for the new generation protocol <#Support%20for%20the%20new%20generation%20protocol>`_
    `A few new commands about already supported data types <#A%20few%20new%20commands%20about%20already%20supported%20data%20types>`_
    `Bug fixing <#Bug%20fixing>`_
  `CHANGELOG for Redis 1.1.90 <#CHANGELOG%20for%20Redis%201.1.90>`_
Redis\_1\_2\_0\_Changelog
=========================

What's new in Redis 1.2
=======================

New persistence mode: Append Only File
--------------------------------------

The Append Only File is an alternative way to save your data in
Redis that is fully durable! Unlike the snapshotting (default)
persistence mode, where the database is saved asynchronously from
time to time, the Append Only File saves every change ASAP in a
text-only file that works like a journal. Redis will play back this
file again at startup reloading the whole dataset back in memory.
Redis Append Only File supports background Log compaction. For more
info read the `Append Only File HOWTO <AppendOnlyFileHowto.html>`_.
New data type: sorted sets
--------------------------

Sorted sets are collections of elements (like Sets) with an
associated score (in the form of a double precision floating point
number). Elements in a sorted set are taken in order, so for
instance to take the greatest element is an O(1) operation.
Insertion and deletion is O(log(N)). Sorted sets are implemented
using a dual ported data structure consisting of an hash table and
a skip list. For more information please read the
`Introduction To Redis Data Types <IntroductionToRedisDataTypes.html>`_.
Specialized integer objects encoding
------------------------------------

Redis 1.2 will use less memory than Redis 1.0 for values in
Strings, Lists or Sets elements that happen to be representable as
32 or 64 bit signed integers (it depends on your arch bits for the
long C type). This is totally transparent form the point of view of
the user, but will safe a lot of memory (30% less in datasets where
there are many integers).
MSET and MSETNX
---------------

That is, setting multiple keys in one command, atomically. For more
information see the `MSET command <MsetCommand.html>`_ wiki page.
Better Performances
-------------------


-  100x times faster SAVE and BGSAVE! There was a problem in the
   LZF lib configuration that is now resolved. The effect is this
   impressive speedup. Also the saving child will no longer use 100%
   of CPU.
-  Glue output buffer and writev(). Many commands producing large
   outputs, like LRANGE, will now be even 10 times faster, thanks to
   the new output buffer gluing algorithm and the (optional) use of
   writev(2) syscall.
-  Support for epool and kqueue / kevent. 10,000 clients
   scalability.
-  Much better EXPIRE support, now it's possible to work with very
   large sets of keys expiring in very short time without to incur in
   memory problems (the new algorithm expires keys in an adaptive way,
   so will get more aggressive if there are a lot of expiring keys)

Solaris Support
---------------

Redis will now compile and work on Solaris without problems.
Warning: the Solaris user base is very little, so Redis running on
Solaris may not be as tested and stable as it is on Linux and Mac
OS X.
Support for the new generation protocol
---------------------------------------


-  Redis is now able to accept commands in a new fully binary safe
   way: with the new protocol keys are binary safe, not only values,
   and there is no distinction between bulk commands and inline
   commands. This new protocol is currently used only for MSET and
   MSETNX but at some point it will hopefully replace the old one. See
   the Multi Bulk Commands section in the
   `Redis Protocol Specification <ProtocolSpecification.html>`_ for
   more information.

A few new commands about already supported data types
-----------------------------------------------------


-  `SRANDMEMBER <SrandmemberCommand.html>`_
-  The `SortCommand <SortCommand.html>`_ is now supprots the
   **STORE** and **GET #** forms, the first can be used to save sorted
   lists, sets or sorted sets into keys for caching. Check the manual
   page for more information about the **GET #** form.
-  The new `RPOPLPUSH command <RpoplpushCommand.html>`_ can do many
   interesting magics, and a few of this are documented in the wiki
   page of the command.

Bug fixing
----------

Of course, many bugs are now fixed, and I bet, a few others
introduced: this is how software works after all, so make sure to
report issues in the Redis mailing list or in the Google Code
issues tracker.
Enjoy! antirez
CHANGELOG for Redis 1.1.90
==========================


-  2009-09-10 in-memory specialized object encoding. (antirez)
-  2009-09-17 maxmemory fixed in 64 systems for values > 4GB.
   (antirez)
-  2009-10-07 multi-bulk protocol implemented. (antriez)
-  2009-10-16 MSET and MSETNX commands implemented (antirez)
-  2009-10-21 SRANDMEMBER added (antirez)
-  2009-10-23 Fixed compilation in mac os x snow leopard when
   compiling a 32 bit binary. (antirez)
-  2009-10-23 New data type: Sorted sets and Z-commands (antirez)
-  2009-10-26 Solaris fixed (Alan Harder)
-  2009-10-29 Fixed Issue a number of open issues (antirez)
-  2009-10-30 New persistence mode: append only file (antirez)
-  2009-11-01 SORT STORE option (antirez)
-  2009-11-03 redis-cli now accepts a -r (repeat) switch. (antirez)
-  2009-11-04 masterauth option merged (Anthony Lauzon)
-  2009-11-04 redis-test is now a better Redis citizen, testing
   everything against DB 9 and 10 and only if this DBs are empty.
   (antirez)
-  2009-11-10 Implemented a much better lazy expiring algorithm for
   EXPIRE (antirez)
-  2009-11-11 RPUSHLPOP (antirez from an idea of @ezmobius)
-  2009-11-12 Merge git://github.com/ianxm/redis (Can't remmber
   what this implements, sorry)
-  2009-11-17 multi-bulk reply support for redis-bench, LRANGE
   speed tests (antirez)
-  2009-11-17 support for writev implemented. (Stefano Barbato)
-  2009-11-19 debug mode (-D) in redis-bench (antirez)
-  2009-11-21 SORT GET # implemented (antirez)
-  2009-11-23 ae.c made modular, with support for epoll. (antirez)
-  2009-11-26 background append log rebuilding (antirez)
-  2009-11-28 Added support for kqueue. (Harish Mallipeddi)
-  2009-11-29 SORT support for sorted sets (antirez, thanks to
   @tobi for the idea)

.. |Redis Documentation| image:: redis.png