---
layout: single
title: "Big Data, Little Tests"
date: 2012-08-01
author: John Heintz
categories: posts
permalink: /2012/08/big-data-little-tests/
header:
  teaser: /assets/Sprint-Story-Points-Burndown.png
  image: /assets/Sprint-Story-Points-Burndown.png
---

This is the content for my Agile2012 presentation. (Download [BigDataLittleTests-Heintz](https://gistlabs.com//2012/08/big-data-little-tests/bigdatalittletests-heintz/))

Slides are attached to this post, and these are the GitHub repos:

- [https://github.com/jheintz/sample-hadoop-testing](https://github.com/jheintz/sample-hadoop-testing)
- [https://github.com/jheintz/sample-riak-testing](https://github.com/jheintz/sample-riak-testing)
- [https://github.com/jheintz/riak-download](https://github.com/jheintz/riak-download)

Here are the scripts that demonstrate everything:

Hadoop Sample:

> #/bin/sh
> git clone [https://github.com/jheintz/sample-hadoop-testing.git](https://github.com/jheintz/sample-hadoop-testing.git)

> cd sample-hadoop-testing.git
> git checkout step1 # initial MRUnit tests

> mvn test

> # eclipse: show mapper

> # eclipse: show reducer

> # eclipse: show unit test

> # eclipse: try open hadoop source...
> git checkout step2 # Use Cloudera repo for sources

> mvn test

> # eclipse show pom

> # eclipse: open hadoop source
> git checkout step3 # parameterized many tests

> # eclipse test ManyWordCountTest.java
> git checkout step4 # parameterized non-mr tests for speed

> # eclipse test ManyWordTest
> git checkout step5 # add cluster test

> # eclipse show HadoopClusterBase

> # eclipse test ClusterTest
> git checkout step6 # add parameterized cluster test

> # eclipse test MultipleClusterTest
> git checkout step7 # split unit and integration tests

> # eclipse show test names

> # eclipse show pom failsafe

> mvn test

> mvn verify

Riak Sample:

> #/bin/sh
> git clone [https://github.com/jheintz/sample-riak-testing.git](https://github.com/jheintz/sample-riak-testing.git)

> cd sample-riak-testing.git
> git checkout step1 # initial test, fails

> mvn test

> # eclipse show SmokeTest failure
> git checkout step2 # add riak downloader

> mvn test

> # I don't know why eclipse has maven failure...

> # eclipse show riak-build.xml

> # eclipse show pom.xml
> git checkout step3 # add parameterized many tests

> # eclipse show ManySmokeTest
> ant -f riak-build.xml stop

Cassandra Sample:

> #/bin/sh
> git clone [http://github.com/jsevellec/cassandra-unit.git](http://github.com/jsevellec/cassandra-unit.git)

> cd cassandra-unit
> mvn test

> mvn eclipse:eclipse