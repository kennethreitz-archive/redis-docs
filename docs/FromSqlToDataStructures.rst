`|Redis Documentation| <index.html>`_
**FromSqlToDataStructures: Contents**
  `Introduction (IDEA MORE THAN A DRAFT) <#Introduction%20(IDEA%20MORE%20THAN%20A%20DRAFT)>`_
    `Data Structures <#Data%20Structures>`_
    `Dude where is my SELECT statement? <#Dude%20where%20is%20my%20SELECT%20statement?>`_
    `LISTs <#LISTs>`_
    `SETs <#SETs>`_
    `SORT to the rescue <#SORT%20to%20the%20rescue>`_
      `SORT BY <#SORT%20BY>`_
    `HASHEs <#HASHEs>`_
FromSqlToDataStructures
=======================

Introduction (IDEA MORE THAN A DRAFT)
=====================================

**Â¿Coming from SQLand?** *Â¿Who doesn't?* Redis is simple,
*primitive* when comapred to the world you are used to in the world
of Relational Database Managers (RDBMS) and Structure Query
Language (SQL), here you will find insight to build bridges between
both worlds to model real life problems.
Data Structures
---------------

When I was young, happy and single ;) I studied **Data Structures**
at the university, actually I learnt Data Structures and Algorithms
*before* learning anything about Databases, and particularly RDBMS
and SQL. This is natural because you need to know about Data
Structures and Algorithms to understand a Database.
Redis can be seen as a **Data Structures Server**, a very simple
interface to a extremly fast and efficient
Dude where is my SELECT statement?
----------------------------------

LISTs
-----

In SQL there is no such thing as a "natural" order, a SELECT
statement without a ORDER BY clause will return data in a undefined
order. In Redis `LISTs <LISTs.html>`_ address the problem of
natural ordering, ...
SETs
----

So you have a bunch of unordered data,
SORT to the rescue
------------------

But sometimes we *need* to actually sort a LIST in a order
different from its natural or take a SET and have it ordered, there
is where the *fast* SORT commands comes handy...
SORT BY
~~~~~~~

Just SORTing keys would be kind of boring, sometimes useless right?
Well, you can SORT...
HASHEs
------

Umm, sorry you will have to wait for a
`upcoming version of Redis <RoadMap.html>`_ to have Hashes, but
here are Idioms you should house to manage Dictionary like data...
.. |Redis Documentation| image:: redis.png