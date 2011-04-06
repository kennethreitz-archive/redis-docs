`|Redis Documentation| <index.html>`_
**Features: Contents**
  `Features (DRAFT) <#Features%20(DRAFT)>`_
    `Speed <#Speed>`_
    `Persistence <#Persistence>`_
    `Support for Data Structures <#Support%20for%20Data%20Structures>`_
    `Atomic Operations <#Atomic%20Operations>`_
    `Variety of Supported Languages <#Variety%20of%20Supported%20Languages>`_
    `Master/Slave Replication <#Master/Slave%20Replication>`_
    `Sharding <#Sharding>`_
    `Hot Backups <#Hot%20Backups>`_
    `Simple to Install, Setup and Manage <#Simple%20to%20Install,%20Setup%20and%20Manage>`_
    `Portable <#Portable>`_
    `Liberal Licensing <#Liberal%20Licensing>`_
    `What's next? <#What's%20next?>`_
Features
========

ï»¿#sidebar `SideBar <SideBar.html>`_
Features (DRAFT)
================

Checking Redis for the first time? Here your will find the most
important features, and pointers to a lot more information.
Speed
-----

Redis is written in ANSI C, and loads the whole dataset in memory,
so it is wicked ***fast**!* Up to 110,000
`SETs <SETs.html>`_/second, 81,000 GETs/second can be achieved in
an entry level Linux box. Read more about Redis
`Speed <Speed.html>`_.
Also Redis supports `Pipelining <Pipelining.html>`_ of commands and
`getting and setting mÃºltiple values in a single command <MultiBulkCommands.html>`_
to speed up communication with the client libraries.
Persistence
-----------

While all the data lives in memory, changes are *asynchronously*
saved on disk using flexible policies based on elapsed time and/or
number of updates since last save.
If you can't afford losing some data, starting on version 1.1
(currently in beta but you can download it from the Git repository)
Redis supports an append-only file persistence mode. Check more on
`Persistence <Persistence.html>`_, or read the
`AppendOnlyFileHowto <AppendOnlyFileHowto.html>`_ for more
information.
Support for Data Structures
---------------------------

Values in Redis can be `Strings <Strings.html>`_ as in a
conventional key-value store, but also `Lists <Lists.html>`_,
`Sets <Sets.html>`_, and `SortedSets <SortedSets.html>`_ (to be
support in `version 1.1 <RoadMap.html>`_). This data types allow
pushing/poping elements, or adding/removing them, also perform
server side union, intersection, difference between sets, and so
forth depending on the types. Redis supports different kind of
sorting abilities for `Sets <Sets.html>`_ and
`Lists <Lists.html>`_.
You can think in Redis as a **Data Structures Server**, that allows
you to model non trivial problems. Read
`Data Types <DataTypes.html>`_ to learn more about the way Redis
handle `Strings <Strings.html>`_, and the
`Commands <Commands.html>`_ supported by `Lists <Lists.html>`_,
`Sets <Sets.html>`_ and `SortedSets <SortedSets.html>`_
Atomic Operations
-----------------

Redis operations working on the different Data Types are
**atomic**, so setting or increasing a key, adding and removing
elements from a set, increasing a counter will all be accomplished
safely.
Variety of Supported Languages
------------------------------

Ruby, Python, Twisted Python, PHP, Erlang, Tcl, Perl, Lua, Java,
Scala, Clojure, choose your poison. Check the list of
`Supported Languages <SupportedLanguages.html>`_ for all the
details.
If your favorite language is not supported yet, you can write your
own client library, as the `Protocol <ProtocolSpecification.html>`_
is pretty simple.
Master/Slave Replication
------------------------

Redis supports a very simple and fast Master/Slave replication. Is
so simple it takes only one line in the
`configuration file <Configuration.html>`_ to set it up, and 21
seconds for a Slave to complete the initial sync of 10 MM key set
in a Amazon EC2 instance.
Read more about Master/Slave `Replication <Replication.html>`_.
Sharding
--------

Distributing the dataset across multiple Redis instances is easy in
Redis, as in any other key-value store. And this depends basically
on the `Languages <Supported.html>`_ client libraries being able to
do so.
Read more about `Sharding <Sharding.html>`_ if you want to know
more abour distributing data and workload in Redis.
Hot Backups
-----------

TODO
Simple to Install, Setup and Manage
-----------------------------------

Installing Redis requires little more than downloading it,
uncompressing it and running make. Management is near zero, so you
can start using Redis in a matter of minutes.
Go on and read about Redis `installation <Installation.html>`_, its
`Setup <Setup.html>`_ and `Management <Management.html>`_.
Portable
--------

Redis is written in ANSI C and works in most POSIX systems like
Linux, BSD, Mac OS X, Solaris, and so on. Redis is reported to
compile and work under WIN32 if compiled with Cygwin, but there is
no official support for Windows currently.
Liberal Licensing
-----------------

Redis is free software released under the very liberal BSD license.
What's next?
------------

Want to get started with Redis? Try the
`Quick Start <QuickStart.html>`_ you will be up and running in just
a matter of minutes.
Check the `Code Samples <CodeSamples.html>`_ and find how you can
use Redis with your favorite programming language.
`Compare <Comparisons.html>`_ Redis with other key-value stores,
like Tokyo Cabinet or Memcached.
.. |Redis Documentation| image:: redis.png