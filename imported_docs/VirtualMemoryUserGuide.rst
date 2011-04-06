`|Redis Documentation| <index.html>`_
**VirtualMemoryUserGuide: Contents**
  `Virtual Memory User Guide <#Virtual%20Memory%20User%20Guide>`_
    `Virtual Memory explained in simple words <#Virtual%20Memory%20explained%20in%20simple%20words>`_
    `When using Virtual Memory is a good idea <#When%20using%20Virtual%20Memory%20is%20a%20good%20idea>`_
  `VM Configuration <#VM%20Configuration>`_
    `The vm-max-memory setting <#The%20vm-max-memory%20setting>`_
    `Configuring the swap file <#Configuring%20the%20swap%20file>`_
    `Threaded VM vs Blocking VM <#Threaded%20VM%20vs%20Blocking%20VM>`_
  `Random things to know <#Random%20things%20to%20know>`_
    `A good place for the swap file <#A%20good%20place%20for%20the%20swap%20file>`_
    `Monitoring the VM <#Monitoring%20the%20VM>`_
    `Redis with VM enabled: better .rdb files or Append Only File? <#Redis%20with%20VM%20enabled:%20better%20.rdb%20files%20or%20Append%20Only%20File?>`_
    `Using as little memory as possible <#Using%20as%20little%20memory%20as%20possible>`_
    `VM Stability <#VM%20Stability>`_
VirtualMemoryUserGuide
======================

ï»¿#sidebar `RedisGuides <RedisGuides.html>`_
Virtual Memory User Guide
=========================

Redis Virtual Memory is a feature that will appear for the first
time in a stable Redis distribution in Redis 2.0. However Virtual
Memory (called VM starting from now) is already available and
stable enough to be tests in the unstable branch of Redis available
`on Git <http://github.com/antirez/redis>`_.
Virtual Memory explained in simple words
----------------------------------------

Redis follows a Key-Value model. You have keys associated with some
values. Usually Redis takes both Keys and associated Values in
memory. Sometimes this is not the best option, and while Keys
**must** be taken in memory for the way Redis is designed (and in
order to ensure fast lookups), Values can be swapped out to disk
when they are rarely used.
In practical terms this means that if you have a dataset of 100,000
keys in memory, but only 10% of this keys are often used, Redis
with Virtual Memory enabled will try to transfer the values
associated to the rarely used keys on disk.
When this values are requested, as a result of a command issued by
a client, the values are loaded back from the swap file to the main
memory.
When using Virtual Memory is a good idea
----------------------------------------

Before using VM you should ask yourself if you really need it.
Redis is a disk backed, in memory database. The right way to use
Redis is almost always to have enough RAM to fit all the data in
memory. Still there are a scenarios where to hold all the data in
memory is not possible:

-  Data access is very biased. Only a small percentage of keys (for
   instance related to active users in your web site) gets the vast
   majority of accesses. At the same time there is too much data per
   key to take everything in memory.
-  There is simply not enough memory available to hold all the data
   in memory, regardless of the data access pattern, and values are
   large. In this configuration Redis can be used as an on-disk DB
   where keys are in memory, so the key lookup is fast, but the access
   to the actual values require accessing the (slower) disk.

An important concept to take in mind is that Redis
**is not able to swap the keys**, so if your memory problems are
related to the fact you have too much keys with very small values,
VM is not the solution.
Instead if a good amount of memory is used because values are
pretty large (for example large strings, lists, sets or hashes with
many elements), then VM can be a good idea.
Sometimes you can turn your "many keys with small values" problem
into a "less keys but with very large values" one just using Hashes
in order to group related data into fields of a single key. For
instance instead of having a key for every attribute of your object
you have a single key per object where Hash fields represent the
different attributes.
VM Configuration
================

Configuring the VM is not hard but requires some care to set the
best parameters accordingly to the requirements.
The VM is enabled and configured editing redis.conf, the first step
is switching it on with:
::

    vm-enabled yes

Many other configuration options are able to change the behavior of
VM. The rule is that you don't want to run with the default
configuration, as every problem and dataset requires some tuning in
order to get the maximum advantages.
The vm-max-memory setting
-------------------------

