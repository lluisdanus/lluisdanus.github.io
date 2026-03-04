---
layout: default
title: Lluís Danús
---

<div class="about-container">

  <!-- Profile Photo -->
  <div class="about-photo">
    <img src="{{ '/assets/images/profile.jpg' | relative_url }}" alt="Lluís Danús">
    
    <!-- Social Links below photo -->
    <div class="social-links">
      <a href="https://github.com/yourusername" target="_blank" title="GitHub">
        <img src="{{ '/assets/icons/github.svg' | relative_url }}" alt="GitHub" class="social-icon">
      </a>
      <a href="https://www.linkedin.com/in/yourusername/" target="_blank" title="LinkedIn">
        <img src="{{ '/assets/icons/linkedin.svg' | relative_url }}" alt="LinkedIn" class="social-icon">
      </a>
      <a href="https://blueskyweb.xyz/yourusername" target="_blank" title="BlueSky">
        <img src="{{ '/assets/icons/bluesky.svg' | relative_url }}" alt="BlueSky" class="social-icon">
      </a>
      <a href="https://scholar.google.com/citations?user=YOURSCHOLARID" target="_blank" title="Google Scholar">
        <img src="{{ '/assets/icons/scholar.svg' | relative_url }}" alt="Google Scholar" class="social-icon">
      </a>
    </div>
  </div>

  <!-- Bio -->
  <div class="about-bio">
    <h1>Lluís Danús</h1>
    <p>
      Postdoctoral researcher focused on social networks, human mobility, and data science.
    </p>
  </div>
</div>

<!-- News Dashboard -->
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
