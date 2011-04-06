`|Redis Documentation| <index.html>`_
**SortCommand: Contents**
    `Sorting by external keys <#Sorting%20by%20external%20keys>`_
    `Not Sorting at all <#Not%20Sorting%20at%20all>`_
    `Retrieving external keys <#Retrieving%20external%20keys>`_
    `Storing the result of a SORT operation <#Storing%20the%20result%20of%20a%20SORT%20operation>`_
    `SORT and Hashes: BY and GET by hash field <#SORT%20and%20Hashes:%20BY%20and%20GET%20by%20hash%20field>`_
    `Return value <#Return%20value>`_
SortCommand
===========

ï»¿= SORT *key* ``[``BY *pattern*``]`` ``[``LIMIT *start*
*count*``]`` ``[``GET *pattern*``]`` ``[``ASC\|DESC``]``
``[``ALPHA``]`` ``[``STORE *dstkey*``]`` =
    Sort the elements contained in the `List <Lists.html>`_,
    `Set <Sets.html>`_, or`Sorted Set <SortedSets.html>`_ value at
    *key*. By defaultsorting is numeric with elements being compared as
    double precisionfloating point numbers. This is the simplest form
    of SORT:

::

    SORT mylist

    Assuming mylist contains a list of numbers, the return value will
    bethe list of numbers ordered from the smallest to the biggest
    number.In order to get the sorting in reverse order use **DESC**:

::

    SORT mylist DESC

    The **ASC** option is also supported but it's the default so you
    don'treally need it.If you want to sort lexicographically use
    **ALPHA**. Note that Redis isutf-8 aware assuming you set the right
    value for the LC\_COLLATEenvironment variable.

    Sort is able to limit the number of returned elements using the
    **LIMIT** option:

::

    SORT mylist LIMIT 0 10

    In the above example SORT will return only 10 elements, starting
    fromthe first one (start is zero-based). Almost all the sort
    options canbe mixed together. For example the command:

::

    SORT mylist LIMIT 0 10 ALPHA DESC

    Will sort *mylist* lexicographically, in descending order,
    returning onlythe first 10 elements.

    Sometimes you want to sort elements using external keys as weights
    tocompare instead to compare the actual List Sets or Sorted Set
    elements.For example the list *mylist* may contain the elements 1,
    2, 3, 4, thatare just unique IDs of objects stored at object\_1,
    object\_2, object\_3and object\_4, while the keys weight\_1,
    weight\_2, weight\_3 and weight\_4can contain weights we want to
    use to sort our list of objectsidentifiers. We can use the
    following command:

Sorting by external keys
------------------------

::

    SORT mylist BY weight_*

    the **BY** option takes a pattern (``weight_*`` in our example)
    that is usedin order to generate the key names of the weights used
    for sorting.Weight key names are obtained substituting the first
    occurrence of ``*``with the actual value of the elements on the
    list (1,2,3,4 in our example).

    Our previous example will return just the sorted IDs. Often it
    isneeded to get the actual objects sorted (object\_1, ...,
    object\_4 in theexample). We can do it with the following command:

Not Sorting at all
------------------

::

    SORT mylist BY nosort

    also the **BY** option can take a "nosort" specifier. This is
    useful if you want to retrieve a external key (using GET, read
    below) but you don't want the sorting overhead.

Retrieving external keys
------------------------

::

    SORT mylist BY weight_* GET object_*

    Note that **GET** can be used multiple times in order to get more
    keys forevery element of the original List, Set or Sorted Set
    sorted.

    Since Redis >= 1.1 it's possible to also GET the list elements
    itselfusing the special # pattern:

::

    SORT mylist BY weight_* GET object_* GET #

Storing the result of a SORT operation
--------------------------------------

    By default SORT returns the sorted elements as its return
    value.Using the **STORE** option instead to return the elements
    SORT willstore this elements as a `Redis List <Lists.html>`_ in the
    specified key.An example:

::

    SORT mylist BY weight_* STORE resultkey

    An interesting pattern using SORT ... STORE consists in
    associatingan `EXPIRE <ExpireCommand.html>`_ timeout to the
    resulting key so that inapplications where the result of a sort
    operation can be cached forsome time other clients will use the
    cached list instead to call SORTfor every request. When the key
    will timeout an updated version ofthe cache can be created using
    SORT ... STORE again.

    Note that implementing this pattern it is important to avoid that
    multipleclients will try to rebuild the cached version of the
    cacheat the same time, so some form of locking should be
    implemented(for instance using `SETNX <SetnxCommand.html>`_).

SORT and Hashes: BY and GET by hash field
-----------------------------------------

    It's possible to use BY and GET options against Hash fields using
    the following syntax:

::

    SORT mylist BY weight_*->fieldname
    SORT mylist GET object_*->fieldname

    The two chars string -> is used in order to signal the name of the
    Hash field. The key is substituted as documented above with sort BY
    and GET against normal keys, and the Hash stored at the resulting
    key is accessed in order to retrieve the specified field.

Return value
------------

`Multi bulk reply <ReplyTypes.html>`_, specifically a list of
sorted elements.
.. |Redis Documentation| image:: redis.png