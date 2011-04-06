`|Redis Documentation| <index.html>`_
**BrpoplpushCommand: Contents**
  `BRPOPLPUSH \_srckey\_ \_dstkey\_ \_timeout\_ (Redis > <#BRPOPLPUSH%20_srckey_%20_dstkey_%20_timeout_%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
BrpoplpushCommand
=================

BRPOPLPUSH \_srckey\_ \_dstkey\_ \_timeout\_ (Redis >
=====================================================

2.1.8) = *Time complexity: O(1)*
    Blocking version of the `RPOPLPUSH <RpoplpushCommand.html>`_
    command. Atomically removes and returnsthe last element (tail) of
    the source list at *srckey*, and as a side effect pushes the
    returned element in the head of the list at *dstkey*.

If the source list is empty, the client blocks until another client
pushes against the source list. Of course in such a case the push
operation against the destination list will be performed after the
command unblocks detecting a push against the source list.
Note that the command returns an error if the target key already
exists but is not a list. The error is delayed at the time the push
operation is attempted, that is, immediately if the source list is
not empty, or when the first push against the source list happens
in the case the command would block.
The timeout value can be 0 or a positive integer value. When it is
zero the command will block forever, until something is pushed
against *srckey*. Otherwise the command will wait the specified
number of seconds at max, returning an nil value when the timeout
expires.
The source and destination of the list can be the same, having the
effect of rotating the list. Please check
`RPOPLPUSH <RpoplpushCommand.html>`_ for more information.
Return value
------------

`Bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png