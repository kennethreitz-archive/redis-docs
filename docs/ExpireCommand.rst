`|Redis Documentation| <index.html>`_
**ExpireCommand: Contents**
  `EXPIRE \_key\_ \_seconds\_ <#EXPIRE%20_key_%20_seconds_>`_
  `EXPIREAT \_key\_ \_unixtime\_ (Redis > <#EXPIREAT%20_key_%20_unixtime_%20(Redis%20%3E>`_
  `PERSIST \_key\_ (Redis > <#PERSIST%20_key_%20(Redis%20%3E>`_
    `How the expire is removed from a key <#How%20the%20expire%20is%20removed%20from%20a%20key>`_
    `Restrictions with write operations against volatile keys <#Restrictions%20with%20write%20operations%20against%20volatile%20keys>`_
    `Restrictions for write operations with volatile keys as sources <#Restrictions%20for%20write%20operations%20with%20volatile%20keys%20as%20sources>`_
    `Setting the timeout again on already volatile keys <#Setting%20the%20timeout%20again%20on%20already%20volatile%20keys>`_
    `Enhanced Lazy Expiration algorithm <#Enhanced%20Lazy%20Expiration%20algorithm>`_
      `Version 1.0 <#Version%201.0>`_
      `Version 1.1 <#Version%201.1>`_
    `Return value <#Return%20value>`_
    `FAQ: Can you explain better why Redis < 2.1.3 deletes keys with an EXPIRE on write operations? <#FAQ:%20Can%20you%20explain%20better%20why%20Redis%20%3C%202.1.3%20deletes%20keys%20with%20an%20EXPIRE%20on%20write%20operations?>`_
    `FAQ: How this limitations were solved in Redis versions > 2.1.3? <#FAQ:%20How%20this%20limitations%20were%20solved%20in%20Redis%20versions%20%3E%202.1.3?>`_
ExpireCommand
=============

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
EXPIRE \_key\_ \_seconds\_
==========================

EXPIREAT \_key\_ \_unixtime\_ (Redis >
======================================

1.1)=
PERSIST \_key\_ (Redis >
========================

2.1.3) = *Time complexity: O(1)*
    Set a timeout on the specified key. After the timeout the key will
    beautomatically deleted by the server. A key with an associated
    timeout issaid to be *volatile* in Redis terminology.

    Voltile keys are stored on disk like the other keys, the timeout is
    persistenttoo like all the other aspects of the dataset. Saving a
    dataset containingexpires and stopping the server does not stop the
    flow of time as Redisstores on disk the time when the key will no
    longer be available as Unixtime, and not the remaining seconds.

    EXPIREAT works exctly like EXPIRE but instead to get the number of
    secondsrepresenting the Time To Live of the key as a second
    argument (that is arelative way of specifing the TTL), it takes an
    absolute one in the form ofa UNIX timestamp (Number of seconds
    elapsed since 1 Gen 1970).

    EXPIREAT was introduced in order to implement
    `the Append Only File persistence mode <AppendOnlyFileHowto.html>`_so
    that EXPIRE commands are automatically translated into EXPIREAT
    commands for the append only file. Of course EXPIREAT can alsoused
    by programmers that need a way to simply specify that a given key
    should expire at a given time in the future.

    Since Redis 2.1.3 you can update the value of the timeout of a key
    alreadyhaving an expire set. It is also possible to undo the expire
    at allturning the key into a normal key using the PERSIST command.

How the expire is removed from a key
------------------------------------

    When the key is set to a new value using the SET command, or when a
    keyis destroied via DEL, the timeout is removed from the key.

Restrictions with write operations against volatile keys
--------------------------------------------------------

    IMPORTANT: Since Redis 2.1.3 or greater, there are no restrictions
    aboutthe operations you can perform against volatile keys, however
    older versionsof Redis, including the current stable version 2.0.0,
    has the followinglimitations:

    Write operations like LPUSH, LSET and every other command that has
    theeffect of modifying the value stored at a volatile key have a
    special semantic:basically a volatile key is destroyed when it is
    target of a write operation.See for example the following usage
    pattern:

::

    % ./redis-cli lpush mylist foobar /Users/antirez/hack/redis
    OK
    % ./redis-cli lpush mylist hello  /Users/antirez/hack/redis
    OK
    % ./redis-cli expire mylist 10000 /Users/antirez/hack/redis
    1
    % ./redis-cli lpush mylist newelement
    OK
    % ./redis-cli lrange mylist 0 -1  /Users/antirez/hack/redis
    1. newelement

    What happened here is that LPUSH against the key with a timeout set
    deletedthe key before to perform the operation. There is so a
    simple rule, writeoperations against volatile keys will destroy the
    key before to perform theoperation. Why Redis uses this behavior?
    In order to retain an importantproperty: a server that receives a
    given number of commands in the samesequence will end with the same
    dataset in memory. Without the delete-on-writesemantic what happens
    is that the state of the server depends on the timethe commands
    were issued. This is not a desirable property in a distributed
    databasethat supports replication.

