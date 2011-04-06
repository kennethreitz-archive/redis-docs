`|Redis Documentation| <index.html>`_
**BlpopCommand: Contents**
  `BLPOP \_key1\_ \_key2\_ ... \_keyN\_ \_timeout\_ (Redis > <#BLPOP%20_key1_%20_key2_%20...%20_keyN_%20_timeout_%20(Redis%20%3E>`_
  `BRPOP \_key1\_ \_key2\_ ... \_keyN\_ \_timeout\_ (Redis > <#BRPOP%20_key1_%20_key2_%20...%20_keyN_%20_timeout_%20(Redis%20%3E>`_
    `Non blocking behavior <#Non%20blocking%20behavior>`_
    `Blocking behavior <#Blocking%20behavior>`_
    `Multiple clients blocking for the same keys <#Multiple%20clients%20blocking%20for%20the%20same%20keys>`_
    `blocking POP inside a MULTI/EXEC transaction <#blocking%20POP%20inside%20a%20MULTI/EXEC%20transaction>`_
    `Return value <#Return%20value>`_
BlpopCommand
============

ï»¿#sidebar `ListCommandsSidebar <ListCommandsSidebar.html>`_
BLPOP \_key1\_ \_key2\_ ... \_keyN\_ \_timeout\_ (Redis >
=========================================================

1.3.1) =
BRPOP \_key1\_ \_key2\_ ... \_keyN\_ \_timeout\_ (Redis >
=========================================================

1.3.1) = *Time complexity: O(1)*
    BLPOP (and BRPOP) is a blocking list pop primitive. You can see
    this commandsas blocking versions of `LPOP <LpopCommand.html>`_ and
    `RPOP <LpopCommand.html>`_ able toblock if the specified keys don't
    exist or contain empty lists.

    The following is a description of the exact semantic. We describe
    BLPOP butthe two commands are identical, the only difference is
    that BLPOP pops theelement from the left (head) of the list, and
    BRPOP pops from the right (tail).

Non blocking behavior
---------------------

    When BLPOP is called, if at least one of the specified keys contain
    a nonempty list, an element is popped from the head of the list and
    returned tothe caller together with the name of the key (BLPOP
    returns a two elementsarray, the first element is the key, the
    second the popped value).

    Keys are scanned from left to right, so for instance if youissue
    **BLPOP list1 list2 list3 0** against a dataset where **list1**
    does notexist but **list2** and **list3** contain non empty lists,
    BLPOP guaranteesto return an element from the list stored at
    **list2** (since it is the firstnon empty list starting from the
    left).

Blocking behavior
-----------------

    If none of the specified keys exist or contain non empty lists,
    BLPOPblocks until some other client performs a
    `LPUSH <RpushCommand.html>`_ oran `RPUSH <RpushCommand.html>`_
    operation against one of the lists.

    Once new data is present on one of the lists, the client finally
    returnswith the name of the key unblocking it and the popped
    value.

    When blocking, if a non-zero timeout is specified, the client will
    unblockreturning a nil special value if the specified amount of
    seconds passedwithout a push operation against at least one of the
    specified keys.

    The timeout argument is interpreted as an integer value. A timeout
    of zero means instead to block forever.

Multiple clients blocking for the same keys
-------------------------------------------

    Multiple clients can block for the same key. They are put intoa
    queue, so the first to be served will be the one that started to
    waitearlier, in a first-blpopping first-served fashion.

blocking POP inside a MULTI/EXEC transaction
--------------------------------------------

    BLPOP and BRPOP can be used with pipelining (sending multiple
    commands and reading the replies in batch), but it does not make
    sense to use BLPOP or BRPOP inside a MULTI/EXEC block (a Redis
    transaction).

    The behavior of BLPOP inside MULTI/EXEC when the list is empty is
    to return a multi-bulk nil reply, exactly what happens when the
    timeout is reached. If you like science fiction, think at it like
    if inside MULTI/EXEC the time will flow at infinite speed :)

Return value
------------

    BLPOP returns a two-elements array via a multi bulk reply in order
    to returnboth the unblocking key and the popped value.

    When a non-zero timeout is specified, and the BLPOP operation timed
    out,the return value is a nil multi bulk reply. Most client values
    will returnfalse or nil accordingly to the programming language
    used.

`Multi bulk reply <ReplyTypes.html>`_
.. |Redis Documentation| image:: redis.png