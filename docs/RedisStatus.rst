`|Redis Documentation| <index.html>`_
**RedisStatus: Contents**
  `Redis Status Page <#Redis%20Status%20Page>`_
  `How stable are the alpha previews? <#How%20stable%20are%20the%20alpha%20previews?>`_
  `How to obtain a 2.2-alpha preview <#How%20to%20obtain%20a%202.2-alpha%20preview>`_
  `ETA for Redis 2.2? <#ETA%20for%20Redis%202.2?>`_
  `When will we be able to see a working version of Redis Cluster? <#When%20will%20we%20be%20able%20to%20see%20a%20working%20version%20of%20Redis%20Cluster?>`_
RedisStatus
===========

Redis Status Page
=================

Hello! Redis uses versions composed of three numbers separated by a
dot: **major**.**minor**.**patchlevel**.
When the **minor** is an odd number, it is used for an unstable
release, so stable releases are for instance 1.2, 2.0, and so
forth.
This is the status of the different Redis versions currently
available:

-  1.2 is the **legacy redis stable release**, now it is completely
   obsoleted by Redis 2.0. Redis 2.0 is almost completely back
   compatible with 1.2 so upgrading is usually not a problem. Still
   1.2 is believed to be a very stable release that works well, so if
   you are using it in production with code that probably will not
   modified to use more advanced Redis features available in 2.0, it
   makes sense to take 1.2 running. For everything new, it's better to
   start with 2.0.


-  2.0 is the current **stable release**. It is better than 1.2 in
   more or less everything: more features, more mature code, better
   replication, better persistence, and so forth. It is currently what
   most users should use, unless they really need features that are
   only available into an **unstable** release.


-  2.1 is the current **unstable release**, and there are no tar.gz
   for this release, you need to download it from git. **Warning:**
   the master branch in git may work most of the time but is NOT what
   you should use. What's better instead is to use the 2.2-alpha tags:
   every time Redis 2.1.x is stable enough and the new features merged
   passed all the tests for a couple of weeks, and we didn't received
   severe bug reports from users, we tag master as 2.2-alpha *number*,
   where *number* is simply a progressive number. Just pick this
   number.

How stable are the alpha previews?
==================================

Well it is surely ok for development, but it is not recommended for
production. Still there are many users that trust Redis development
process so much to use alpha releases in production, but this is up
to you, we don't give any guarantee ;)
How to obtain a 2.2-alpha preview
=================================

Simply using git:
::

    $ git clone git://github.com/antirez/redis.git
    Initialized empty Git repository in /tmp/redis/.git/
    ...

Then you can list all the branches matching 2.1-alpha with:
::

    cd redis
    $ git tag | grep 2.2-alpha
    2.2-alpha0
    2.2-alpha1
    2.2-alpha2

At this point you can just use **git checkout *tagname***,
substituting *tagname* with 2.2-alphaX where X is the greater
progressive number you see in the listing.
ETA for Redis 2.2?
==================

Redis 2.2 is planned to enter the release candidate stage before
the end of the 2010.
When will we be able to see a working version of Redis Cluster?
===============================================================

I'm already working at it, I mean not just designing, but writing
code. In three months we should have some kind of experimental
version, while in six months we should have the first release
candidate.
Probably the first **stable** release of Redis with working cluster
will be called 3.0, but I'll try to merge it into 2.2 as an
experimental support if we'll be sure there is no impact in the
stability of the system when clustering is not used.
.. |Redis Documentation| image:: redis.png