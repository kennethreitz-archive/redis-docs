`|Redis Documentation| <index.html>`_
**Lists: Contents**
  `Redis List Type <#Redis%20List%20Type>`_
  `Implementation details <#Implementation%20details>`_
Lists
=====

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
Redis List Type
===============

Redis Lists are lists of `Redis Strings <Strings.html>`_, sorted by
insertion order. It's possible to add elements to a Redis List
pushing new elements on the head (on the left) or on the tail (on
the right) of the list.
The `LPUSH <RpushCommand.html>`_ command inserts a new elmenet on
head, while `RPUSH <RpushCommand.html>`_ inserts a new element on
tail. A new list is created when one of this operations is
performed against an empty key.
For instance if perform the following operations:
::

    LPUSH mylist a   # now the list is "a"
    LPUSH mylist b   # now the list is "b","a"
    RPUSH mylist c   # now the list is "b","a","c" (RPUSH was used this time)

The resulting list stored at *mylist* will contain the elements
"b","a","c".
The max length of a list is 232-1 elements (4294967295, more than 4
billion of elements per list).
Implementation details
======================

Redis Lists are implemented as doubly liked lists. A few commands
benefit from the fact the lists are doubly linked in order to reach
the needed element starting from the nearest extreme (head or
tail). `LRANGE <LrangeCommand.html>`_ and
`LINDEX <LindexCommand.html>`_ are examples of such commands.
The use of linked lists also guarantees that regardless of the
length of the list pushing and popping are O(1) operations.
Redis Lists cache length information so `LLEN <LlenCommand.html>`_
is O(1) as well.
.. |Redis Documentation| image:: redis.png