The **vm-max-memory** setting specifies how much memory Redis is
free to use before starting swapping values on disk.
Basically if this memory limit is still not reached, no object will
be swapped, Redis will work all in memory as usually. Once this
limit is hit, enough objects are swapped out in order to return
just under the limit.
The swapped objects are the one with the highest "age" (that is,
the number of seconds since they are not used in any way) mainly,
but the "swappability" of an object is also proportional to the
logarithm of it's size in memory. So basically older objects are
preferred, but when they are about the same size, bigger objects
are preferred.
**WARNING:** Because keys can't be swapped out, Redis will not be
able to honour the **vm-max-memory** setting if the keys alone are
using more space than the limit.
The best value for this setting is enough RAM in order to hold the
"working set" of data. In practical terms, just give Redis as much
memory as you can, and swapping will work better.
Configuring the swap file
-------------------------

In order to transfer data from memory to disk, Redis uses a swap
file. The swap file has nothing to do with durability of data, and
can be removed when a Redis instance is terminated. Still the swap
file should not be moved, deleted, or altered in any other way
while Redis is running.
Because the Redis swap file is used mostly in a random access
fashion, to put the swap file into a Solid State Disk will lead to
better performances.
The swap file is divided into "pages". A value can be swapped into
one or multiple pages, but a single page can't hold more than a
value.
There is no direct way to tell Redis how much bytes of swap file it
should be using. Instead two different values are configured, that
multiplied together will produce the total number of bytes used.
This two values are the number of pages inside the swap file, and
the page size. It is possible to configure this two parameters in
redis.conf.

-  The **vm-pages** configuration directive is used to set the
   total number of pages in the swap file.
-  the **vm-page-size** configuration directive is used in order to
   set the page size in bytes.

So for instance if the page size is set to the value of 32 bytes,
and the total number of pages is set to 10000000 (10 millions), the
swap file can hold a total of 320 MB of data.
Because a single page can't be used to hold more than a value (but
a value can be stored into multiple pages), care must be taken in
setting this parameters. Usually the best idea is setting the page
size so that the majority of the values can be swapped using a few
pages.
Threaded VM vs Blocking VM
--------------------------

Another very important configuration parameter is
**vm-max-threads**:
::

    # The default vm-max-threads configuration
    vm-max-threads 4

This is the maximum number of threads used in order to perform I/O
from/to the swap file. A good value is just to match the number of
cores in your system.
However the special value of "0" will enable blocking VM. When VM
is configured to be blocking it performs the I/O in a synchronous
blocking way. This is what you can expect from blocking VM:

-  Clients accessing swapped out keys will block other clients
   while reading from disk, so the latency experimented by clients can
   be larger, especially if the disk is slow or busy and/or if there
   are big values swapped on disk.
-  The blocking VM performances are **overall** better, as there is
   no time lost in synchronization, spawning of threads, resuming
   blocked clients waiting for values.

So if you are willing to accept an higher latency from time to
time, blocking VM can be a good pick, especially if swapping
happens rarely as most of your often accessed data happens to fit
in your memory.
If instead you have a lot of swap in and swap out operations and
you have many cores that you want to exploit, and in general when
you don't want that clients dealing with swapped values will block
other clients for a few milliseconds (or more if the swapped value
is very big), then it's better to use threaded VM.
To experiment with your dataset and different configurations is
warmly encouraged...
Random things to know
=====================

A good place for the swap file
------------------------------

In many configurations the swap file can be fairly large, even 40GB
or more. Not all the kind of file systems are able to deal with
large files in a good way, especially Mac OS X file system tends to
be really lame about it.
The suggestion is to use Linux ext3 file system, or any other file
system with good support for **sparse files**. What are sparse
files?
Sparse files are files where a lot of the content happen to be
empty. Advanced file systems like ext2, ext3, ext4, RaiserFS,
Raiser4, and many others, are able to encode this files in a more
efficient way and will allocate more space for the file when
needed, that is, when more actual blocks of the file will be used.
The swap file is obviously pretty sparse, especially if the server
is running since little time or it is much bigger compared to the
amount of data swapped out. A file system not supporting sparse
files can at some point block the Redis process while creating a
very big file at once.
For a list of file systems supporting spare files
`check this Wikipedia page comparing different files systems <http://en.wikipedia.org/wiki/Comparison_of_file_systems>`_.
Monitoring the VM
-----------------

