`|Redis Documentation| <index.html>`_
**RedisInternals: Contents**
  `Redis Internals <#Redis%20Internals>`_
    `Redis STRINGS <#Redis%20STRINGS>`_
    `Redis Virtual Memory <#Redis%20Virtual%20Memory>`_
    `Redis Event Library <#Redis%20Event%20Library>`_
RedisInternals
==============

Redis Internals
===============

This is a source code level documentation of Redis.
Redis STRINGS
-------------

String is the basic building block of Redis types.
Redis is a key-value store. All Redis keys are strings and its also
the simplest value type.


Lists, sets, sorted sets and hashes are other more complex value
types and even these are composed of strings.
`Hacking Strings <HackingStrings.html>`_ documents the Redis String
implementation details.
Redis Virtual Memory
--------------------

A technical specification full of details about the
`Redis Virtual Memory subsystem <VirtualMemorySpecification.html>`_
Redis Event Library
-------------------

Read `event library <EventLibray.html>`_ to understand what an
event library does and why its needed.
`Redis event library <RedisEventLibrary.html>`_ documents the
implementation details of the event library used by Redis
.. |Redis Documentation| image:: redis.png