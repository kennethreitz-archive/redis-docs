`|Redis Documentation| <index.html>`_
**Comparisons: Contents**
    `Memcached <#Memcached>`_
    `Tokyo Cabinet / Toyo Tyrant <#Tokyo%20Cabinet%20/%20Toyo%20Tyrant>`_
Comparisons
===========

ï»¿if your are asking yourself how is Redis different fom other
key-value stores here you will find it compared to some of the most
popular contendors (all great software) in this category.
Memcached
---------


-  Memcached is not persistent, it just holds everything in memory
   without saving since its main goal is to be used as a cache, while
   Redis is `persistent <Persistence.html>`_.


-  Like memcached Redis uses a key-value model, but while keys can
   just be strings, values in Redis can be `Lists <Lists.html>`_,
   `Sets <Sets.html>`_ or `SortedSets <SortedSets.html>`_ and complex
   operations like intersections, set/get n-th element of lists,
   pop/push of elements, can be performed against sets and lists.

Tokyo Cabinet / Toyo Tyrant
---------------------------

Redis and Tokyo Cabinet can be used for the same applications, but
actually they are *very different* beasts. If you read Twitter
messages of people involved in scalable things both products are
reported to work well, but surely there are times where one or the
other can be the best choice.

-  Tokyo Cabinet writes synchronously on disk, Redis takes the
   whole dataset on memory and writes on disk asynchronously. Tokyo
   Cabinet is safer and probably a better idea if your dataset is
   going to be bigger than RAM, but Redis is faster (note that Redis
   supports master-slave replication that is trivial to setup, so you
   are safe anyway if you want a setup where data can't be lost even
   after a disaster).


-  Redis supports higher level operations and data structures.
   Tokyo Cabinet supports a kind of database that is able to organize
   data into rows with named fields (in a way very similar to Berkeley
   DB) but can't do things like server side List and Set operations
   Redis is able to do: pushing or popping from Lists in an atomic
   way, in O(1) time complexity, server side Set intersections,
   Sorting of schema free data in complex ways (By the way TC supports
   sorting in the table-based database format). Redis on the other
   hand does not support the abstraction of tables with fields, the
   idea is that you can build this stuff in software easily if you
   really need a table-alike approach.


-  Tokyo Cabinet does not implement a networking layer. You have to
   use a networking layer called Tokyo Tyrant that interfaces to Tokyo
   Cabinet so you can talk to Tokyo Cabinet in a client-server
   fashion. In Redis the networking support is built-in inside the
   server, and is basically the only interface between the external
   world and the dataset.


-  Redis is reported to be much faster, especially if you plan to
   access Tokyo Cabinet via Tokyo Tyrant. Here I can only say that
   with Redis you can expect 100,000 operations/seconds with a normal
   Linux box and 50 concurrent clients. You should test Redis, Tokyo,
   and the other alternatives with your specific work load to get a
   feeling about performances for your application.


-  Redis is not an on-disk DB engine like Tokyo: the latter can be
   used as a fast DB engine in your C project without the networking
   overhead just linking to the library. Still in many scalable
   applications you need multiple servers talking with multiple
   clients, so the client-server model is almost always needed, this
   is why in Redis this is built-in.

.. |Redis Documentation| image:: redis.png