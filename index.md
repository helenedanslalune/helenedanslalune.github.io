---
layout: default
---

# fatal system error
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a><br>
      <small>{{ post.subtitle }}</small>
    </li>
  {% endfor %}
</ul>

