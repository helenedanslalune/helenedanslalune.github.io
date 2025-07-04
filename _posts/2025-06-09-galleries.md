---
layout: post
title: Hélène's Galleries
date: 2025-06-09
permalink: /galleries/
---

<div class="post-grid">
  {% assign galleries = site.data.post_meta.galleries %}
  {% for filename in galleries %}
    {% assign post = site.posts | where_exp: "p", "p.path contains filename" | first %}
    {% if post %}
      <div class="post-box">
        <a href="{{ post.url }}" class="post-box-link">{{ post.title }}</a>
        {% if post.subtitle %}
          <p class="subtitle">{{ post.subtitle }}</p>
        {% endif %}
      </div>
    {% endif %}
  {% endfor %}
</div>
