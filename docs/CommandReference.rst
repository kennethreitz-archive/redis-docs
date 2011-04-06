`|Redis Documentation| <index.html>`_
**CommandReference: Contents**
    `Categorized Command List <#Categorized%20Command%20List>`_
    `Connection handling <#Connection%20handling>`_
    `Commands operating on all value types <#Commands%20operating%20on%20all%20value%20types>`_
    `Commands operating on string values <#Commands%20operating%20on%20string%20values>`_
    `Commands operating on lists <#Commands%20operating%20on%20lists>`_
    `Commands operating on sets <#Commands%20operating%20on%20sets>`_
    `Commands operating on sorted zsets (sorted sets) <#Commands%20operating%20on%20sorted%20zsets%20(sorted%20sets)>`_
    `Commands operating on hashes <#Commands%20operating%20on%20hashes>`_
    `Sorting <#Sorting>`_
    `Transactions <#Transactions>`_
    `Publish/Subscribe <#Publish/Subscribe>`_
    `Persistence control commands <#Persistence%20control%20commands>`_
    `Remote server control commands <#Remote%20server%20control%20commands>`_
CommandReference
================

ï»¿= Redis Command Reference =
Every command name links to a specific wiki page describing the
behavior of the command.
Categorized Command List
------------------------

Connection handling
-------------------

**Command**
**Parameters**
**Description**
`QUIT <QuitCommand.html>`_
-
close the connection
`AUTH <AuthCommand.html>`_
*password*
simple password authentication if enabled
Commands operating on all value types
-------------------------------------

**Command**
**Parameters**
**Description**
`EXISTS <ExistsCommand.html>`_
*key*
test if a key exists
`DEL <DelCommand.html>`_
*key*
delete a key
`TYPE <TypeCommand.html>`_
*key*
return the type of the value stored at key
`KEYS <KeysCommand.html>`_
*pattern*
return all the keys matching a given pattern
`RANDOMKEY <RandomkeyCommand.html>`_
-
return a random key from the key space
`RENAME <RenameCommand.html>`_
*oldname* *newname*
rename the old key in the new one, destroying the newname key if it
already exists
`RENAMENX <RenamenxCommand.html>`_
*oldname* *newname*
rename the *oldname* key to *newname*, if the *newname* key does
not already exist
`DBSIZE <DbsizeCommand.html>`_
-
return the number of keys in the current db
`EXPIRE <ExpireCommand.html>`_
-
set a time to live in seconds on a key
`PERSIST <ExpireCommand.html>`_
-
remove the expire from a key
`TTL <TtlCommand.html>`_
-
get the time to live in seconds of a key
`SELECT <SelectCommand.html>`_
*index*
Select the DB with the specified index
`MOVE <MoveCommand.html>`_
*key* *dbindex*
Move the key from the currently selected DB to the *dbindex* DB
`FLUSHDB <FlushdbCommand.html>`_
-
Remove all the keys from the currently selected DB
`FLUSHALL <FlushallCommand.html>`_
-
Remove all the keys from all the databases
Commands operating on string values
-----------------------------------

**Command**
**Parameters**
**Description**
`SET <SetCommand.html>`_
*key* *value*
Set a *key* to a string *value*
`GET <GetCommand.html>`_
*key*
Return the string value of the *key*
`GETSET <GetsetCommand.html>`_
*key* *value*
Set a key to a string returning the old value of the key
`SETNX <SetnxCommand.html>`_
*key* *value*
Set a key to a string value if the key does not exist
`SETEX <SetexCommand.html>`_
*key* *time* *value*
Set+Expire combo command
`SETBIT <SetbitCommand.html>`_
*key* *offset* *value*
Set bit at *offset* to *value*
`GETBIT <GetbitCommand.html>`_
*key* *offset*
Return bit value at *offset*
`MSET <MsetCommand.html>`_
*key1* *value1* *key2* *value2* ... *keyN* *valueN*
Set multiple keys to multiple values in a single atomic operation
`MSETNX <MsetCommand.html>`_
*key1* *value1* *key2* *value2* ... *keyN* *valueN*
Set multiple keys to multiple values in a single atomic operation
if none of the keys already exist
`MGET <MgetCommand.html>`_
*key1* *key2* ... *keyN*
Multi-get, return the strings values of the keys
`INCR <IncrCommand.html>`_
*key*
Increment the integer value of key
`INCRBY <IncrCommand.html>`_
*key* *integer*
Increment the integer value of *key* by *integer*
`DECR <IncrCommand.html>`_
*key*
Decrement the integer value of key
`DECRBY <IncrCommand.html>`_
*key* *integer*
Decrement the integer value of *key* by *integer*
`APPEND <AppendCommand.html>`_
*key* *value*
Append the specified string to the string stored at key
`SUBSTR <SubstrCommand.html>`_
*key* *start* *end*
Return a substring of a larger string
Commands operating on lists
---------------------------

