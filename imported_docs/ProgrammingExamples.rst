`|Redis Documentation| <index.html>`_
**ProgrammingExamples: Contents**
  `Programming Examples (DRAFT) <#Programming%20Examples%20(DRAFT)>`_
    `TODO <#TODO>`_
    `Java <#Java>`_
      `Twayis <#Twayis>`_
    `PHP <#PHP>`_
      `Retwis <#Retwis>`_
    `Ruby <#Ruby>`_
      `twatcher-lite <#twatcher-lite>`_
      `Resque <#Resque>`_
      `Retwis-rb <#Retwis-rb>`_
      `scanty-redis <#scanty-redis>`_
      `Note Taking <#Note%20Taking>`_
ProgrammingExamples
===================

Programming Examples (DRAFT)
============================

TODO
----


-  Add
   `http://github.com/jodosha/redis-store <http://github.com/jodosha/redis-store>`_

Nothing speaks better than code examples, here you are:
Java
----

Twayis
~~~~~~

A Java clone of **Retwis** showcase integration between the
`Play! framework <http://www.playframework.org/>`_ and Redis
`Google Code Project Page <http://code.google.com/p/twayis/>`_
PHP
---

Retwis
~~~~~~

A PHP Twitter clone, the original example of Redis capabilities.
With a `live demo <http://retwis.antirez.com/>`_, and an
`article explaining it design <http://code.google.com/p/redis/wiki/TwitterAlikeExample>`_.
You can find the code in the Downloads tab.
Ruby
----

twatcher-lite
~~~~~~~~~~~~~

A simplied version of the application running
`http://twatcher.com/ <http://twatcher.com/>`_ from Mirko Froehlich
(`@digitalhobbit <http://twitter.com/digitalhobbit>`_) with a full
blog post explaining its development at
`Building a Twitter Filter With Sinatra, Redis, and TweetStream <http://www.digitalhobbit.com/2009/11/08/building-a-twitter-filter-with-sinatra-redis-and-tweetstream/>`_
Resque
~~~~~~

The "simple" Redis-based queue behind Github background jobs, that
replaced SQS, Starling, ActiveMessaging, BackgroundJob, DelayedJob,
and Beanstalkd. Developed by Chris Wanstrath
(`@defunkt <http://twitter.com/defunkt>`_) the code is at
`http://github.com/defunkt/resque <http://github.com/defunkt/resque>`_,
be sure to read
`the introduction <http://github.com/blog/542-introducing-resque>`_
Retwis-rb
~~~~~~~~~

A port of **Retwis** to Ruby and
`Sinatra <http://www.sinatrarb.com/>`_ written by Daniel Lucraft
(`@DanLucraft <http://twitter.com/DanLucraft>`_) Full source code
is available at
`http://github.com/danlucraft/retwis-rb <http://github.com/danlucraft/retwis-rb>`_
scanty-redis
~~~~~~~~~~~~

Scanty is *minimal* blogging software developed by Adam Wiggins
(`@hirodusk <http://twitter.com/hirodusk>`_) It is not a blogging
engine, but itâ��s small and easy to modify, so it could be the
starting point for your blog.
`This fork <http://github.com/adamwiggins/scanty-redis>`_ is
modified to use Redis, a full featured key-value database, instead
of SQL.
Note Taking
~~~~~~~~~~~

A *very simple* note taking example of Ruby and Redis application
using `Sinatra <http://www.sinatrarb.com/>`_. Developed by Pieter
Noordhuis `@pnoordhuis <http://twitter.com/pnoordhuis>`_, you can
check the code at
`http://gist.github.com/86714 <http://gist.github.com/86714>`_
.. |Redis Documentation| image:: redis.png