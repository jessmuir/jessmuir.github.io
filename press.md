---
layout: page
title: Press
use-site-title: true
---

News coverage, interviews, and other media featuring my research.

<ul class="press-list">
  {% for item in site.data.press %}
  <li class="press-item">
    <span class="press-date">{{ item.date | date: "%B %Y" }}</span>{% if item.kind %} <span class="press-kind">{{ item.kind }}</span>{% endif %}
    <div class="press-text">{{ item.text | markdownify }}</div>
  </li>
  {% endfor %}
</ul>