Restrictions for write operations with volatile keys as sources
---------------------------------------------------------------

Even when the volatile key is not modified as part of a write
operation, if it is read in a composite write operation (such as
SINTERSTORE) it will be cleared at the start of the operation. This
is done to avoid concurrency issues in replication. Imagine a key
that is about to expire and the composite operation is run against
it. On a slave node, this key might already be expired, which
leaves you with a desync in your dataset.
Setting the timeout again on already volatile keys
--------------------------------------------------

    Trying to call EXPIRE against a key that already has an associated
    timeoutwill not change the timeout of the key, but will just return
    0. If insteadthe key does not have a timeout associated the timeout
    will be set and EXPIREwill return 1.

Enhanced Lazy Expiration algorithm
----------------------------------

    Redis does not constantly monitor keys that are going to be
    expired.Keys are expired simply when some client tries to access a
    key, andthe key is found to be timed out.

    Of course this is not enough as there are expired keys that will
    neverbe accessed again. This keys should be expired anyway, so once
    everysecond Redis test a few keys at random among keys with an
    expire set.All the keys that are already expired are deleted from
    the keyspace.

Version 1.0
~~~~~~~~~~~

    Each time a fixed number of keys where tested (100 by default). So
    ifyou had a client setting keys with a very short expire faster
    than 100for second the memory continued to grow. When you stopped
    to insertnew keys the memory started to be freed, 100 keys every
    second in thebest conditions. Under a peak Redis continues to use
    more and more RAMeven if most keys are expired in each sweep.

Version 1.1
~~~~~~~~~~~

    Each time Redis:


#. Tests 100 random keys from expired keys set.
#. Deletes all the keys found expired.
#. If more than 25 keys were expired, it start again from 1.

    This is a trivial probabilistic algorithm, basically the assumption
    isthat our sample is representative of the whole key space,and we
    continue to expire until the percentage of keys that are likelyto
    be expired is under 25%

    This means that at any given moment the maximum amount of keys
    alreadyexpired that are using memory is at max equal to max setting
    operations per second divided by 4.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically:
::

    1: the timeout was set.
    0: the timeout was not set since the key already has an associated timeout
       (this may happen only in Redis versions < 2.1.3, Redis >= 2.1.3 will
       happily update the timeout), or the key does not exist.

FAQ: Can you explain better why Redis < 2.1.3 deletes keys with an EXPIRE on write operations?
----------------------------------------------------------------------------------------------

Ok let's start with the problem:
::

    redis> set a 100
    OK
    redis> expire a 360
    (integer) 1
    redis> incr a
    (integer) 1

I set a key to the value of 100, then set an expire of 360 seconds,
and then incremented the key (before the 360 timeout expired of
course). The obvious result would be: 101, instead the key is set
to the value of 1. Why? There is a very important reason involving
the Append Only File and Replication. Let's rework a bit our
example adding the notion of time to the mix:
::

    SET a 100
    EXPIRE a 5
    ... wait 10 seconds ...
    INCR a

Imagine a Redis version that does not implement the "Delete keys
with an expire set on write operation" semantic. Running the above
example with the 10 seconds pause will lead to 'a' being set to the
value of 1, as it no longer exists when INCR is called 10 seconds
later.
Instead if we drop the 10 seconds pause, the result is that 'a' is
set to 101.
And in the practice timing changes! For instance the client may
wait 10 seconds before INCR, but the sequence written in the Append
Only File (and later replayed-back as fast as possible when Redis
is restarted) will not have the pause. Even if we add a timestamp
in the AOF, when the time difference is smaller than our timer
resolution, we have a race condition.
The same happens with master-slave replication. Again, consider the
example above: the client will use the same sequence of commands
without the 10 seconds pause, but the replication link will slow
down for a few seconds due to a network problem. Result? The master
will contain 'a' set to 101, the slave 'a' set to 1.
The only way to avoid this but at the same time have reliable non
time dependent timeouts on keys is to destroy volatile keys when a
write operation is attempted against it.
After all Redis is one of the rare fully persistent databases that
will give you EXPIRE. This comes to a cost :)
FAQ: How this limitations were solved in Redis versions > 2.1.3?
----------------------------------------------------------------

Since Redis 2.1.3 there are no longer restrictions in the use you
can do of write commands against volatile keys, still the
replication and AOF file are guaranteed to be fully consistent.
In order to obtain a correct behavior without sacrificing
consistency now when a key expires, a DEL operation is synthesized
in both the AOF file and against all the attached slaves. This way
the expiration process is centralized in the master instance, and
there is no longer a chance of consistency errors.
However while the slaves while connected to a master will not
expire keys independently, they'll still take the full state of the
expires existing in the dataset, so when a slave is elected to a
master it will be able to expire the keys independently, fully
acting as a master.
.. |Redis Documentation| image:: redis.png