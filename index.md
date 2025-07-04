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
      <div class="post-box">
        <a href="{{ post.url }}" class="post-box-link">{{ post.title }}</a>
        {% if post.subtitle %}
          <p class="subtitle">{{ post.subtitle }}</p>
        {% endif %}
      </div>
    {% endif %}
  {% endfor %}
</div>


