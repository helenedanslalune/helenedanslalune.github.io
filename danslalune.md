---
layout: default
permalink: /danslalune/
title: Hélène dans la lune
published: true
---

<script>
document.addEventListener('DOMContentLoaded', function() {
  document.body.classList.add('home');
  
  // Portal entry overlay for first-time visitors
  if (!localStorage.getItem('hasVisited')) {
    showPortalOverlay();
  }
  
  function showPortalOverlay() {
    const overlay = document.createElement('div');
    overlay.id = 'portal-overlay';
    overlay.innerHTML = `
      <div class="portal-background">
        <div class="portal-content">
          <div class="portal-title-box" onclick="enterPortal()">
            <h1 class="portal-title">Hélène dans la lune</h1>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(overlay);
  }
  
  window.enterPortal = function() {
    localStorage.setItem('hasVisited', 'true');
    const overlay = document.getElementById('portal-overlay');
    if (overlay) {
      overlay.style.opacity = '0';
      setTimeout(() => overlay.remove(), 500);
    }
  }
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