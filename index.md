---
title: About
layout: default
---

## About

!Bones!

I am a postdoctoral researcher in Computational Social Science at the Center for Information Networks and Democracy (CIND) in the University of Pennsylvania. My research nowadays is centered on how

---

## News

{% for post in site.posts limit:5 %}
- **{{ post.date | date: "%b %Y" }}** — {{ post.title }}
{% endfor %}