**Command**
**Parameters**
**Description**
`RPUSH <RpushCommand.html>`_
*key* *value*
Append an element to the tail of the List value at key
`LPUSH <RpushCommand.html>`_
*key* *value*
Append an element to the head of the List value at key
`LLEN <LlenCommand.html>`_
*key*
Return the length of the List value at key
`LRANGE <LrangeCommand.html>`_
*key* *start* *end*
Return a range of elements from the List at key
`LTRIM <LtrimCommand.html>`_
*key* *start* *end*
Trim the list at key to the specified range of elements
`LINDEX <LindexCommand.html>`_
*key* *index*
Return the element at index position from the List at key
`LSET <LsetCommand.html>`_
*key* *index* *value*
Set a new value as the element at index position of the List at key
`LREM <LremCommand.html>`_
*key* *count* *value*
Remove the first-N, last-N, or all the elements matching value from
the List at key
`LPOP <LpopCommand.html>`_
*key*
Return and remove (atomically) the first element of the List at key
`RPOP <LpopCommand.html>`_
*key*
Return and remove (atomically) the last element of the List at key
`BLPOP <BlpopCommand.html>`_
*key1* *key2* ... *keyN* *timeout*
Blocking LPOP
`BRPOP <BlpopCommand.html>`_
*key1* *key2* ... *keyN* *timeout*
Blocking RPOP
`RPOPLPUSH <RpoplpushCommand.html>`_
*srckey* *dstkey*
Return and remove (atomically) the last element of the source List
stored at *srckey* and push the same element to the destination
List stored at *dstkey*
`BRPOPLPUSH <BrpoplpushCommand.html>`_
*srckey* *dstkey*
Like RPOPLPUSH but blocking of source key is empty
Commands operating on sets
--------------------------

**Command**
**Parameters**
**Description**
`SADD <SaddCommand.html>`_
*key* *member*
Add the specified member to the Set value at key
`SREM <SremCommand.html>`_
*key* *member*
Remove the specified member from the Set value at key
`SPOP <SpopCommand.html>`_
*key*
Remove and return (pop) a random element from the Set value at key
`SMOVE <SmoveCommand.html>`_
*srckey* *dstkey* *member*
Move the specified member from one Set to another atomically
`SCARD <ScardCommand.html>`_
*key*
Return the number of elements (the cardinality) of the Set at key
`SISMEMBER <SismemberCommand.html>`_
*key* *member*
Test if the specified value is a member of the Set at key
`SINTER <SinterCommand.html>`_
*key1* *key2* ... *keyN*
Return the intersection between the Sets stored at key1, key2, ...,
keyN
`SINTERSTORE <SinterstoreCommand.html>`_
*dstkey* *key1* *key2* ... *keyN*
Compute the intersection between the Sets stored at key1, key2,
..., keyN, and store the resulting Set at dstkey
`SUNION <SunionCommand.html>`_
*key1* *key2* ... *keyN*
Return the union between the Sets stored at key1, key2, ..., keyN
`SUNIONSTORE <SunionstoreCommand.html>`_
*dstkey* *key1* *key2* ... *keyN*
Compute the union between the Sets stored at key1, key2, ..., keyN,
and store the resulting Set at dstkey
`SDIFF <SdiffCommand.html>`_
*key1* *key2* ... *keyN*
Return the difference between the Set stored at key1 and all the
Sets key2, ..., keyN
`SDIFFSTORE <SdiffstoreCommand.html>`_
*dstkey* *key1* *key2* ... *keyN*
Compute the difference between the Set key1 and all the Sets key2,
..., keyN, and store the resulting Set at dstkey
`SMEMBERS <SmembersCommand.html>`_
*key*
Return all the members of the Set value at key
`SRANDMEMBER <SrandmemberCommand.html>`_
*key*
Return a random member of the Set value at key
Commands operating on sorted zsets (sorted sets)
------------------------------------------------

