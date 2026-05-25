---
layout: single
title: "Abstract != Vague"
date: 2011-12-01 10:00:00 -0700
categories: posts
author: John Heintz
permalink: /2011/12/abstract-vague/
header:
  teaser: /assets/white-board-featured.jpg
  image: /assets/white-board-featured.jpg
---

(I've re-published this here. Originally published on my [old personal blog](http://johnheintz.blogspot.com/2010/01/abstract-vague.html)).

I've got a bone to pick, so I'll do it here. This is a problem of mine that I have with both developers(architects) and with analysts(customers).

Context: This rant applies to models/designs/architectures of a problem or solution domain. It doesn't apply to the actual coding of a solution (much).

First, some definitions:

• [Abstract](http://dictionary.reference.com/browse/abstract): something that concentrates in itself the essential qualities of anything more extensive or more general, or of several things; essence.
• [Concrete](http://dictionary.reference.com/browse/concrete): pertaining to or concerned with realities or actual instances rather than abstractions
• [Precise](http://dictionary.reference.com/browse/precise): definite or exact in statement
• [Vague](http://dictionary.reference.com/browse/vague): not clearly or explicitly stated or expressed

What does this mean?

Analysts tend towards Abstract-Vague. "Let's not get bogged down with details right now."

Developers tend towards Concrete-Precise. "I need all of the table properties fields."

Fortunately, almost no one tends to Vague-Concrete. Phew.

Un-fortunately, few move towards the most valuable region: Abstract-Precision. That's the most valuable because it offers the least noise (Concrete details) and the most information (Precision).

Here's an example. Squares are types, circles are interactions.

Notice that "Money" isn't concretely defined here. It could be a BigDecimal, double, or Smalltalk Number. Also, that Post Condition is much more precise than a lot requirements documents usually specify.

Ah, I feel better.

Here's my rule of thumb for achieving more precision:

> Add elements to your model only in order to exactly say what your audience thinks is really important.

In the example above the balance, amount, and cash properties are only present because a Withdraw requires them to precisely describe what needs to be done.
