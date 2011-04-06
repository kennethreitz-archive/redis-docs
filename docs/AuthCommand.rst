`|Redis Documentation| <index.html>`_
**AuthCommand: Contents**
  `AUTH \_password\_ <#AUTH%20_password_>`_
    `Return value <#Return%20value>`_
AuthCommand
===========

ï»¿#sidebar
`ConnectionHandlingSidebar <ConnectionHandlingSidebar.html>`_
AUTH \_password\_
=================

    Request for authentication in a password protected Redis server.A
    Redis server can be instructed to require a password before to
    allow clientsto issue commands. This is done using the
    *requirepass* directive in theRedis configuration file.

    If the password given by the client is correct the server replies
    withan OK status code reply and starts accepting commands from the
    client.Otherwise an error is returned and the clients needs to try
    a new password.Note that for the high performance nature of Redis
    it is possible to trya lot of passwords in parallel in very short
    time, so make sure to generatea strong and very long password so
    that this attack is infeasible.

Return value
------------

`Status code reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png