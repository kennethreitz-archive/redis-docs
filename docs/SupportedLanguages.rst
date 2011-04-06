`|Redis Documentation| <index.html>`_
**SupportedLanguages: Contents**
  `Supported Languages (DRAFT) <#Supported%20Languages%20(DRAFT)>`_
    `TODO <#TODO>`_
    `Features Support Matrix <#Features%20Support%20Matrix>`_
      `Version 1.1 <#Version%201.1>`_
      `Version 1.0 <#Version%201.0>`_
    `Client Libraries Reference <#Client%20Libraries%20Reference>`_
      `as3 (ActionScript 3) <#as3%20(ActionScript%203)>`_
      `redis-clojure (Clojure) <#redis-clojure%20(Clojure)>`_
      `CL-Redis (Common Lisp) <#CL-Redis%20(Common%20Lisp)>`_
      `erldis (Erlang) <#erldis%20(Erlang)>`_
      `Go-Redis (Go) <#Go-Redis%20(Go)>`_
      `haskell-redis (Haskell) <#haskell-redis%20(Haskell)>`_
      `Java <#Java>`_
      `redis-lua (Lua) <#redis-lua%20(Lua)>`_
      `Perl <#Perl>`_
      `PHP <#PHP>`_
      `Python <#Python>`_
      `txredis <#txredis>`_
      `redis-rb (Ruby) <#redis-rb%20(Ruby)>`_
      `scala-redis (Scala) <#scala-redis%20(Scala)>`_
      `Tcl <#Tcl>`_
SupportedLanguages
==================

Supported Languages (DRAFT)
===========================

Wondering if you can use Redis from your favorite language? Well
here is the definitive guide to the available client libraries.
This libraries are intended to expose Redis commands, but you also
have the option to use some higher level libraries that provide a
**`Object Hash Mappings <ObjectHashMappers.html>`_** pretty much
the same idea implemented by a classic **ORM**.
TODO
----


-  Add
   `http://github.com/madsimian/em-redis <http://github.com/madsimian/em-redis>`_
-  Add
   `http://github.com/besquared/redis-datastructures <http://github.com/besquared/redis-datastructures>`_
-  Add
   `http://github.com/sma/redis-node-client <http://github.com/sma/redis-node-client>`_

Features Support Matrix
-----------------------

The following matrix should give you a quick overviwe of the state
of the different client libraries existing for each supported
language.
The core command set is the one of Version 1.0, while
`Sharding <Sharding.html>`_ and `Pipelining <Pipelining.html>`_ are
convenient client side features not tied to any Redis server
version.
Version 1.1
~~~~~~~~~~~

Compatible client libraries are expected to implement the command
sets specified in **Version 1.0** plus:

-  **String**: MSET, MSETNX.
-  **List**: RPOPLPUSH.
-  **Sorted Set (ZSET)**: ZADD, ZREM, ZRANGE, ZREVRANGE,
   ZRANGEBYSCORE, ZCARD, ZSCORE.

Version 1.0
~~~~~~~~~~~

Compatible client libraries are expected to implement the following
command sets:

-  **String**: GET, SET, SETNX, DEL, EXISTS, INCR, DECR, MGET,
   INCRBY, DECRBY, GETSET, TYPE.
-  **List**: RPUSH, LPUSH, RPOP, LPOP, LLEN, LINDEX, LSET, LRANGE,
   LTRIM, LREM.
-  **Set**: SADD, SREM, SMOVE, SISMEMBER, SCARD, SPOP, SINTER,
   SINTERSTORE, SUNION, SUNIONSTORE, SDIFF, SDIFFSTORE, SMEMBERS.
-  **Keyspace**: KEYS, RANDOMKEY, RENAME, RENAMENX, DBSIZE, EXPIRE,
   TTL.
-  **Databases**: SELECT, MOVE, FLUSHDB, FLUSHALL.
-  **Sort**: SORT
-  **Connection**: AUTH, QUIT?. ???
-  **Persistence**: SAVE, BGSAVE, LASTSAVE, SHUTDOWN?. ???
-  **Server**: INFO, MONITOR? SLAVEOF? ???



**Language**
**Name**
**Sharding**
**Pipelining**
**1.1**
**1.0**
ActionScript 3
as3redis
No
Yes
Yes
Yes
Clojure
redis-clojure
No
No
Partial
Yes
Common Lisp
CL-Redis
No
No
No
Yes
Erlang
erldis
No
Looks like
No
Looks like
Go
Go-Redis
No
Yes
Yes
Yes
Haskell
haskell-redis
No
No
No
Yes
Java
JDBC-Redis
No
No
No
Yes
Java
JRedis
No
Yes
Yes
Yes
Java
Jedis
No
Yes
Yes
Yes
LUA
redis-lua
No
No
Yes
Yes
Perl
Redis Client
No
No
No
Yes
Perl
AnyEvent::Redis
No
No
No
Yes
PHP
Redis PHP Bindings
No
No
No
Yes
PHP
phpredis (C)
No
No
No
Yes
PHP
Predis
Yes
Yes
Yes
Yes
PHP
Redisent
Yes
No
No
Yes
Python
Python Client
No
No
No
Yes
Python
py-redis
No
No
Partial
Yes
Python
txredis
No
No
No
Yes
Ruby
redis-rb
Yes
Yes
Yes
Yes
Scala
scala-redis
Yes
No
No
Yes
TCL
TCL
No
No
Yes
Yes
Client Libraries Reference
--------------------------

