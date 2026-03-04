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

## News Highlights

{% for item in site.data.news limit:5 %}
<div class="news-teaser">
  <h3>{{ item.title }}</h3>
  <p>{{ item.short_content }}</p>
  <a href="{{ '/news#' | append: item.id }}">Read more</a>
</div>
{% endfor %}
