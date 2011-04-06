`|Redis Documentation| <index.html>`_
**KeysCommand: Contents**
  `KEYS \_pattern\_ <#KEYS%20_pattern_>`_
    `Return value <#Return%20value>`_
KeysCommand
===========

ï»¿#sidebar `GenericCommandsSidebar <GenericCommandsSidebar.html>`_
KEYS \_pattern\_
================

*Time complexity: O(n) (with n being the number of keys in the DB, and assuming keys and pattern of limited length)*
    Returns all the keys matching the glob-style *pattern* asspace
    separated strings. For example if you have in thedatabase the keys
    "foo" and "foobar" the command "KEYS foo``*``"will return "foo
    foobar".

    Note that while the time complexity for this operation is O(n)the
    constant times are pretty low. For example Redis runningon an entry
    level laptop can scan a 1 million keys databasein 40 milliseconds.
    **Still it's better to consider this one of**
        the slow commands that may ruin the DB performance if not usedwith
        care\*.

        In other words this command is intended only for debugging and
        \*special\* operations like creating a script to change the DB
        schema. Don't use it in your normal code. Use Redis
        `Sets <Sets.html>`_ in order to group together a subset of
        objects.

    Glob style patterns examples:
        \* h?llo will match hello hallo hhllo\* h\*llo will match hllo
        heeeello\* h``[``ae``]``llo will match hello and hallo, but not
        hillo

    Use \\ to escape special chars if you want to match them verbatim.
    Return value
    ------------

    `Multi bulk reply <ReplyTypes.html>`_

.. |Redis Documentation| image:: redis.png