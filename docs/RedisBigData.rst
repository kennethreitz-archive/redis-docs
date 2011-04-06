`|Redis Documentation| <index.html>`_
**RedisBigData: Contents**
    `BGSAVE and BGREWRITEAOF blocking fork() call <#BGSAVE%20and%20BGREWRITEAOF%20blocking%20fork()%20call>`_
    `Using multiple cores <#Using%20multiple%20cores>`_
    `Splitting data into multiple instances <#Splitting%20data%20into%20multiple%20instances>`_
    `BGSAVE / AOFSAVE memory usage, and copy on write <#BGSAVE%20/%20AOFSAVE%20memory%20usage,%20and%20copy%20on%20write>`_
    `BGSAVE / AOFSAVE time for big datasets <#BGSAVE%20/%20AOFSAVE%20time%20for%20big%20datasets>`_
    `Non blocking hash table <#Non%20blocking%20hash%20table>`_
RedisBigData
============

ï»¿=Redis Big Data: facts and guidelines=
BGSAVE and BGREWRITEAOF blocking fork() call
--------------------------------------------

::

    fork.c && ./a.out
    allocated:     1 MB, fork() took 0.000
    allocated:    10 MB, fork() took 0.001
    allocated:   100 MB, fork() took 0.007
    allocated:  1000 MB, fork() took 0.059
    allocated: 10000 MB, fork() took 0.460
    allocated: 20000 MB, fork() took 0.895
    allocated: 30000 MB, fork() took 1.327
    allocated: 40000 MB, fork() took 1.759
    allocated: 50000 MB, fork() took 2.190
    allocated: 60000 MB, fork() took 2.621
    allocated: 70000 MB, fork() took 3.051
    allocated: 80000 MB, fork() took 3.483
    allocated: 90000 MB, fork() took 3.911
    allocated: 100000 MB, fork() took 4.340
    allocated: 110000 MB, fork() took 4.770
    allocated: 120000 MB, fork() took 5.202

Using multiple cores
--------------------

Splitting data into multiple instances
--------------------------------------

BGSAVE / AOFSAVE memory usage, and copy on write
------------------------------------------------

BGSAVE / AOFSAVE time for big datasets
--------------------------------------

Non blocking hash table
-----------------------

.. |Redis Documentation| image:: redis.png