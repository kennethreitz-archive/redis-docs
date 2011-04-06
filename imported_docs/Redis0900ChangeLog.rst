`|Redis Documentation| <index.html>`_
**Redis0900ChangeLog: Contents**
  `CHANGELOG for Redis 0.900 <#CHANGELOG%20for%20Redis%200.900>`_
Redis0900ChangeLog
==================

CHANGELOG for Redis 0.900
=========================

::

    2009-06-16 client libraries updated (antirez)
    2009-06-16 Better handling of background saving process killed or crashed (antirez)
    2009-06-14 number of keys info in INFO command (Diego Rosario Brogna)
    2009-06-14 SPOP documented (antirez)
    2009-06-14 Clojure library (Ragnar DahlÃ©n)
    2009-06-10 It is now possible to specify - as config file name to read it from stdin (antirez)
    2009-06-10 max bytes in an inline command raised to 1024*1024 bytes, in order to allow for very large MGETs and still protect from client crashes (antirez)
    2009-06-08 SPOP implemented. Hash table resizing for Sets and Expires too. Changed the resize policy to play better with RANDOMKEY and SPOP. (antirez)
    2009-06-07 some minor changes to the backtrace code (antirez)
    2009-06-07 enable backtrace capabilities only for Linux and MacOSX (antirez)
    2009-06-07 Dump a backtrace on sigsegv/sigbus, original coded (Diego Rosario Brogna)
    2009-06-05 Avoid a busy loop while sending very large replies against very fast links, this allows to be more responsive with other clients even under a KEY * against the loopback interface (antirez)
    2009-06-05 Kill the background saving process before performing SHUTDOWN to avoid races (antirez)
    2009-06-05 LREM now returns :0 for non existing keys (antirez)
    2009-06-05 added config.h for #ifdef business isolation, added fstat64 for Mac OS X (antirez)
    2009-06-04 macosx specific zmalloc.c, uses malloc_size function in order to avoid to waste memory and time to put an additional header (antirez)
    2009-06-04 DEBUG OBJECT implemented (antirez)
    2009-06-03 shareobjectspoolsize implemented in reds.conf, in order to control the pool size when object sharing is on (antirez)
    2009-05-27 maxmemory implemented (antirez)

.. |Redis Documentation| image:: redis.png