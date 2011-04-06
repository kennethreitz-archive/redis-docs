`|Redis Documentation| <index.html>`_
**EventLibray: Contents**
  `Event Library <#Event%20Library>`_
    `Why is an Event Library needed at all? <#Why%20is%20an%20Event%20Library%20needed%20at%20all?>`_
EventLibray
===========

Event Library
=============

Why is an Event Library needed at all?
--------------------------------------

Let us figure it out through a series of Q&As.
Q: What do you expect a network server to be doing all the time?
<br/> A: Watch for inbound connections on the port its listening
and accept them.
Q: Calling `accept <http://man.cx/accept(2)>`_ yields a descriptor.
What do I do with it?<br/> A: Save the descriptor and do a
non-blocking read/write operation on it.
Q: Why does the read/write have to be non-blocking?<br/> A: If the
file operation ( even a socket in Unix is a file ) is blocking how
could the server for example accept other connection requests when
its blocked in a file I/O operation.
Q: I guess I have to do many such non-blocking operations on the
socket to see when it's ready. Am I right?<br/> A: Yes. That is
what an event library does for you. Now you get it.
Q: How do Event Libraries do what they do?<br/> A: They use the
operating system's
`polling <http://www.devshed.com/c/a/BrainDump/Linux-Files-and-the-Event-Poll-Interface/>`_
facility along with timers.
Q: So are there any open source event libraries that do what you
just described? <br/> A: Yes. Libevent and Libev are two such event
libraries that I can recall off the top of my head.
Q: Does Redis use such open source event libraries for handling
socket I/O?<br/> A: No. For various
`reasons <http://groups.google.com/group/redis-db/browse_thread/thread/b52814e9ef15b8d0/>`_
Redis uses its own event library.
.. |Redis Documentation| image:: redis.png