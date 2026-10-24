---
layout: page
title: Press
use-site-title: true
hide-title: true
---

I'm happy to talk with reporters and science writers about science, and especially about cosmology, including topics like dark energy, the large-scale structure of the Universe, and what galaxy surveys like the Dark Energy Survey and Rubin Observatory's LSST can tell us about fundamental physics. For media inquiries, please contact me by [email](mailto:muirjc@ucmail.uc.edu).

Below are news coverage, interviews, and other media featuring my research.

<ul class="press-list">
  {% for item in site.data.press %}
  <li class="press-item">
    {{ item.text | markdownify | remove: "<p>" | remove: "</p>" | strip }}
    <span class="press-meta">({{ item.date | date: "%B %Y" }}{% if item.kind %} &middot; {{ item.kind }}{% endif %})</span>
  </li>
  {% endfor %}
</ul>