Once you have a Redis system with VM enabled up and running, you
may be very interested in knowing how it's working: how many
objects are swapped in total, the number of objects swapped and
loaded every second, and so forth.
There is an utility that is very handy in checking how the VM is
working, that is part of
`Redis Tools <http://github.com/antirez/redis-tools>`_. This tool
is called redis-stat, and using it is pretty straightforward:
::

    $ ./redis-stat vmstat
     --------------- objects --------------- ------ pages ------ ----- memory -----
     load-in  swap-out  swapped   delta      used     delta      used     delta    
     138837   1078936   800402    +800402    807620   +807620    209.50M  +209.50M  
     4277     38011     829802    +29400     837441   +29821     206.47M  -3.03M   
     3347     39508     862619    +32817     870340   +32899     202.96M  -3.51M   
     4445     36943     890646    +28027     897925   +27585     199.92M  -3.04M   
     10391    16902     886783    -3863     894104   -3821     200.22M  +309.56K  
     8888     19507     888371    +1588      895678   +1574      200.05M  -171.81K 
     8377     20082     891664    +3293      899850   +4172      200.10M  +53.55K   
     9671     20210     892586    +922       899917   +67        199.82M  -285.30K 
     10861    16723     887638    -4948     895003   -4914     200.13M  +312.35K  
     9541     21945     890618    +2980      898004   +3001      199.94M  -197.11K 
     9689     17257     888345    -2273     896405   -1599     200.27M  +337.77K  
     10087    18784     886771    -1574     894577   -1828     200.36M  +91.60K   
     9330     19350     887411    +640       894817   +240       200.17M  -189.72K 

The above output is about a redis-server with VM enable, around 1
million of keys inside, and a lot of simulated load using the
redis-load utility.
As you can see from the output a number of load-in and swap-out
operations are happening every second. Note that the first line
reports the actual values since the server was started, while the
next lines are differences compared to the previous reading.
If you assigned enough memory to hold your working set of data,
probably you should see a lot less dramatic swapping happening, so
redis-stat can be a really valuable tool in order to understand if
you need to shop for RAM ;)
Redis with VM enabled: better .rdb files or Append Only File?
-------------------------------------------------------------

When VM is enabled, saving and loading the database are
**much slower** operations. A DB that usually loads in 2 seconds
takes 13 seconds with VM enabled if the server is configured to use
the smallest memory possible (that is, vm-max-memory set to 0).
So you probably want to switch to a configuration using the Append
Only File for persistence, so that you can perform the BGREWRITEAOF
from time to time.
It is important to note that while a BGSAVE or BGREWRITEAOF is in
progress Redis does **not** swap new values on disk. The VM will be
read-only while there is another child accessing it. So if you have
a lot of writes while there is a child working, the memory usage
may grow.
Using as little memory as possible
----------------------------------

An interesting setup to turn Redis into an on-disk DB with just
keys in memory is setting vm-max-memory to 0. If you don't mind
some latency more and poorer performances but want to use very
little memory for very big values, this is a good setup.
In this setup you should first try setting the VM as blocking
(vm-max-threads 0) as with this configuration and high traffic the
number of swap in and swap out operations will be huge, and
threading will consume a lot of resources compared to a simple
blocking implementation.
VM Stability
------------

VM is still experimental code, but in the latest weeks it was
tested in many ways in development environments, and even in some
production environment. No bugs were noticed during this testing
period. Still the more obscure bugs may happen in non controlled
environments where there are setups that we are not able to
reproduce for some reason.
In this stage you are encouraged to try VM in your development
environment, and even in production if your DB is not mission
critical, but for instance just a big persistent cache of data that
may go away without too much problems.
Please report any problem you will notice to the Redis Google Group
or by IRC joining the #redis IRC channel on freenode.
.. |Redis Documentation| image:: redis.png