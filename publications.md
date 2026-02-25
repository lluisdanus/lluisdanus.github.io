---
title: Publications
layout: default
---

{% for pub in site.data.publications %}
<div class="publication">

<div class="pub-title">
  <a href="https://doi.org/{{ pub.doi }}">{{ pub.title }}</a>
</div>

<div class="pub-meta">
  {{ pub.authors | replace: "Your Name", "<span class='author'>Your Name</span>" }}  
  <br>
  <em>{{ pub.journal }}</em> ({{ pub.year }}) ·
  {{ site.data.citations[pub.id] }} citations
</div>

</div>
{% endfor %}
