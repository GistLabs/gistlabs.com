---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

# Welcome to GistLabs

This is my personal website built with Jekyll and hosted on GitHub Pages.

## Pages
- [About Me]({{ '/about/' | relative_url }})
- [Blog]({{ '/blog/' | relative_url }})

## Latest Posts
<ul>
  {% for post in site.posts limit:3 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}
    </li>
  {% endfor %}
</ul>