**Command**
**Parameters**
**Description**
`ZADD <ZaddCommand.html>`_
*key* *score* *member*
Add the specified member to the Sorted Set value at key or update
the score if it already exist
`ZREM <ZremCommand.html>`_
*key* *member*
Remove the specified member from the Sorted Set value at key
`ZINCRBY <ZincrbyCommand.html>`_
*key* *increment* *member*
If the member already exists increment its score by *increment*,
otherwise add the member setting *increment* as score
`ZRANK <ZrankCommand.html>`_
*key* *member*
Return the rank (or index) or *member* in the sorted set at *key*,
with scores being ordered from low to high
`ZREVRANK <ZrankCommand.html>`_
*key* *member*
Return the rank (or index) or *member* in the sorted set at *key*,
with scores being ordered from high to low
`ZRANGE <ZrangeCommand.html>`_
*key* *start* *end*
Return a range of elements from the sorted set at key
`ZREVRANGE <ZrangeCommand.html>`_
*key* *start* *end*
Return a range of elements from the sorted set at key, exactly like
ZRANGE, but the sorted set is ordered in traversed in reverse
order, from the greatest to the smallest score
`ZRANGEBYSCORE <ZrangebyscoreCommand.html>`_
*key* *min* *max*
Return all the elements with score >= min and score <= max (a range
query) from the sorted set
`ZCOUNT <ZrangebyscoreCommand.html>`_
*key* *min* *max*
Return the number of elements with score >= min and score <= max in
the sorted set
`ZCARD <ZcardCommand.html>`_
*key*
Return the cardinality (number of elements) of the sorted set at
key
`ZSCORE <ZscoreCommand.html>`_
*key* *element*
Return the score associated with the specified element of the
sorted set at key
`ZREMRANGEBYRANK <ZremrangebyrankCommand.html>`_
*key* *min* *max*
Remove all the elements with rank >= min and rank <= max from the
sorted set
`ZREMRANGEBYSCORE <ZremrangebyscoreCommand.html>`_
*key* *min* *max*
Remove all the elements with score >= min and score <= max from the
sorted set
`ZUNIONSTORE / ZINTERSTORE <ZunionstoreCommand.html>`_
*dstkey* *N* *key1* ... *keyN* WEIGHTS *w1* ... *wN* AGGREGATE
SUM\|MIN\|MAX
Perform a union or intersection over a number of sorted sets with
optional weight and aggregate
Commands operating on hashes
----------------------------

**Command**
**Parameters**
**Description**
`HSET <HsetCommand.html>`_
*key* *field* *value*
Set the hash field to the specified value. Creates the hash if
needed.
`HGET <HgetCommand.html>`_
*key* *field*
Retrieve the value of the specified hash field.
`HMGET <HmgetCommand.html>`_
*key* *field1* ... *fieldN*
Get the hash values associated to the specified fields.
`HMSET <HmsetCommand.html>`_
*key* *field1* *value1* ... *fieldN* *valueN*
Set the hash fields to their respective values.
`HINCRBY <HincrbyCommand.html>`_
*key* *field* *integer*
Increment the integer value of the hash at *key* on *field* with
*integer*.
`HEXISTS <HexistsCommand.html>`_
*key* *field*
Test for existence of a specified field in a hash
`HDEL <HdelCommand.html>`_
*key* *field*
Remove the specified field from a hash
`HLEN <HlenCommand.html>`_
*key*
Return the number of items in a hash.
`HKEYS <HgetallCommand.html>`_
*key*
Return all the fields in a hash.
`HVALS <HgetallCommand.html>`_
*key*
Return all the values in a hash.
`HGETALL <HgetallCommand.html>`_
*key*
Return all the fields and associated values in a hash.
Sorting
-------

**Command**
**Parameters**
**Description**
`SORT <SortCommand.html>`_
*key* BY *pattern* LIMIT *start* *end* GET *pattern* ASC\|DESC
ALPHA
Sort a Set or a List accordingly to the specified parameters
Transactions
------------

**Command**
**Parameters**
**Description**
`MULTI/EXEC/DISCARD/WATCH/UNWATCH <MultiExecCommand.html>`_
-
Redis atomic transactions
Publish/Subscribe
-----------------

**Command**
**Parameters**
**Description**
`SUBSCRIBE/UNSUBSCRIBE/PUBLISH <PublishSubscribe.html>`_
-
Redis Public/Subscribe messaging paradigm implementation
Persistence control commands
----------------------------

**Command**
**Parameters**
**Description**
`SAVE <SaveCommand.html>`_
-
Synchronously save the DB on disk
`BGSAVE <BgsaveCommand.html>`_
-
Asynchronously save the DB on disk
`LASTSAVE <LastsaveCommand.html>`_
-
Return the UNIX time stamp of the last successfully saving of the
dataset on disk
`SHUTDOWN <ShutdownCommand.html>`_
-
Synchronously save the DB on disk, then shutdown the server
`BGREWRITEAOF <BgrewriteaofCommand.html>`_
-
Rewrite the append only file in background when it gets too big
Remote server control commands
------------------------------

**Command**
**Parameters**
**Description**
`INFO <InfoCommand.html>`_
-
Provide information and statistics about the server
`MONITOR <MonitorCommand.html>`_
-
Dump all the received requests in real time
`SLAVEOF <SlaveofCommand.html>`_
-
Change the replication settings
`CONFIG <ConfigCommand.html>`_
-
Configure a Redis server at runtime
.. |Redis Documentation| image:: redis.png