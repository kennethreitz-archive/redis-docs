`|Redis Documentation| <index.html>`_
**ConfigCommand: Contents**
  `CONFIG GET \_pattern\_ (Redis > <#CONFIG%20GET%20_pattern_%20(Redis%20%3E>`_
  `CONFIG SET \_parameter\_ \_value\_ (Redis > <#CONFIG%20SET%20_parameter_%20_value_%20(Redis%20%3E>`_
    `CONFIG GET \_pattern\_ <#CONFIG%20GET%20_pattern_>`_
    `CONFIG SET \_parameter\_ \_value\_ <#CONFIG%20SET%20_parameter_%20_value_>`_
    `Parameters value format <#Parameters%20value%20format>`_
    `See Also <#See%20Also>`_
ConfigCommand
=============

ï»¿#sidebar `ControlCommandsSidebar <ControlCommandsSidebar.html>`_
CONFIG GET \_pattern\_ (Redis >
===============================

2.0)=
CONFIG SET \_parameter\_ \_value\_ (Redis >
===========================================

2.0)=
    The CONFIG command is able to retrieve or alter the configuration
    of a runningRedis server. Not all the configuration parameters are
    supported.

    CONFIG has two sub commands, GET and SET. The GET command is used
    to readthe configuration, while the SET command is used to alter
    the configuration.

CONFIG GET \_pattern\_
----------------------

    CONFIG GET returns the current configuration parameters. This sub
    commandonly accepts a single argument, that is glob style pattern.
    All theconfiguration parameters matching this parameter are
    reported as alist of key-value pairs. Example:

::

    $ redis-cli config get '*'
    1. "dbfilename"
    2. "dump.rdb"
    3. "requirepass"
    4. (nil)
    5. "masterauth"
    6. (nil)
    7. "maxmemory"
    8. "0\n"
    9. "appendfsync"
    10. "everysec"
    11. "save"
    12. "3600 1 300 100 60 10000"
    
    $ redis-cli config get 'm*'
    1. "masterauth"
    2. (nil)
    3. "maxmemory"
    4. "0\n"

The return type of the command is a
`bulk reply <ReplyTypes.html>`_.
CONFIG SET \_parameter\_ \_value\_
----------------------------------

    CONFIG SET is used in order to reconfigure the server, setting a
    specificconfiguration parameter to a new value.

    The list of configuration parameters supported by CONFIG SET can
    beobtained issuing a ``CONFIG GET *`` command.

    The configuration set using CONFIG SET is immediately loaded by the
    Redisserver that will start acting as specified starting from the
    next command.

    Example:

::

    $ ./redis-cli 
    redis> set x 10
    OK
    redis> config set maxmemory 200
    OK
    redis> set y 20
    (error) ERR command not allowed when used memory > 'maxmemory'
    redis> config set maxmemory 0
    OK
    redis> set y 20
    OK

Parameters value format
-----------------------

    The value of the configuration parameter is the same as the one of
    thesame parameter in the Redis configuration file, with the
    following exceptions:


-  The ``save`` paramter is a list of space-separated integers.
   Every pair of integers specify the time and number of changes limit
   to trigger a save. For instance the command
   ``CONFIG SET save "3600 10 60 10000"`` will configure the server to
   issue a background saving of the RDB file every 3600 seconds if
   there are at least 10 changes in the dataset, and every 60 seconds
   if there are at least 10000 changes. To completely disable
   automatic snapshots just set the parameter as an empty string.
-  All the integer parameters representing memory are returned and
   accepted only using bytes as unit.

See Also
--------

The `INFO <InfoCommand.html>`_ command can be used in order to read
configuriaton parameters that are not available in the CONFIG
command.
.. |Redis Documentation| image:: redis.png