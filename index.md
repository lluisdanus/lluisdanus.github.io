---
title: About
layout: default
---

## About

I am a postdoctoral researcher in **[field]** at **[institution]**.
My research focuses on [one-sentence summary].

---

## News

{% for post in site.posts limit:5 %}
- **{{ post.date | date: "%b %Y" }}** — {{ post.title }}
{% endfor %}
