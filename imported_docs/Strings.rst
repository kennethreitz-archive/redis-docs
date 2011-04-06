`|Redis Documentation| <index.html>`_
**Strings: Contents**
  `Redis String Type <#Redis%20String%20Type>`_
  `Implementation details <#Implementation%20details>`_
Strings
=======

ï»¿#sidebar `StringCommandsSidebar <StringCommandsSidebar.html>`_
Redis String Type
=================

Strings are the most basic Redis kind of values. Redis Strings are
binary safe, this means a Redis string can contain any kind of
data, for instance a JPEG image or a serialized Ruby object, and so
forth.
A String value can be at max 512 Megabytes in length.
Strings are treated as integer values by the
`INCR <IncrCommand.html>`_ commands family, in this respect the
value of an intger is limited to a singed 64 bit value.
Note that the single elements contained in Redis
`Lists <Lists.html>`_, `Sets <Sets.html>`_ and
`Sorted Sets <SortedSets.html>`_, are Redis Strings.
Implementation details
======================

Strings are implemented using a dynamic strings library called
``sds.c`` (simple dynamic strings). This library caches the current
length of the string, so to obtain the length of a Redis string is
an O(1) operation (but currently there is no such STRLEN command.
It will likely be added later).
Redis strings are incapsualted into Redis Objects. Redis Objects
use a reference counting memory management system, so a single
Redis String can be shared in different places of the dataset. This
means that if you happen to use the same strings many times
(especially if you have *object sharing* turned on in the
configuration file) Redis will try to use the same string object
instead to allocate one new every time.
Starting from version 1.1 Redis is also able to encode in a special
way strings that are actually just numbers. Instead to save the
string as an array of characters Redis will save the integer value
in order to use less memory. With many datasets this can reduce the
memory usage of about 30% compared to Redis 1.0.
.. |Redis Documentation| image:: redis.png