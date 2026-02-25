---
title: Publications
layout: default
---

## Peer-reviewed publications

{% for pub in site.data.publications %}
  <div class="publication">
    <div class="pub-title">{{ pub.title }}</div>

    <div class="pub-authors">
      {{ pub.authors }}
    </div>

    <div class="pub-meta">
      {{ pub.journal }} ({{ pub.year }})
      {% assign c = site.data.citations[pub.id] %}
      {% if c %}
        · {{ c }} citations
      {% endif %}
    </div>
  </div>
{% endfor %}

## Manuscripts under review

<div class="publication">
	<div class="pub-title">
	  <a href="https://doi.org/10.xxxx/xxxxx">
	    Informal Connections Outweigh Co-authorship Ties in Academic Impact
	  </a>
	</div>

	<div class="pub-meta">
	  <span class="author">Lluís Danús</span>, William Dineenn, Carolina Torreblanca, Guy Grossman, Sandra González-Bailón
	  <br>
	  <em>*R&R PNAS*</em> (2026) <span class="citations" data-scholar="paper_id_1">–</span> Cited by 
	</div>
</div>

<div class="publication">
	<div class="pub-title">
	  <a href="https://doi.org/10.xxxx/xxxxx">
	    Gender and the influence of research environment in topic selection of early-career faculty in STEM
	  </a>
	</div>

	<div class="pub-meta">
	  <span class="author">Lluís Danús</span>, Robert H. Davis, Roger Guimerà, Marta Sales-Pardo
	  <br>
	  <em>R&R EPJ Data Science</em> (2026) <span class="citations" data-scholar="paper_id_1">–</span> Cited by 
	</div>
</div>
