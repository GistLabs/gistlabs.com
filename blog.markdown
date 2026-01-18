---
layout: page
title: Blog
permalink: /blog/
---

This is my blog where I share thoughts and updates.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>