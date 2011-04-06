`|Redis Documentation| <index.html>`_
**index: Contents**
  `Getting started <#Getting%20started>`_
  `Full programming examples <#Full%20programming%20examples>`_
  `FAQs and benchmarks <#FAQs%20and%20benchmarks>`_
  `HOWTOs about selected features <#HOWTOs%20about%20selected%20features>`_
  `Hacking <#Hacking>`_
  `Videos <#Videos>`_
  `Recipes and books <#Recipes%20and%20books>`_
index
=====

ï»¿= Redis Documentation =
`Russian Translation <http://pyha.ru/wiki/index.php?title=Redis:index>`_Hello!
The followings are pointers to different parts of the Redis
Documentation.
Getting started
===============


-  New! You can now
   `Try Redis directly in your browser! <http://try.redis-db.com>`_.
-  `The README <README.html>`_ is a good starting point to know
   more about the project.
-  `This short Quick Start <QuickStart.html>`_ provides a five
   minutes step-by-step istructions on how to download, compile, run
   and test the basic workings of a Redis server.
-  `The command reference <CommandReference.html>`_ is a
   description of all the Redis commands with links to command
   specific pages. You can also download the
   `Redis Commands Cheat-Sheet <http://go2.wordpress.com/?id=725X1342&site=masonoise.wordpress.com&url=http://masonoise.files.wordpress.com/2010/03/redis-cheatsheet-v1.pdf>`_
   provided by Mason Jones (btw some command may be missing, the
   primary source is the wiki).
-  `A Fifteen Minutes Introduction to the Redis Data Types <IntroductionToRedisDataTypes.html>`_
   explains how Redis data types work and the basic patterns of
   working with Redis.
-  `the Simon Willison Redis Tutorial <http://simonwillison.net/static/2010/redis-tutorial/>`_
   is a **must read**, very good documentation where you will find a
   lot of real world ideas and use cases.
-  `Redis from the ground up <http://blog.mjrusso.com/2010/10/17/redis-from-the-ground-up.html>`_
   is an impressive article to know more about Redis if you are a
   newcomer.
-  `Getting started with Redis and Python <http://playnice.ly/blog/2010/10/19/getting-started-redis-python/>`_

Full programming examples
=========================


-  `This is a tutorial about creating a Twitter clone using \*only\* Redis as database, no relational DB at all is used <TwitterAlikeExample.html>`_,
   it is a good start to understand the key-value database paradigm.

FAQs and benchmarks
===================


-  `The benchmark page <Benchmarks.html>`_ is about the speed
   performances of Redis.
-  `Our FAQ <FAQ.html>`_ contains of course some answers to common
   questions about Redis. Not very up-to-date.

HOWTOs about selected features
==============================


-  `The Redis Replication HOWTO <ReplicationHowto.html>`_ is what
   you need to read in order to understand how Redis master ``<->``
   slave replication works.
-  `The Append Only File HOWTO <AppendOnlyFileHowto.html>`_
   explains how the alternative Redis durability mode works. AOF is an
   alternative to snapshotting on disk from time to time (the
   default).
-  `Virtual Memory User Guide <VirtualMemoryUserGuide.html>`_. A
   simple to understand guide about using and configuring the Redis
   Virtual Memory.
-  `Redis Pipelining Guide <RedisPipelining.html>`_.
-  Memory optimization: Full of keys, a
   `blog post at antirez.com <http://antirez.com/post/redis-weekly-update-7.html>`_
   showing how to use Redis 2.0 and hashes to create a setup where you
   can store 5 times more data in your Redis instance.
-  `Implementing auto complete with Redis <http://antirez.com/post/autocomplete-with-redis.html>`_.

Hacking
=======


-  `The Protocol Specification <ProtocolSpecification.html>`_ is
   all you need in order to implement a Redis client library for a
   missing language. PHP, Python, Ruby and Erlang are already
   supported.
-  Look at `Redis Internals <RedisInternals.html>`_ if you are
   interested in the implementation details of the Redis server.

Videos
======


-  `Ezra Zygmuntowicz at the Mountain West Ruby Conference 2009 <http://confreaks.net/videos/62-mwrc2009-redis-key-value-nirvana>`_
   to know the most important Redis ideas in few minutes.
-  `Salvatore Sanfilippo and Pieter Noordhuis at the SF Redis Meetup <http://www.ustream.tv/recorded/7855635>`_

Recipes and books
=================


-  `The Redis Cookbook <http://www.rediscookbook.org/>`_ is a
   collaborative effort to provide some good recipe.
-  There is an ongoing effort to write a Redis book for O'Reilly

.. |Redis Documentation| image:: redis.png