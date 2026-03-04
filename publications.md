---
title: Publications
layout: default
---

## Peer-reviewed publications

{% for pub in site.data.publications %}
<div class="publication">

<div class="pub-title">
  <a href="https://doi.org/{{ pub.doi }}">
  {{ pub.title }}<span class="pub-link-arrow">↗</span>
  </a>
</div>

<div class="pub-meta">
  {{ pub.authors | replace: "Danús, Lluís", "<span class='author'>Danús, Lluís</span>" }}  
  <br>
  <em>{{ pub.journal }}</em> ({{ pub.year }})
  <span class="citations">
  – Cited by: {{ site.data.citations[pub.id] | default: 0 }}
</span>
</div>

{% if pub.abstract %}
  <details class="abstract-block">
    <summary>Abstract</summary>
    <div class="abstract-text">
      {{ pub.abstract }}
    </div>
  </details>
{% endif %}

<div class="abstract-block">
  <details>
    <summary>Show citation</summary>
    <pre class="bibtex-text">
@article{ {{ pub.id }},
  author={{ "{{ pub.authors }}" }},
  title={{ "{{ pub.title }}" }},
  journal={{ "{{ pub.journal }}" }},
  year={{ "{{ pub.year }}" }},
  doi={{ "{{ pub.doi }}" }}
}
    </pre>
    <a href="/path/to/{{ pub.id }}.bib" download>Download BibTeX</a>
  </details>
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
	  <em>*R&R PNAS*</em> (2026) <span class="citations" data-scholar="paper_id_1">–</span>
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
	  <em>R&R EPJ Data Science</em> (2026) <span class="citations" data-scholar="paper_id_1">–</span> 
	</div>
</div>
