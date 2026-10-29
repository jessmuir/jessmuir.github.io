---
layout: page
title: Research Group
use-site-title: true
hide-title: true
own-heading: true
---

<div class="page-top" markdown="1">
<div markdown="1">

{% include page-heading.html %}

My research group works at the intersection of cosmology theory and observation, using the large-scale structure of the Universe as a window into dark energy, gravity, and fundamental physics. We are based in the [University of Cincinnati Physics Department](https://www.artsci.uc.edu/departments/physics.html) and are involved in the [Dark Energy Survey](https://www.darkenergysurvey.org/) and the [Rubin Observatory LSST Dark Energy Science Collaboration](https://lsstdesc.org/).

We interact closely with other astrophysicists in the UC Physics Department, including the groups of [Colin Bischoff](https://homepages.uc.edu/~bischocn/), [Matt Bayliss](https://www.matthewbbayliss.com/), and [Helen Meskhidze](https://helenmeskhidze.com/). We hold a weekly joint group meeting with [Jahmour Givans](https://jgivans.github.io/)'s group. 

</div>
<div class="side-box" markdown="1">

#### Joining the group

**PhD students** — Admission is through the [UC Physics PhD program](https://www.artsci.uc.edu/natural-sciences/physics/academic-programs/graduate-programs.html).

**UC undergraduates** —  I'm happy to chat about research with interested students, and occasionally am able to take on undergraduate researchers into the group. Outside capstone projects, I encourage students to apply to work on summer research via the [UPRISE program](https://www.ceas.uc.edu/research/undergraduate/uprise.html). Undergraduates interested in astrophysics are encouraged to attend the department's weekly astrophysics journal club. Ask me (or other UC astro people) about it if you're interested!

</div>
</div>

{% assign current = site.data.group | where_exp: "m", "m.alum != true" %}
{% assign alumni = site.data.group | where: "alum", true %}

## Current members

<div class="group-grid">
  {% for m in current %}
  <div class="group-card">
    {% if m.photo %}
    <img class="group-photo" src="{{ m.photo | relative_url }}" alt="Photo of {{ m.name | escape }}">
    {% else %}
    {% assign parts = m.name | split: " " %}
    <div class="group-photo group-initials">{{ parts.first | slice: 0 }}{{ parts.last | slice: 0 }}</div>
    {% endif %}
    <div class="group-name">{% if m.link %}<a href="{{ m.link }}">{{ m.name }}</a>{% else %}{{ m.name }}{% endif %}</div>
    {% if m.role %}<div class="group-role">{{ m.role }}</div>{% endif %}
    {% if m.blurb %}<p class="group-blurb">{{ m.blurb }}</p>{% endif %}
  </div>
  {% endfor %}
</div>

{% if alumni.size > 0 %}
## Past mentees

<ul class="alumni-list">
  {% for m in alumni %}
  <li>
    {% if m.link %}<a href="{{ m.link }}">{{ m.name }}</a>{% else %}{{ m.name }}{% endif %}{% if m.role %} &ndash; {{ m.role }}{% endif %}
    {% if m.blurb %}<span class="alumni-now">{{ m.blurb }}</span>{% endif %}
  </li>
  {% endfor %}
</ul>
{% endif %}
