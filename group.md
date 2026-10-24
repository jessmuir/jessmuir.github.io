---
layout: page
title: Research Group
use-site-title: true
hide-title: true
---

Our group works at the intersection of cosmological theory and data analysis, using observations of the large-scale structure of the Universe to learn about dark energy, gravity, and other fundamental physics. We are based in the [University of Cincinnati Physics Department](https://www.artsci.uc.edu/departments/physics.html) and are involved in the [Dark Energy Survey](https://www.darkenergysurvey.org/) and the [Rubin Observatory LSST Dark Energy Science Collaboration](https://lsstdesc.org/).

We interact closely with other astrophysicists in the UC Physics Department, including the groups of [Colin Bischoff](https://homepages.uc.edu/~bischocn/), [Matt Bayliss](https://www.matthewbbayliss.com/), and [Helen Meskhidze](https://helenmeskhidze.com/), and particularly [Jahmour Givans](https://jgivans.github.io/)'s group. Our two groups hold a weekly joint group meeting, which includes PhD student Sakshi Gupta and postdoc Manon Ramel from the Givans group.

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

<ul>
  {% for m in alumni %}
  <li>{% if m.link %}<a href="{{ m.link }}">{{ m.name }}</a>{% else %}{{ m.name }}{% endif %}{% if m.role %} &ndash; {{ m.role }}{% endif %}</li>
  {% endfor %}
</ul>
{% endif %}

## Prospective students

**Prospective PhD students:** Admission to the group is through the University of Cincinnati Physics PhD program. Information about the program, admissions requirements, and how to apply can be found on the [UC Physics graduate programs page](https://www.artsci.uc.edu/natural-sciences/physics/academic-programs/graduate-programs.html). Please note that I do not admit students directly, and that I am not able to respond individually to every inquiry about graduate admissions.

**University of Cincinnati undergraduates:** I periodically take on undergraduate researchers, either for summer research or for senior capstone projects. If you are interested in either option, please contact me by email to discuss possible projects. Students seeking summer research positions will be expected to apply through UC's [UPRISE program](https://www.ceas.uc.edu/research/undergraduate/uprise.html) (Undergraduates Pursuing Research in Science and Engineering). *[Note: I am not currently taking on new undergraduate researchers, but you are welcome to contact me to express interest in case that changes in the future.]*
