---
layout: post
title: Hélène's Galleries
date: 2025-06-09
permalink: /galleries/
---

<div class="post-grid">
  {% assign galleries = site.data.post_meta.galleries %}
  {% for filename in galleries %}
    {% for post in site.posts %}
      {% assign post_filename = post.path | split: "/" | last %}
      {% if post_filename == filename %}
        <a href="{{ post.url }}" class="post-box" style="text-decoration: none; display: block;">
          <span class="post-box-link">{{ post.title }}</span>
          {% if post.subtitle %}
            <p class="subtitle">{{ post.subtitle }}</p>
          {% endif %}
        </a>
        {% break %}
      {% endif %}
    {% endfor %}
  {% endfor %}
</div>
