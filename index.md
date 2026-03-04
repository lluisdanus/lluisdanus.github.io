---
layout: default
title: Lluís Danús
---

<!-- About Container -->
<div class="about-container">

  <!-- Profile Photo -->
  <div class="about-photo">
    <img src="{{ '/assets/profile_picture.png' | relative_url }}" alt="Lluís Danús">
    <!-- Social Links -->
    <div class="social-links">
      <a href="https://github.com/lluisdanus" target="_blank" title="GitHub">
        <img src="{{ '/assets/icons/github.svg' | relative_url }}" alt="GitHub" class="social-icon">
      </a>
      <a href="https://www.linkedin.com/in/lluisdanus/" target="_blank" title="LinkedIn">
        <img src="{{ '/assets/icons/linkedin.svg' | relative_url }}" alt="LinkedIn" class="social-icon">
      </a>
      <a href="https://blueskyweb.xyz/lluisdanus.bsky.social" target="_blank" title="BlueSky">
        <img src="{{ '/assets/icons/bluesky.svg' | relative_url }}" alt="BlueSky" class="social-icon">
      </a>
      <a href="https://scholar.google.com/citations?user=DYeubX0AAAAJ&hl=ca" target="_blank" title="Google Scholar">
        <img src="{{ '/assets/icons/scholar.svg' | relative_url }}" alt="Google Scholar" class="social-icon">
      </a>
    </div>
  </div>

  <!-- Bio and Social Links -->
  <div class="about-bio">
    <h1>Lluís Danús</h1>
    <p>
      !Bones! I am a computational social scientist who combines statistical physics methods, social network analysis, and large language models (LLMs) to study how humans interact, organize, and circulate. My research spans three interconnected areas: the science of science, where I investigate formal and informal collaboration patterns shape how researchers engage with each other and the effects of its effects on the scientific production; online political organization, exploring how social media shapes collective behavior, information diffusion and how LLMs ; and human mobility, modeling how people move across cities and regions and how these flows influence social and economic dynamics. 
    </p>
    
    <p>
    	I am currently a postdoctoral researcher at University of Pennsylvania's <a href='https://www.asc.upenn.edu/research/centers/center-for-information-networks-and-democracy'> Center for Information Networks and Democracy (CIND) </a> working with Dr. Sandra Gonzalez-Bailon. I received my Ph.D. in Complex Systems at the Rovira i Virgili University where I worked at the <a href='https://seeslab.info/' title="SEESLab">Systems and Emerging Systems Laboratory</a>. Previously I earned my BSc in Physics at the <a href='https://www.ub.edu/portal/web/fisica' title="University of Barcelona">University of Barcelona</a>
    </p>

  </div>
</div>

<!-- Mini Dashboard: News Teaser -->
<div class="dashboard-section">
  <h2>News</h2>
  {% for item in site.data.news limit:3 %}
    <div class="news-teaser">
      <a href="{{ '/news#' | append: item.id }}">{{ item.title }}</a>
      <p>{{ item.short_content }}</p>
    </div>
  {% endfor %}
  <a href="{{ '/news' | relative_url }}" class="see-all">See all news →</a>
</div>
