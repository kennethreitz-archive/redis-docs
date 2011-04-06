`|Redis Documentation| <index.html>`_
**PublishSubscribe: Contents**
  `UNSUBSCRIBE channel\_1 channel\_2 ... channel\_N <#UNSUBSCRIBE%20channel_1%20channel_2%20...%20channel_N>`_
  `UNSUBSCRIBE (unsubscribe from all channels) <#UNSUBSCRIBE%20(unsubscribe%20from%20all%20channels)>`_
  `PSUBSCRIBE pattern\_1 pattern\_2 ... pattern\_N <#PSUBSCRIBE%20pattern_1%20pattern_2%20...%20pattern_N>`_
  `PUNSUBSCRIBE pattern\_1 pattern\_2 ... pattern\_N <#PUNSUBSCRIBE%20pattern_1%20pattern_2%20...%20pattern_N>`_
  `PUNSUBSCRIBE (unsubscribe from all patterns) <#PUNSUBSCRIBE%20(unsubscribe%20from%20all%20patterns)>`_
  `PUBLISH channel message <#PUBLISH%20channel%20message>`_
    `Format of pushed messages <#Format%20of%20pushed%20messages>`_
    `Unsubscribing from all the channels at once <#Unsubscribing%20from%20all%20the%20channels%20at%20once>`_
    `Wire protocol example <#Wire%20protocol%20example>`_
    `PSUBSCRIBE and PUNSUBSCRIBE: pattern matching subscriptions <#PSUBSCRIBE%20and%20PUNSUBSCRIBE:%20pattern%20matching%20subscriptions>`_
    `Messages matching both a pattern and a channel subscription <#Messages%20matching%20both%20a%20pattern%20and%20a%20channel%20subscription>`_
    `The meaning of the count of subscriptions with pattern matching <#The%20meaning%20of%20the%20count%20of%20subscriptions%20with%20pattern%20matching>`_
    `More details on the PUBLISH command <#More%20details%20on%20the%20PUBLISH%20command>`_
    `Programming Example <#Programming%20Example>`_
    `Client library implementations hints <#Client%20library%20implementations%20hints>`_
PublishSubscribe
================

ï»¿=SUBSCRIBE channel\_1 channel\_2 ... channel\_N=
UNSUBSCRIBE channel\_1 channel\_2 ... channel\_N
================================================

UNSUBSCRIBE (unsubscribe from all channels)
===========================================

PSUBSCRIBE pattern\_1 pattern\_2 ... pattern\_N
===============================================

PUNSUBSCRIBE pattern\_1 pattern\_2 ... pattern\_N
=================================================

PUNSUBSCRIBE (unsubscribe from all patterns)
============================================

PUBLISH channel message
=======================

Time complexity: subscribe is O(1), unsubscribe is O(N) where N is
the number of clients already subscribed to a channel, publish is
O(N+M) where N is the number of clients subscribed to the receiving
channel, and M is the total number of subscribed patterns (by any
client). Psubscribe is O(N) where N is the number of patterns the
Psubscribing client is already subscribed to. Punsubscribe is
O(N+M) where N is the number of patterns the Punsubscribing client
is already subscribed and M is the number of total patterns
subscribed in the system (by any client).
**Note**: this commands are available starting form Redis 2.0.0
    SUBSCRIBE, UNSUBSCRIBE and PUBLISH commands implement
    the`Publish/Subscribe messaging paradigm <http://en.wikipedia.org/wiki/Publish/subscribe>`_
    where (citing Wikipedia) senders (publishers) are not programmed to
    send their messages to specific receivers (subscribers). Rather,
    published messages are characterized into channels, without
    knowledge of what (if any) subscribers there may be. Subscribers
    express interest in one or more channels, and only receive messages
    that are of interest, without knowledge of what (if any) publishers
    there are. This decoupling of publishers and subscribers can allow
    for greater scalability and a more dynamic network topology.

    For instance in order to subscribe to the channels foo and bar the
    clientwill issue the SUBSCRIBE command followed by the names of the
    channels.

::

    SUBSCRIBE foo bar

    All the messages sent by other clients to this channels will be
    pushed bythe Redis server to all the subscribed clients, in the
    form of a threeelements bulk reply, where the first element is the
    message type, thesecond the originating channel, and the third
    argument the message payload.

    A client subscribed to 1 or more channels should NOT issue other
    commandsother than SUBSCRIBE and UNSUBSCRIBE, but can subscribe or
    unsubscribeto other channels dynamically.

    The reply of the SUBSCRIBE and UNSUBSCRIBE operations are sent in
    the formof messages, so that the client can just read a coherent
    stream of messageswhere the first element indicates the kind of
    message.

