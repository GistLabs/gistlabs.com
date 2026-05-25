---
layout: single
title: "The Outbox: An EIP Pattern"
date: 2014-05-23 10:00:00 -0700
categories: patterns
author: John Heintz
permalink: /2014/05/the-outbox/
header:
  teaser: /assets/outbox-featured.jpg
  image: /assets/outbox-featured.jpg
---

![Outbox]({{ '/assets/outbox-featured.jpg' | relative_url }})

## The Outbox

The outbox pattern, I believe, is missing from the [Enterprise Integration Patterns](http://amazon.com/o/asin/0321200683/ref=nosim/enterpriseint-20) book. This pattern is exactly like the local outbox that email clients have for disconnected operation.

How can producers reliably send messages when the broker/consumer is unavailable?

The producer of messages can durably store those messages in a local outbox before sending to a [Message Endpoint](http://www.eaipatterns.com/MessageEndpoint.html). The durable local storage may be implemented in the [Message Channel](http://www.eaipatterns.com/MessageChannel.html) directly, especially when combined with Idempotent Messages.

This pattern is implied in the book inside the [Guaranteed Messaging](http://www.eaipatterns.com/GuaranteedMessaging.html) pattern. See the "Computer 1 Disk" inside the image.

This pattern avoids the following [The Lost Send]:

1. Producer sends a message.
2. The Message Channel is temporarily unavailable.
3. Messages will queue locally and periodically retry sending.

This pattern can be used to minimize [The Premature Send]:

1. Producer sends a message within the context of some local processing scope or transactional boundary.
2. After sending the message, but still within the same processing scope, the producer aborts and rolls back local changes.
3. The message may already have been sent and processed.
4. Either:
   1. The Producer can send another compensation message to undo actions,
   2. or the producer can first store messages in the Outbox and then at the end of the scope push or purge local messages.
