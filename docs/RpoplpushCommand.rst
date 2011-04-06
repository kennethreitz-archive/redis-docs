`|Redis Documentation| <index.html>`_
**RpoplpushCommand: Contents**
  `RPOPLPUSH \_srckey\_ \_dstkey\_ (Redis > <#RPOPLPUSH%20_srckey_%20_dstkey_%20(Redis%20%3E>`_
    `Programming patterns: safe queues <#Programming%20patterns:%20safe%20queues>`_
    `Programming patterns: server-side O(N) list traversal <#Programming%20patterns:%20server-side%20O(N)%20list%20traversal>`_
    `Return value <#Return%20value>`_
RpoplpushCommand
================

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
RPOPLPUSH \_srckey\_ \_dstkey\_ (Redis >
========================================

1.1) = *Time complexity: O(1)*
    Atomically return and remove the last (tail) element of the
    *srckey* list,and push the element as the first (head) element of
    the *dstkey* list. Forexample if the source list contains the
    elements "a","b","c" and thedestination list contains the elements
    "foo","bar" after an RPOPLPUSH commandthe content of the two lists
    will be "a","b" and "c","foo","bar".

    If the *key* does not exist or the list is already empty the
    specialvalue 'nil' is returned. If the *srckey* and *dstkey* are
    the same theoperation is equivalent to removing the last element
    from the list and pusingit as first element of the list, so it's a
    "list rotation" command.

Programming patterns: safe queues
---------------------------------

    Redis lists are often used as queues in order to exchange messages
    betweendifferent programs. A program can add a message performing
    an `LPUSH <RpushCommand.html>`_ operationagainst a Redis list (we
    call this program a Producer), while another program(that we call
    Consumer) can process the messages performing an
    `RPOP <LpopCommand.html>`_ commandin order to start reading the
    messages from the oldest.

    Unfortunately if a Consumer crashes just after an
    `RPOP <LpopCommand.html>`_ operation the messagegets lost.
    RPOPLPUSH solves this problem since the returned message isadded to
    another "backup" list. The Consumer can later remove the
    messagefrom the backup list using the `LREM <LremCommand.html>`_
    command when the message was correctlyprocessed.

    Another process, called Helper, can monitor the "backup" list to
    check fortimed out entries to repush against the main queue.

Programming patterns: server-side O(N) list traversal
-----------------------------------------------------

    Using RPOPPUSH with the same source and destination key a process
    canvisit all the elements of an N-elements List in O(N) without to
    transferthe full list from the server to the client in a single
    `LRANGE <LrangeCommand.html>`_ operation.Note that a process can
    traverse the list even while other processesare actively RPUSHing
    against the list, and still no element will be skipped.

Return value
------------

`Bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png