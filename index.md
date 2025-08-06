---
layout: default
---

<script>
document.addEventListener('DOMContentLoaded', function() {
  document.body.classList.add('home');
});
</script>

{% assign menu_posts = site.data.post_meta["menu"] %}

<div class="post-grid">
  {% for post in site.posts %}
    {% assign filename = post.path | split: "/" | last %}
    {% if menu_posts contains filename %}
      <a href="{{ post.url }}" class="post-box" style="text-decoration: none; display: block;">
        <span class="post-box-link">{{ post.title }}</span>
        {% if post.subtitle %}
          <p class="subtitle">{{ post.subtitle }}</p>
        {% endif %}
      </a>
    {% endif %}
  {% endfor %}
</div>


