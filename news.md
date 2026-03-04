---
layout: default
title: News
permalink: /news/
---

# News

{% for item in site.data.news %}
<article class="news-item">

  <h2 class="news-title">{{ item.title }}</h2>

  <div class="news-date">{{ item.date }}</div>

  <div class="news-full">
    {{ item.full_content | markdownify }}
  </div>

</article>
{% endfor %}
