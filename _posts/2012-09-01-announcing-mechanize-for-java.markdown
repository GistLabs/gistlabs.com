---
layout: single
title: "Announcing mechanize for java"
date: 2012-09-01
author: John Heintz
categories: posts
permalink: /2012/09/announcing-mechanize-for-java/
header:
  teaser: /assets/white-board-featured.jpg
  image: /assets/white-board-featured.jpg
---

On a recent project for a one of our startup clients, we at Gist Labs looked for a RESTful client library to support making the server even more hypermedia friendly. (This means we can move URLs around &#8211; even to other servers &#8211; without breaking the clients coded against the site.)

Their exists a wonderful library to do this (mechanize) implemented in [Perl](http://search.cpan.org/dist/WWW-Mechanize/), [Python](http://pypi.python.org/pypi/mechanize/), and [Ruby](http://mechanize.rubyforge.org/). But we were writing a Java/Android client, so we did something about it.

Today we are happy to announce the availability of a Java port of this great tool. If you are building a REST client or screen scraping web pages in Java, please check it out!

Here is the project page: <a title="Mechanize for Java" href="https://gistlabs.com//software/mechanize-for-java/">mechanize for java</a>