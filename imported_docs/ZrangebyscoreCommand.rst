`|Redis Documentation| <index.html>`_
**ZrangebyscoreCommand: Contents**
  `ZRANGEBYSCORE \_key\_ \_min\_ \_max\_ \`[\`LIMIT \_offset\_ \_count\_\`]\` (Redis > <#ZRANGEBYSCORE%20_key_%20_min_%20_max_%20%60[%60LIMIT%20_offset_%20_count_%60]%60%20(Redis%20%3E>`_
  `ZRANGEBYSCORE \_key\_ \_min\_ \_max\_ \`[\`LIMIT \_offset\_ \_count\_\`]\` \`[\`WITHSCORES\`]\` (Redis > <#ZRANGEBYSCORE%20_key_%20_min_%20_max_%20%60[%60LIMIT%20_offset_%20_count_%60]%60%20%60[%60WITHSCORES%60]%60%20(Redis%20%3E>`_
  `ZCOUNT \_key\_ \_min\_ \_max\_ <#ZCOUNT%20_key_%20_min_%20_max_>`_
    `Exclusive intervals and infinity <#Exclusive%20intervals%20and%20infinity>`_
    `Return value <#Return%20value>`_
    `Examples <#Examples>`_
ZrangebyscoreCommand
====================

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
ZRANGEBYSCORE \_key\_ \_min\_ \_max\_ \`[\`LIMIT \_offset\_ \_count\_\`]\` (Redis >
===================================================================================

1.1) =
ZRANGEBYSCORE \_key\_ \_min\_ \_max\_ \`[\`LIMIT \_offset\_ \_count\_\`]\` \`[\`WITHSCORES\`]\` (Redis >
========================================================================================================

1.3.4) =
ZCOUNT \_key\_ \_min\_ \_max\_
==============================

*Time complexity: O(log(N))+O(M) with N being the number of elements in the sorted set and M the number of elements returned by the command, so if M is constant (for instance you always ask for the first ten elements with LIMIT) you can consider it O(log(N))*
    Return the all the elements in the sorted set at key with a score
    between\_min\_ and *max* (including elements with score equal to
    min or max).

    The elements having the same score are returned sorted
    lexicographically asASCII strings (this follows from a property of
    Redis sorted sets and does notinvolve further computation).

    Using the optional LIMIT it's possible to get only a range of the
    matchingelements in an SQL-alike way. Note that if *offset* is
    large the commandsneeds to traverse the list for *offset* elements
    and this adds up to theO(M) figure.

    The **ZCOUNT** command is similar to **ZRANGEBYSCORE** but instead
    of returningthe actual elements in the specified interval, it just
    returns the numberof matching elements.

Exclusive intervals and infinity
--------------------------------

*min* and *max* can be -inf and +inf, so that you are not required
to know what's the greatest or smallest element in order to take,
for instance, elements "up to a given value".
Also while the interval is for default closed (inclusive) it's
possible to specify open intervals prefixing the score with a "("
character, so for instance:
::

    ZRANGEBYSCORE zset (1.3 5

Will return all the values with score **> 1.3 and <= 5**, while for
instance:
::

    ZRANGEBYSCORE zset (5 (10

Will return all the values with score **> 5 and < 10** (5 and 10
excluded).
Return value
------------

ZRANGEBYSCORE returns a `Multi bulk reply <ReplyTypes.html>`_
specifically a list of elements in the specified score range.
ZCOUNT returns a `Integer reply <ReplyTypes.html>`_ specifically
the number of elements matching the specified score range.
Examples
--------

::

    redis> zadd zset 1 foo
    (integer) 1
    redis> zadd zset 2 bar
    (integer) 1
    redis> zadd zset 3 biz
    (integer) 1
    redis> zadd zset 4 foz
    (integer) 1
    redis> zrangebyscore zset -inf +inf
    1. "foo"
    2. "bar"
    3. "biz"
    4. "foz"
    redis> zcount zset 1 2
    (integer) 2
    redis> zrangebyscore zset 1 2
    1. "foo"
    2. "bar"
    redis> zrangebyscore zset (1 2
    1. "bar"
    redis> zrangebyscore zset (1 (2
    (empty list or set)

.. |Redis Documentation| image:: redis.png