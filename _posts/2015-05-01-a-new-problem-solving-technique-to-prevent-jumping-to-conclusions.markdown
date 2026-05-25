---
layout: single
title: "A New Problem Solving Technique To Prevent Jumping to Conclusions"
date: 2015-05-01 10:00:00 -0700
categories: posts
author: John Heintz
permalink: /2015/05/a-new-problem-solving-technique-to-prevent-jumping-to-conclusions/
header:
  teaser: /assets/white-board-featured.jpg
  image: /assets/white-board-featured.jpg
---

![White board]({{ '/assets/white-board-featured.jpg' | relative_url }})

## The Three-Color Problem Solving Technique

### Hide the Blue Markers: A tool you can use to analyze and fix complex problems

You have a problem. It's a big problem and you're not exactly sure what it is, much less how to fix it. When you start discussing the problem with your team, you find that some team members are jumping to conclusions and you haven't even outlined the entire problem.

This is the simplest problem solving tool I've used to help a team completely define and analyze a problem before creating any solutions. I discovered this technique by accident, a happy accident. Here's how it came about.

### Hide the Blue Markers: How This Solution Came About

Several years ago, I was working with a team and one day, we started experiencing a production issue. The systems were behaving slowly everywhere: the process queues were backing up; the application servers were nearly idle: the databases were nearly idle; no thread locks or contention could be found. There were many different components and subsystems at play and it was not obvious what was going on. It was quite a mysterious problem.

The team organized into a meeting room to figure out what was going on, what they should do, and I was invited to join them.

### Jumping to Solutions

As we dove into the conversation to understand things, I asked the group to step back a moment and draw a systems diagram to show and teach me what was going on – because I didn't know what was present.

![Black Ink One Problem Solving Tool]({{ '/assets/black-ink-problem-solving.jpg' | relative_url }})

We used black markers to draw the systems diagram, showing the client components, the communication channels, the various server components and processes and databases and so on.

![Use Red Marker to denote problem areas]({{ '/assets/red-marker-problem-areas.jpg' | relative_url }})

As we were drawing the systems diagram, we also agreed to use red markers to show the problem areas: where things were going wrong, or where we thought there were risks of failures. As certain risks were marked in red, some individuals would get an "aha" and then jump to leave the room and go fix it.

I literally watched people leap to solutions. I was fascinated.

As the meeting progressed, the team used blue markers to denote solutions. Although I cautioned the team to "not leap to conclusions," they still did. It was amazing seeing individuals yet again try to jump up and go do something. Yet, we hadn't even finished fully describing all of the system. And we hadn't finished describing all of the possible problems, risks, or failures.

### One Color at a Time

I began actively facilitating the meeting. I gathered all of the markers in the room and set a meeting rule: "We can't move on to the next color until we're finished with the color that we're on." That meant that we had to finish using the black marker to define the current systems diagrams and the things that we knew to be true. No more red or blue markers for a while.

Once we all agreed to this new rule, we moved on. We used black until everyone agreed, with a head nod, that we had captured the current system as we knew it. Then, we picked up the red markers and annotated the diagram focusing on the problem areas, where things were going wrong and potential risks. Whenever ideas or solutions came up, we politely deferred those to when we were ready for the final phase: the solutions phase where we would get to use the blue marker.

After the red marker annotations were completed and everyone nodded their heads that we had gotten everything, we moved to the blue marker. We noted ideas, suggestions, things we could try and investigate. And that went on for a short while.

### The Full Picture

When we finished this process we had a pretty good view of the whole picture. We understood the components that were there, we understood what all of the possible things were that could be wrong and where they could go wrong, plus, we had a set of suggestions for what we could do about them. It was actually very easy to prioritize what we ought to do next. In fact, some of the suggestions made in blue were quite obvious choices.

At the end of the meeting, we had come to a good decision that worked well for us and we moved on.

Here is an actual first use of this technique (we used BLACK, RED, BLUE marker colors) that the team still talks about helping them not jump to conclusions.

![Three color problem solving]({{ '/assets/three-color-problem-solving.jpg' | relative_url }})

### Don't Jump to Conclusions

So, now you know why I call the story "Hide the Blue Markers." Drawing (literally) conclusions before you've really examined the problem is detrimental to your process. I highly recommend using the Three-Color Problem Solving tool when your team has a problem and you can't figure out the entire problem, nor the entire solution.

## How to Hold a Three-Color Problem Solving Session

1. Grab three colored markers: black, red and green.
2. Meet at the whiteboard (or use a large piece of paper).
3. Ask all team members to the join the meeting.

### Pen Colors and Their Meaning

• The black pen is used for diagramming and identifying facts.
• The red pen is used for identifying challenges or problems.
• The green pen, however, is used for documenting potential solutions. This is the pen you need to hide. (In my story, "Hide the Blue Markers," we were using blue rather than green).

#### The Rules:

1. Only one color may be used at a time.
2. You can not move on to the next color until everyone agrees that everything is covered by the first color.
3. You can return to a previous color if you discover you missed something.

#### The Process:

1. Draw in BLACK the things you know for sure. (Systems diagram, current measurements, list of assumptions, …) Keep adding to this until everyone agrees it's accurate and reasonably complete. Keep asking, "What have we missed?" Get full consensus that all things are drawn in black.
2. Annotate this diagram with RED for challenges, concerns, or big questions. Keep adding RED until everyone agrees everything is captured. You MAY add more BLACK notes if missing information comes up. NO GREEN may be used at all!
3. Start annotating GREEN to mark ideas, solutions, and next steps. Do this until everyone agrees everything is captured.

When your diagram is done, you should have a full picture of facts, concerns and possible solutions. From here, you can use a method to sort which solutions should be addressed first. (I've used dot voting to great effect).

The Three-Color Problem Solving Tool is an effective technique for helping your team examine a large, complex problem. By hiding the green marker, the one meant for solutions, you will prevent your team members from jumping to conclusions, while helping them completely define and understand the problem before creating solutions.

Please let me know if this technique works for you, or if you'd like some help facilitating it's use in your organization.
