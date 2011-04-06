`|Redis Documentation| <index.html>`_
**Sets: Contents**
  `Redis Set Type <#Redis%20Set%20Type>`_
  `Implementation details <#Implementation%20details>`_
Sets
====

ï»¿#sidebar `SetCommandsSidebar <SetCommandsSidebar.html>`_
Redis Set Type
==============

Redis Sets are unordered collections of
`Redis Strings <Strings.html>`_. It's possible to add, remove, and
test for existence of members in O(1).
Redis Sets have the desirable property of not allowing repeated
members. Adding the same element multiple times will result in a
set having a single copy of this element. Practically speaking this
means that adding an members does not require a "check if exists
then add" operation.
Commands operating on sets try to make a good use of the return
value in order to signal the application about previous existence
of members. For instance the `SADD <SaddCommand.html>`_ command
will return 1 if the element added was not already a member of the
set, otherwise will return 0.
The max number of members in a set is 232-1 (4294967295, more than
4 billion of members per set).
Redis Sets support a wide range of operations, like union,
intersection, difference. Intersection is optimized in order to
perform the smallest number of lookups. For instance if you try to
intersect a 10000 members set with a 2 members set Redis will
iterate the 2 members set testing for members existence in the
other set, performing 2 lookups instead of 10000.
Implementation details
======================

Redis Sets are implemented using hash tables, so adding, removing
and testing for members is O(1) in the average. The hash table will
automatically resize when new elements are added or removed into a
Set.
The hash table resizing is a blocking operation performed
synchronously so working with huge sets (consisting of many
millions of elements) care should be taken when mass-inserting a
very big amount of elements in a Set while other clients are
querying Redis at high speed.
It is possible that in the near future Redis will switch to skip
lists (already used in sorted sets) in order to avoid such a
problem.
.. |Redis Documentation| image:: redis.png