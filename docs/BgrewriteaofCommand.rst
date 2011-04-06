
BGREWRITEAOF
~~~~~~~~~~~~

    Please for detailed information about the Redis Append Only File
    check`the Append Only File Howto <AppendOnlyFileHowto.html>`_.

    BGREWRITEAOF rewrites the Append Only File in background when it
    gets toobig. The Redis Append Only File is a Journal, so every
    operation modifyingthe dataset is logged in the Append Only File
    (and replayed at startup).This means that the Append Only File
    always grows. In order to rebuildits content the BGREWRITEAOF
    creates a new version of the append only filestarting directly form
    the dataset in memory in order to guarantee thegeneration of the
    minimal number of commands needed to rebuild the database.

    The `Append Only File Howto <AppendOnlyFileHowto.html>`_ contains
    further details.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png