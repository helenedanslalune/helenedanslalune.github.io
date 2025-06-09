---
layout: default
---

{% assign menu_posts = site.data.post_meta["menu"] %}

<ul>
  {% for post in site.posts %}
    {% assign filename = post.path | split: "/" | last %}
    {% if menu_posts contains filename %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        {% if post.subtitle %}
          <p class="subtitle" style="font-size: 1rem; color: #666;">{{ post.subtitle }}</p>
        {% endif %}
      </li>
    {% endif %}
  {% endfor %}
</ul>


