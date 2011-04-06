`|Redis Documentation| <index.html>`_
**ReplyTypes: Contents**
  `Redis Reply Types <#Redis%20Reply%20Types>`_
  `Status code reply <#Status%20code%20reply>`_
  `Error reply <#Error%20reply>`_
  `Integer reply <#Integer%20reply>`_
  `Bulk reply <#Bulk%20reply>`_
  `Multi bulk reply <#Multi%20bulk%20reply>`_
ReplyTypes
==========

Redis Reply Types
=================

Redis commands can reply to the client with four different kind of
replies, you can find the protocol level specification of this
replies in the
`Redis Protocol Specification <ProtocolSpecification.html>`_. This
page is instead an higher level description of the four types of
replies from the point of view of the final user.
Status code reply
=================

Status code replies are single line strings having the **+**
character as first byte. The string to return to the client is
simply verything that follows the first **+** character. For
example the `PING <PingCommand.html>`_ command returns **+PONG**,
that is the string "PONG".
Error reply
===========

This is like a status code reply but the first character is **-**
instead of **+**. The client library should raise an error for
error replies and stop the execution of the program if the
exception is not trapped, showing the error message (everything
following the first **-** character). An example of error is
"-Error no such key" or "-foobar". Note that error replies will not
collide with negative integer replies since integer replies are
prefixed with the **:** character.
Integer reply
=============

At protocol level integer replies are single line replies in form
of a decimal singed number prefixed by a **:** character. For
example **:10** is an integer reply. Redis commands returning
*true* or *false* will use an integer reply with 0 or 1 as values
where 0 is false and 1 is true.
Integer replies are usually passed by client libraries as integer
values.
Bulk reply
==========

A bulk reply is a binary-safe reply that is used to return a binary
safe single string value (string is not limited to alphanumerical
strings, it may contain binary data of any kind). Client libraries
will usually return a string as return value of Redis commands
returning bulk replies. There is a special bulk reply that signal
that the element does not exist. When this happens the client
library should return 'nil', 'false', or some other special element
that can be distinguished by an empty string.
Multi bulk reply
================

While a bulk reply returns a single string value, multi bulk
replies are used to return multiple values: lists, sets, and so on.
Elements of a bulk reply can be missing. Client libraries should
return 'nil' or 'false' in order to make this elements
distinguishable from empty strings. Client libraries should return
multi bulk replies that are about ordered elements like list ranges
as lists, and bulk replies about sets as hashes or Sets if the
implementation language has a Set type.
.. |Redis Documentation| image:: redis.png