---
title: About
layout: default
---

<div class="profile">
  <img src="/assets/profile_picture.png" alt="Profile photo">
  <div>

!Bones!

I am a postdoctoral researcher in Computational Social Science at the Center for Information Networks and Democracy (CIND) in the University of Pennsylvania. My research nowadays is centered on how

  </div>
</div>

---

## News

{% for post in site.posts limit:5 %}
- **{{ post.date | date: "%b %Y" }}** — {{ post.title }}
{% endfor %}
