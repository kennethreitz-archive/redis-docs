`|Redis Documentation| <index.html>`_
**QuickStart: Contents**
  `Quick Start <#Quick%20Start>`_
    `Obtain the latest version <#Obtain%20the%20latest%20version>`_
    `Compile <#Compile>`_
    `Run the server <#Run%20the%20server>`_
    `Play with the built in client <#Play%20with%20the%20built%20in%20client>`_
    `Further reading <#Further%20reading>`_
QuickStart
==========

ï»¿#sidebar `RedisGuides <RedisGuides.html>`_
Quick Start
===========

This quickstart is a five minutes howto on how to get started with
Redis. For more information on Redis check
`Redis Documentation Index <http://code.google.com/p/redis/wiki/index>`_.
Obtain the latest version
-------------------------

The latest stable source distribution of Redis can be obtained
`at this location as a tarball <http://code.google.com/p/redis/downloads/list>`_.
::

    $ wget http://redis.googlecode.com/files/redis-1.02.tar.gz

The unstable source code, with more features but not ready for
production, can be downloaded using git:
::

    $ git clone git://github.com/antirez/redis.git

Compile
-------

Redis can be compiled in most
`POSIX systems <SupportedPlatforms.html>`_. To compile Redis just
untar the tar.gz, enter the directly and type 'make'.
::

    $ tar xvzf redis-1.02.tar.gz
    $ cd redis-1.02
    $ make

In order to test if the Redis server is working well in your
computer make sure to run ``make test`` and check that all the
tests are passed.
Run the server
--------------

Redis can run just fine without a configuration file (when executed
without a config file a standard configuration is used). To run
Redis just type the following command:
::

    $ ./redis-server

With the `default configuration <Configuration.html>`_ Redis will
log to the standard output so you can check what happens. Later,
you can `change the default settings <Configuration.html>`_.
Play with the built in client
-----------------------------

Redis ships with a command line client that is automatically
compiled when you ran ``make`` and it is called ``redis-cli``For
instance to set a key and read back the value use the following:
::

    $ ./redis-cli set mykey somevalue
    OK
    $ ./redis-cli get mykey
    somevalue

What about adding elements to a `list <Lists.html>`_:
::

    $ ./redis-cli lpush mylist firstvalue
    OK
    $ ./redis-cli lpush mylist secondvalue
    OK
    $ ./redis-cli lpush mylist thirdvalue
    OK
    $ ./redis-cli lrange mylist 0 -1
    1. thirdvalue
    2. secondvalue
    3. firstvalue
    $ ./redis-cli rpop mylist
    firstvalue
    $ ./redis-cli lrange mylist 0 -1
    1. thirdvalue
    2. secondvalue

Further reading
---------------


-  What to play more with Redis? Read
   `Fifteen minutes introduction to Redis data types <IntroductionToRedisDataTypes.html>`_.
-  Check all the `Features <Features.html>`_
-  Read the full list of available commands in the
   `Command Reference <CommandReference.html>`_.
-  Start using Redis from your
   `favorite language <SupportedLanguages.html>`_.
-  Take a look at some
   `Programming Examples <ProgrammingExamples.html>`_.

.. |Redis Documentation| image:: redis.png