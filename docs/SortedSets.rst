`|Redis Documentation| <index.html>`_
**SortedSets: Contents**
  `Redis Sorted Set Type <#Redis%20Sorted%20Set%20Type>`_
  `Implementation details <#Implementation%20details>`_
SortedSets
==========

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
Redis Sorted Set Type
=====================

Redis Sorted Sets are, similarly to `Sets <Sets.html>`_,
collections of `Redis Strings <Strings.html>`_. The difference is
that every member of a Sorted Set hash an **associated score** that
is used in order to take this member in order.
The `ZADD <ZaddCommand.html>`_ command is used to add a new member
to a Sorted Set, specifying the score of the element. Calling ZADD
against a member already present in the sorted set but using a
different score will update the score for the element, moving it to
the right position in order to preserve ordering.
It's possible to get ranges of elements from Sorted Sets in a very
similar way to what happens with `Lists <Lists.html>`_ and the
`LRANGE <LrangeCommnad.html>`_ command using the Sorted Sets
`ZRANGE <ZrangeCommand.html>`_ command.
It's also possible to get or remove ranges of elements by score
using the `ZRANGEBYSCORE <ZrangebyscoreCommand.html>`_ and
`ZREMRANGEBYSCORE <ZremrangebyscoreCommand.html>`_ commands.
The max number of members in a sorted set is 232-1 (4294967295,
more than 4 billion of members per set).
Note that while Sorted Sets are already ordered, it is still
possible to use the `SORT <SortCommand.html>`_ command against
sorted sets to get the elements in a different order.
Implementation details
======================

Redis Sets are implemented using a dual-ported data structure
containing a skip list and an hash table. When an element is added
a map between the element and the score is added to the hash table
(so that given the element we get the score in O(1)), and a map
between the score and the element is added in the skip list so that
elements are taken in order.
Redis uses a special skip list implementation that is doubly linked
so that it's possible to traverse the sorted set from tail to head
if needed (Check the `ZREVRANGE <ZRevrangeCommand.html>`_ command).
When `ZADD <ZaddCommand.html>`_ is used in order to update the
score of an element, Redis retrieve the score of the element using
the hash table, so that it's fast to access the element inside the
skip list (that's indexed by score) in order to update the
position.
Like it happens for Sets the hash table resizing is a blocking
operation performed synchronously so working with huge sorted sets
(consisting of many millions of elements) care should be taken when
mass-inserting a very big amount of elements in a Set while other
clients are querying Redis at high speed.
It is possible that in the near future Redis will switch to skip
lists even for the element => score map, so every Sorted Set will
have two skip lists, one indexed by element and one indexed by
score.
.. |Redis Documentation| image:: redis.png