as3 (ActionScript 3)
~~~~~~~~~~~~~~~~~~~~


-  An ActionScript 3 (Flash) library for Redis.
-  Repository:
   `http://github.com/claus/as3redis <http://github.com/claus/as3redis>`_
-  Author: Claus Wahlers,
   `@cwahlers <http://twitter.com/cwahlers>`_.

redis-clojure (Clojure)
~~~~~~~~~~~~~~~~~~~~~~~


-  A Clojure client library for the key-value storage system Redis.
-  Repository:
   `http://github.com/ragnard/redis-clojure <http://github.com/ragnard/redis-clojure>`_
-  Author: Ragnar DahlÃ©n, `@ragge <http://twitter.com/ragge>`_.

CL-Redis (Common Lisp)
~~~~~~~~~~~~~~~~~~~~~~


-  Common Lisp client library for Redis, an advanced key/value
   store.
-  Home Page:
   `http://www.cliki.net/cl-redis <http://www.cliki.net/cl-redis>`_
-  Author: Mahmud,
   `@BigThingist <http://twitter.com/BigThingist>`_.

erldis (Erlang)
~~~~~~~~~~~~~~~


-  Client protocol for redis key-value store.
-  Author: `Valentino Volonghi <http://www.adroll.com/>`_,
   `@dialtone\_ <http://twitter.com/dialtone_>`_.
-  Repository:
   `http://bitbucket.org/adroll/erldis/ <http://bitbucket.org/adroll/erldis/>`_

Go-Redis (Go)
~~~~~~~~~~~~~


-  Client protocol for redis key-value store.
-  Author: Joubin Houshyar,
   `@SunOf27 <http://twitter.com/SunOf27>`_.
-  Repository:
   `http://github.com/alphazero/Go-Redis <http://github.com/alphazero/Go-Redis>`_

haskell-redis (Haskell)
~~~~~~~~~~~~~~~~~~~~~~~


-  A Haskell binding for the Redis database.
-  Author: `Alvaro Videla <http://obvioushints.blogspot.com/>`_,
   `@old\_sound <http://twitter.com/old_sound>`_.
-  Repository:
   ` <http://bitbucket.org/videlalvaro/redis-haskell/wiki/Home>`_

Java
~~~~

JDBC-Redis
^^^^^^^^^^


-  JDBC-Redis is Java driver using the JDBC interface for Redis
   Database. This project doesn't aim for a complete implementation of
   the JDBC specification since Redis isn't a relational database, but
   should provide a familiar interface to Java developers interact
   with Redis.
-  Repository:
   `http://code.google.com/p/jdbc-redis/ <http://code.google.com/p/jdbc-redis/>`_

JRedis
^^^^^^


-  Java Client and Connectors for Redis JCA compliant. Currently
   offers a complete functioning Synchronous connector, Asynchronous
   connection and pipelining support under heavy development.
-  Author: Joubin Houshyar,
   `@SunOf27 <http://twitter.com/SunOf27>`_.
-  Home:
   `http://code.google.com/p/jredis/ <http://code.google.com/p/jredis/>`_
-  Repository:
   `http://github.com/alphazero/jredis <http://github.com/alphazero/jredis>`_

Jedis
^^^^^


-  Jedis is a small and sane Redis client for Java. It aims to be
   easier to use by providing a more natural API. It currently
   supports the binary-safe protocol and pipelining. Sharding and
   connection pooling is on the way.
-  Author: Jonathan Leibiusky,
   `@xetorthio <http://twitter.com/xetorthio>`_.
-  Repository:
   `http://github.com/xetorthio/jedis <http://github.com/xetorthio/jedis>`_

redis-lua (Lua)
~~~~~~~~~~~~~~~


-  A Lua client library for the redis key value storage system.
-  Author:
   `Daniele Alessandri <http://www.clorophilla.net/blog/>`_,
   `@jol1hahn <http://twitter.com/jol1hahn>`_.
-  Repository:
   `http://github.com/nrk/redis-lua <http://github.com/nrk/redis-lua>`_

Perl
~~~~

Perl Client
^^^^^^^^^^^


-  Perl binding for Redis database.
-  Author: `Dobrica Pavlinusic <http://blog.rot13.org/>`_,
   `@dpavlin <http://twitter.com/dpavlin>`_.
-  Repository:
   `http://svn.rot13.org/index.cgi/Redis <http://svn.rot13.org/index.cgi/Redis>`_

