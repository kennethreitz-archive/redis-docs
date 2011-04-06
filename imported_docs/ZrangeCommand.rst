`|Redis Documentation| <index.html>`_
**ZrangeCommand: Contents**
  `ZRANGE \_key\_ \_start\_ \_end\_ \`[\`WITHSCORES\`]\`(Redis > <#ZRANGE%20_key_%20_start_%20_end_%20%60[%60WITHSCORES%60]%60(Redis%20%3E>`_
  `ZREVRANGE \_key\_ \_start\_ \_end\_ \`[\`WITHSCORES\`]\` (Redis > <#ZREVRANGE%20_key_%20_start_%20_end_%20%60[%60WITHSCORES%60]%60%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZrangeCommand
=============

ï»¿#sidebar
`SortedSetCommandsSidebar <SortedSetCommandsSidebar.html>`_
ZRANGE \_key\_ \_start\_ \_end\_ \`[\`WITHSCORES\`]\`(Redis >
=============================================================

1.1) =
ZREVRANGE \_key\_ \_start\_ \_end\_ \`[\`WITHSCORES\`]\` (Redis >
=================================================================

1.1) =
*Time complexity: O(log(N))+O(M) (with N being the number of elements in the sorted set and M the number of elements requested)*
    Return the specified elements of the sorted set at the
    specifiedkey. The elements are considered sorted from the lowerest
    to the highestscore when using ZRANGE, and in the reverse order
    when using ZREVRANGE.Start and end are zero-based indexes. 0 is the
    first elementof the sorted set (the one with the lowerest score
    when using ZRANGE), 1the next element by score and so on.

    \_start\_ and *end* can also be negative numbers indicating
    offsetsfrom the end of the sorted set. For example -1 is the last
    element ofthe sorted set, -2 the penultimate element and so on.

    Indexes out of range will not produce an error: if start is overthe
    end of the sorted set, or start ``>`` end, an empty list is
    returned.If end is over the end of the sorted set Redis will threat
    it just likethe last element of the sorted set.

    It's possible to pass the WITHSCORES option to the command in order
    to return notonly the values but also the scores of the elements.
    Redis will return the dataas a single list composed of
    value1,score1,value2,score2,...,valueN,scoreN but clientlibraries
    are free to return a more appropriate data type (what we think is
    thatthe best return type for this command is a Array of
    two-elements Array / Tuple inorder to preserve sorting).

Return value
------------

`Multi bulk reply <ReplyTypes.html>`_, specifically a list of
elements in the specified range.
.. |Redis Documentation| image:: redis.png