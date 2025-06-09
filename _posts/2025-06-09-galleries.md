---
layout: post
title: Hélène's Galleries
date: 2025-06-09
permalink: /galleries/
---

<ul>
  {% assign galleries = site.data.post_meta.galleries %}
  {% for filename in galleries %}
    {% assign post = site.posts | where_exp: "p", "p.path contains filename" | first %}
    {% if post %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