AnyEvent::Redis
^^^^^^^^^^^^^^^


-  Non-blocking Redis client.
-  Author: `Tatsuhiko Miyagawa <http://bulknews.typepad.com/>`_,
   `@miyagawa <http://twitter.com/miyagawa>`_.
-  Repository:
   `http://github.com/miyagawa/AnyEvent-Redis/ <http://github.com/miyagawa/AnyEvent-Redis/>`_

PHP
~~~

Redis PHP Bindings
^^^^^^^^^^^^^^^^^^


-  Simple default binding in Redis main repository. No longer under
   active development.
-  Author: `Ludovico Magnocavallo <http://qix.it/>`_,
   `@ludo <http://twitter.com/ludo>`_.
-  Repository:
   `http://code.google.com/p/redis/source/browse/#svn/trunk/client-libraries/php <http://code.google.com/p/redis/source/browse/#svn/trunk/client-libraries/php>`_

phpredis
^^^^^^^^


-  This extension provides an API for communicating with Redis
   database, a persistent key-value database with built-in net
   interface written in ANSI-C for Posix systems.
-  Author: `Alfonso Jimenez <http://www.alfonsojimenez.com/>`_ ,
   (`@alfonsojimenez <http://twitter.com/alfonsojimenez>`_), Nicolas
   Favre-FÃ©lix and Nasreddine Bouafif.
-  Repository:
   `http://github.com/owlient/phpredis <http://github.com/owlient/phpredis>`_

Predis
^^^^^^


-  A flexible and feature-complete PHP client library for the Redis
   key-value database. Predis is currently a work-in-progress and it
   targets PHP >= 5.3, though it is highly due to be backported to PHP
   >= 5.2.6 as soon as the public API and the internal design on the
   main branch will be considered stable enough.
-  Author:
   `Daniele Alessandri <http://www.clorophilla.net/blog/>`_,
   `@jol1hahn <http://twitter.com/jol1hahn>`_
-  Repository:
   `http://github.com/nrk/predis/ <http://github.com/nrk/predis/>`_

Redisent
^^^^^^^^


-  Redisent is a simple, no-nonsense interface to the Redis
   key-value store for modest developers. Due to the way it is
   implemented, it is flexible and tolerant of changes to the Redis
   protocol.
-  Author: `Justin Poliey <http://blog.justinpoliey.com/>`_,
   `@justinpoliey <http://twitter.com/justinpoliey>`_
-  Repository:
   `http://github.com/jdp/redisent <http://github.com/jdp/redisent>`_

Python
~~~~~~

Python Client
^^^^^^^^^^^^^


-  Simple Python client in Redis main repository. No longer under
   active development.
-  Author: `Ludovico Magnocavallo <http://qix.it/>`_,
   `@ludo <http://twitter.com/ludo>`_.
-  Repository:
   `http://code.google.com/p/redis/source/browse/#svn/trunk/client-libraries/python <http://code.google.com/p/redis/source/browse/#svn/trunk/client-libraries/python>`_

py-redis
^^^^^^^^


-  Redis Python Client.
-  Author: `McCurdy <Andy.html>`_,
   `@andymccurdy <http://twitter.com/andymccurdy>`_.
-  Repository:
   `http://github.com/andymccurdy/redis-py <http://github.com/andymccurdy/redis-py>`_

txredis
~~~~~~~


-  Python/Twisted client for Redis key-value store
-  Author: Dorian Raymer,
   `@dio\_rian <http://twitter.com/dio_rian>`_.
-  PyPI:
   `http://pypi.python.org/pypi/txredis/0.1.1 <http://pypi.python.org/pypi/txredis/0.1.1>`_

redis-rb (Ruby)
~~~~~~~~~~~~~~~


-  A Ruby client library for the redis key value storage engine.
-  Author: `Ezra Zygmuntowicz <http://brainspl.at/>`_,
   `@ezmobius <http://twitter.com/ezmobius>`_.
-  Repository:
   `http://github.com/ezmobius/redis-rb <http://github.com/ezmobius/redis-rb>`_

scala-redis (Scala)
~~~~~~~~~~~~~~~~~~~


-  A scala library for connecting to a redis server, or a cluster
   of redis nodes using consistent hashing on the client side.
-  Author:
   `Alejandro Crosa <http://www.linkedin.com/in/alejandrocrosa>`_,
   `@alejandrocrosa <http://twitter.com/alejandrocrosa>`_.
-  Repository:
   `http://github.com/acrosa/scala-redis <http://github.com/acrosa/scala-redis>`_

Tcl
~~~


-  The official version is included in the Redis tarball since it's
   maintained by Salvatore.
-  Author: `Salvatore Sanfilippo <http://invece.org/>`_,
   `@antirez <http://twitter.com/antirez>`_
-  Repository:
   `http://github.com/antirez/redis/blob/master/redis.tcl <http://github.com/antirez/redis/blob/master/redis.tcl>`_

.. |Redis Documentation| image:: redis.png