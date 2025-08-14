---
layout: post
title: Hélène's Sidequests
subtitle: That Have Monopolized Her Attention And Distracted Her From Urgent And Important Matters
date: 2025-06-09
permalink: /sidequests/
---

<div class="post-grid">
  {% assign sidequests = site.data.post_meta.sidequests %}
  {% for filename in sidequests %}
    {% assign post = site.posts | where_exp: "p", "p.path contains filename" | first %}
    {% if post %}
      <a href="{{ post.url }}" class="post-box" style="text-decoration: none; display: block;">
        <span class="post-box-link">{{ post.title }}</span>
        {% if post.subtitle %}
          <p class="subtitle">{{ post.subtitle }}</p>
        {% endif %}
      </a>
    {% endif %}
  {% endfor %}
</div>
