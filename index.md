---
layout: default
title: Lluís Danús
---

<!-- About Container -->
<div class="about-container">

  <!-- Profile Photo -->
  <div class="about-photo">
    <img src="{{ '/assets/images/profile_picture.png' | relative_url }}" alt="Lluís Danús">
    <p>
    Computational Social Science |
    Network Science | Complex Systems |
    AI research
    </p>
    <!-- Social Links -->
    <div class="social-links">
      <a href="https://github.com/lluisdanus" target="_blank" title="GitHub">
        <img src="{{ '/assets/icons/github.svg' | relative_url }}" alt="GitHub" class="social-icon">
      </a>
      <a href="https://www.linkedin.com/in/lluisdanus/" target="_blank" title="LinkedIn">
        <img src="{{ '/assets/icons/linkedin.svg' | relative_url }}" alt="LinkedIn" class="social-icon">
      </a>
      <a href="https://bsky.app/profile/lluisdanus.bsky.social" target="_blank" title="BlueSky">
        <img src="{{ '/assets/icons/bluesky.svg' | relative_url }}" alt="BlueSky" class="social-icon">
      </a>
      <a href="https://scholar.google.com/citations?user=DYeubX0AAAAJ&hl=ca" target="_blank" title="Google Scholar">
        <img src="{{ '/assets/icons/scholar.svg' | relative_url }}" alt="Google Scholar" class="social-icon">
      </a>
    </div>
  </div>

  <!-- Bio and Social Links -->
  <div class="about-bio">
<p>
  !Bones! I am a computational social scientist who combines statistical physics methods, social network analysis, and large language models (LLMs) to study how humans interact, organize, and circulate. My research focuses on how these methods help us understand complex social systems: how collaborations between colleagues shape the growth of scientific domains, how online networks drive the formation and evolution of collective organization and the spread of information, and how simpler, statistically grounded approaches can sometimes better capture human behavior in urban environments.
</p>

<p>
  More recently, I have been developing LLM-assisted pipelines to identify political framing in casual, non-partisan content, and to investigate how these models may influence the way we communicate and consume information.
</p>

<p>
  I am currently a postdoctoral researcher at the University of Pennsylvania's <a href='https://www.asc.upenn.edu/research/centers/center-for-information-networks-and-democracy'>Center for Information Networks and Democracy (CIND)</a>, working with Dr. Sandra González-Bailón. I received my Ph.D. in Complex Systems at the Rovira i Virgili University, where I worked at the <a href='https://seeslab.info/' title="SEESLab">Systems and Emerging Systems Laboratory</a>. Previously, I earned my BSc in Physics at the <a href='https://www.ub.edu/portal/web/fisica' title="University of Barcelona">University of Barcelona</a>.
</p>

  </div>
</div>

<h2> News </h2>

<div class="about-news-dashboard">
  {% for item in site.data.news limit:3 %}
    <a href="{{ '/news#' | append: item.id }}" class="news-card">
      <img src="{{ item.image | relative_url }}" alt="{{ item.title }}">
      <div class="news-caption">
        <strong>{{ item.title }}</strong>
        <p>{{ item.short_content }}</p>
      </div>
    </a>
  {% endfor %}
</div>

{% assign today = 'now' | date: "%Y-%m-%d" %}

<!-- News / Events Table -->
<div class="events-dashboard">
  <table>
    <thead>
      <tr>
        <th>Date</th>
        <th>Event / News</th>
      </tr>
    </thead>
    <tbody>
      {% assign upcoming = site.data.events | sort: 'date' %}
      {% for item in upcoming %}
        {% assign item_date = item.date | date: "%Y-%m-%d" %}
        {% if item_date >= today %}
          <tr>
            <td>
              {{ item.date | date: "%b %d, %Y" }}
              {% if item.location %}
                <span class="location-icon">📍</span>
              {% endif %}
            </td>
            <td>
              <strong>
                {% if item.url %}
                  <a href="{{ item.url }}" target="_blank">{{ item.title }}</a>
                {% else %}
                  {{ item.title }}
                {% endif %}
              </strong>
              {% if item.short_content %}
                <p>{{ item.short_content }}</p>
              {% endif %}
            </td>
          </tr>
        {% endif %}
      {% endfor %}
    </tbody>
  </table>
</div>
