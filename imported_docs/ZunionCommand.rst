`|Redis Documentation| <index.html>`_
**ZunionCommand: Contents**
  `ZUNIONSTORE \_dstkey\_ \_N\_ \_k1\_ ... \_kN\_ \`[\`WEIGHTS \_w1\_ ... \_wN\_\`]\` \`[\`AGGREGATE SUM\|MIN\|MAX\`]\` (Redis > <#ZUNIONSTORE%20_dstkey_%20_N_%20_k1_%20...%20_kN_%20%60[%60WEIGHTS%20_w1_%20...%20_wN_%60]%60%20%60[%60AGGREGATE%20SUM%7CMIN%7CMAX%60]%60%20%20(Redis%20%3E>`_
  `ZINTERSTORE \_dstkey\_ \_N\_ \_k1\_ ... \_kN\_ \`[\`WEIGHTS \_w1\_ ... \_wN\_\`]\` \`[\`AGGREGATE SUM\|MIN\|MAX\`]\` (Redis > <#ZINTERSTORE%20_dstkey_%20_N_%20_k1_%20...%20_kN_%20%60[%60WEIGHTS%20_w1_%20...%20_wN_%60]%60%20%60[%60AGGREGATE%20SUM%7CMIN%7CMAX%60]%60%20%20(Redis%20%3E>`_
    `Return value <#Return%20value>`_
ZunionCommand
=============

ZUNIONSTORE \_dstkey\_ \_N\_ \_k1\_ ... \_kN\_ \`[\`WEIGHTS \_w1\_ ... \_wN\_\`]\` \`[\`AGGREGATE SUM\|MIN\|MAX\`]\` (Redis >
=============================================================================================================================

1.3.12) =
ZINTERSTORE \_dstkey\_ \_N\_ \_k1\_ ... \_kN\_ \`[\`WEIGHTS \_w1\_ ... \_wN\_\`]\` \`[\`AGGREGATE SUM\|MIN\|MAX\`]\` (Redis >
=============================================================================================================================

1.3.12) =
*Time complexity: O(N) + O(M log(M)) with N being the sum of the sizes of the input sorted sets, and M being the number of elements in the resulting sorted set*
    Creates a union or intersection of *N* sorted sets given by keys
    *k1* through *kN*, and stores it at *dstkey*. It is mandatory to
    provide the number of input keys *N*, before passing the input keys
    and the other (optional) arguments.

    As the terms imply, the ZINTERSTORE command requires an element to
    be present in each of the given inputs to be inserted in the
    result. The ZUNIONSTORE command inserts all elements across all
    inputs.

    Using the WEIGHTS option, it is possible to add weight to each
    input sorted set. This means that the score of each element in the
    sorted set is first multiplied by this weight before being passed
    to the aggregation. When this option is not given, all weights
    default to 1.

    With the AGGREGATE option, it's possible to specify how the results
    of the union or intersection are aggregated. This option defaults
    to SUM, where the score of an element is summed across the inputs
    where it exists. When this option is set to be either MIN or MAX,
    the resulting set will contain the minimum or maximum score of an
    element across the inputs where it exists.

Return value
------------

`Integer reply <ReplyTypes.html>`_, specifically the number of
elements in the sorted set at *dstkey*.
.. |Redis Documentation| image:: redis.png