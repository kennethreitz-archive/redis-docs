`|Redis Documentation| <index.html>`_
**Hashes: Contents**
  `Redis Hash Type <#Redis%20Hash%20Type>`_
  `Implementation details <#Implementation%20details>`_
Hashes
======

ï»¿#sidebar `HashCommandsSidebar <HashCommandsSidebar.html>`_
Redis Hash Type
===============

Redis Hashes are unordered maps of `Redis Strings <String.html>`_
between fields and values. It is possible to add, remove, test for
existence of fields in O(1) amortized time. It is also possible to
enumerate all the keys, values, or both, in O(N) (where N is the
number of fields inside the hash).
Redis Hashes are interesting because they are very well suited to
represent objects. For instance web applications users can be
represented by a Redis Hash containing fields such username,
encrpypted\_password, lastlogin, and so forth.
Another very important property of Redis Hashes is that they use
very little memory for hashes composed of a small number of fields
(configurable, check redis.conf for details), compared to storing
every field as a top level Redis key. This is obtained using a
different specialized representation for small hashes. See the
implementation details paragraph below for more information.
Commands operating on hashes try to make a good use of the return
value in order to signal the application about previous existence
of fields. For instance the `HSET <HsetCommand.html>`_ command will
return 1 if the field set was not already present in the hash,
otherwise will return 0 (and the user knows this was just an update
operation).
The max number of fields in a set is 232-1 (4294967295, more than 4
billion of members per hash).
Implementation details
======================

The obvious internal representation of hashes is indeed an hash
table, as the name of the data structure itself suggests. Still the
drawback of this representation is that there is a lot of space
overhead for hash table metadata.
Because one of the most interesting uses of Hashes is object
encoding, and objects are often composed of a few fields each,
Redis uses a different internal representation for small hashes
(for Redis to consider a hash small, this must be composed a
limited number of fields, and each field and value can't exceed a
given number of bytes. All this is user-configurable).
Small hashes are thus encoded using a data structure called zipmap
(is not something you can find in a CS book, the name is a Redis
invention), that is a very memory efficient data structure to
represent string to string maps, at the cost of being O(N) instead
of O(1) for most operations. Since the constant times of this data
structure are very small, and the zipmaps are converted into real
hash tables once they are big enough, the amortized time of Redis
hashes is still O(1), and in the practice small zipmaps are not
slower than small hash tables because they are designed for good
cache locality and fast access.
The result is that small hashes are both memory efficient and fast,
while bigger hashes are fast but not as memory efficient than small
hashes.
.. |Redis Documentation| image:: redis.png