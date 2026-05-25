---
layout: splash
permalink: /
title: "Gist Labs"
excerpt: "We Get To The Source Of People, Process, And Technology."
header:
  overlay_image: /assets/white-board-featured.jpg
  overlay_filter: 0.7
  actions:
    - label: "Book an Intro Call"
      url: "https://www.linkedin.com/company/gist-labs/services"
intro:
  - excerpt: "World-class, deep consulting into the most important aspects of your Strategy, Delivery, and Technology."
feature_row:
  - title: "Custom Agile Process"
    excerpt: "A process that works for your organization. We build from principles and collaborate with your staff to create the Agile@YourCompany that changes engagement and the bottom line."
  - title: "Tech Due Diligence & Investigations"
    excerpt: "Build/Buy/Acquire and M&A choices need clarity into the technology at stake, and often the people and processes that created it. We are experts at getting that clarity and connecting it to business opportunity and strategy."
  - title: "Technology Roadmaps"
    excerpt: "Balance the agile approach of 'build what you really need now' with 'have a vision of what you are building towards.' We help you create a true technology vision and blend that with iterative delivery."
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

<div class="client-logos">
  <h2>Our Clients</h2>
  <p>Delivering insights for leading brands</p>
  <div class="logos">
    <img src="/assets/hp-logo.png" alt="HP" />
    <img src="/assets/pizza-hut-logo.png" alt="Pizza Hut" />
    <img src="/assets/snapfish-logo.png" alt="Snapfish" />
    <img src="/assets/tw-logo.png" alt="ThoughtWorks" />
    <img src="/assets/doordash-logo.png" alt="DoorDash" />
  </div>
</div>

<div class="recent-posts">
  <h2>Recent Posts</h2>
  {% for post in site.posts limit:5 %}
    {% include archive-single.html %}
  {% endfor %}
  <p><a href="/blog/" class="btn btn--primary">View all posts</a></p>
</div>
