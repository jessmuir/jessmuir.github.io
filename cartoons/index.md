---
layout: page
title: "Cartoons"
permalink: /cartoons/
---

See below for cartoons or other science-related artwork that I've made for talks or other outreach projects. You're welcome to use any of these images for non-commercial purposes, but please credit me if you do.

<div class="cartoon-gallery">
  {% assign cartoon_posts = site.categories.cartoons | sort: "date" | reverse %}
  {% for post in cartoon_posts %}
    {% if post.image %}
      <div class="cartoon-item">
        <a href="{{ post.url | relative_url }}">
          <img src="{{ post.image | relative_url }}" alt="{{ post.title }}">
        </a>
        <p class="cartoon-caption">
          {{ post.title }}<br>
          <span class="cartoon-date">
            {{ post.date | date: "%B %-d, %Y" }}
          </span>
        </p>
      </div>
    {% endif %}
  {% endfor %}
</div>

<style>
.cartoon-gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.cartoon-item {
  flex: 1 1 240px;
  max-width: 320px;
}

.cartoon-item img {
  width: 100%;
  height: auto;
  border-radius: 4px;
  border: 1px solid #ddd;
  object-fit: cover;
}

.cartoon-caption {
  margin-top: 0.5rem;
  font-size: 0.9rem;
}

.cartoon-date {
  color: #777;
  font-size: 0.8rem;
}
</style>