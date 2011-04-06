`|Redis Documentation| <index.html>`_
**Credits: Contents**
  `Credits <#Credits>`_
Credits
=======

Credits
=======


-  The Redis server was designed and written by
   `Salvatore Sanfilippo (aka antirez) <http://invece.org>`_
-  `Ezra Zygmuntowicz (aka ezmobius) <http://brainspl.at/>`_ - Ruby
   client lib initial version and hacking
-  `Ludovico Magnocavallo (aka ludo) <http://qix.it>`_ - Python
   clinet lib
-  `Valentino Volonghi of Adroll <http://www.adroll.com/>`_ -
   Erlang client lib
-  **brettbender** - found and fixed a bug in sds.c that caused the
   server to crash at least on 64 bit systems, and anyway to be buggy
   since we used the same vararg thing against vsprintf without to
   call va\_start and va\_end every time.
-  `Dobrica Pavlinusic <http://www.rot13.org/~dpavlin>`_ - Perl
   client lib
-  Brian Hammond - AUTH command implementation, C++ client lib
-  `Daniele Alessandri <http://www.clorophilla.net/>`_ - Lua client
   lib
-  Corey Stup - C99 cleanups
-  Taylor Weibley - Ruby client improvements
-  Bob Potter - Rearrange redisObject struct to reduce memory usage
   in 64bit environments
-  Luca Guidi and Brian McKinney - Ruby client improvements
-  Aman Gupta - SDIFF / SDIFFSTORE, other Set operations
   improvements, ability to disable clients timeout.
-  Diego Rosario Brogna - Code and ideas about dumping backtrace on
   sigsegv and similar error conditions.

p.s. sorry to take this file in sync is hard in this early days.
Please drop me an email if I forgot to add your name here!
.. |Redis Documentation| image:: redis.png