Format of pushed messages
-------------------------

    Messages are in the form of multi bulk replies with three
    elements.The first element is the kind of message:


-  "subscribe": means that we successfully subscribed to the
   channel given as second element of the multi bulk reply. The third
   argument represents the number of channels we are currently
   subscribed to.
-  "unsubscribe": means that we successfully unsubscribed from the
   channel given as second element of the multi bulk reply. The third
   argument represents the number of channels we are currently
   subscribed to. If this latest argument is zero, we are no longer
   subscribed to any channel, and the client can issue any kind of
   Redis command as we are outside the Pub/sub state.
-  "message": it is a message received as result of a PUBLISH
   command issued by another client. The second element is the name of
   the originating channel, and the third the actual message payload.

Unsubscribing from all the channels at once
-------------------------------------------

If the UNSUBSCRIBE command is issued without additional arguments,
it is equivalent to unsubscribing to all the channels we are
currently subscribed. A message for every unsubscribed channel will
be received.
Wire protocol example
---------------------

::

    SUBSCRIBE first second
    *3
    $9
    subscribe
    $5
    first
    :1
    *3
    $9
    subscribe
    $6
    second
    :2

at this point from another client we issue a PUBLISH operation
against the channel named "second". This is what the first client
receives:
::

    *3
    $7
    message
    $6
    second
    $5
    Hello

Now the client unsubscribes itself from all the channels using the
UNSUBSCRIBE command without additional arguments:
::

    UNSUBSCRIBE
    *3
    $11
    unsubscribe
    $6
    second
    :1
    *3
    $11
    unsubscribe
    $5
    first
    :0

PSUBSCRIBE and PUNSUBSCRIBE: pattern matching subscriptions
-----------------------------------------------------------

Redis Pub/Sub implementation supports pattern matching. Clients may
subscribe to glob style patterns in order to receive all the
messages sent to channel names matching a given pattern.
For instance the command:
::

    PSUBSCRIBE news.*

Will receive all the messages sent to the channel
news.art.figurative and news.music.jazz and so forth. All the glob
style patterns as valid, so multiple wild cards are supported.
Messages received as a result of pattern matching are sent in a
different format:

-  The type of the message is "pmessage": it is a message received
   as result of a PUBLISH command issued by another client, matching a
   pattern matching subscription. The second element is the original
   pattern matched, the third element is the name of the originating
   channel, and the last element the actual message payload.

Similarly to SUBSCRIBE and UNSUBSCRIBE, PSUBSCRIBE and PUNSUBSCRIBE
commands are acknowledged by the system sending a message of type
"psubscribe" and "punsubscribe" using the same format as the
"subscribe" and "unsubscribe" message format.
Messages matching both a pattern and a channel subscription
-----------------------------------------------------------

A client may receive a single message multiple time if it's
subscribed to multiple patterns matching a published message, or it
is subscribed to both patterns and channels matching the message.
Like in the following example:
::

    SUBSCRIBE foo
    PSUBSCRIBE f*

In the above example, if a message is sent to the **foo** channel,
the client will receive two messages, one of type "message" and one
of type "pmessage".
The meaning of the count of subscriptions with pattern matching
---------------------------------------------------------------

In **subscribe**, **unsubscribe**, **psubscribe** and
**punsubscribe** message types, the last argument is the count of
subscriptions still active. This number is actually the total
number of channels and patterns the client is still subscribed to.
So the client will exit the Pub/Sub state only when this count will
drop to zero as a result of unsubscription from all the channels
and patterns.
More details on the PUBLISH command
-----------------------------------

The Publish command is a bulk command where the first argument is
the target class, and the second argument the data to send. It
returns an Integer Reply representing the number of clients that
received the message (that is, the number of clients that were
listening for this class).
Programming Example
-------------------

Pieter Noordhuis provided a great example using Event-machine and
Redis to create
`a multi user high performance web chat <http://chat.redis-db.com>`_,
with source code included of course!
Client library implementations hints
------------------------------------

Because all the messages received contain the original subscription
causing the message delivery (the channel in the case of "message"
type, and the original pattern in the case of "pmessage" type)
clinet libraries may bind the original subscription to callbacks
(that can be anonymous functions, blocks, function pointers, and so
forth), using an hash table.
When a message is received an O(1) lookup can be done in order to
deliver the message to the registered callback.
.. |Redis Documentation| image:: redis.png