---
layout: post
title: Hélène's Suggestions Of Passwords
subtitle: That You Could Use For Your Main Bank Account Maybe
date: 2025-06-09
permalink: /passwords/
---
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 1em;">
  <pre id="copy-target-1" style="margin: 0;">12345</pre>
  <button onclick="copyText('copy-target-1')">Copy</button>
</div>

<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 1em;">
  <pre id="copy-target-2" style="margin: 0;">123456</pre>
  <button onclick="copyText('copy-target-2')">Copy</button>
</div>

<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 1em;">
  <pre id="copy-target-3" style="margin: 0;">MrHandsome</pre>
  <button onclick="copyText('copy-target-3')">Copy</button>
</div>

<script>
function copyText(id) {
  var el = document.getElementById(id);
  if (!el) {
    alert("Element not found.");
    return;
  }
  navigator.clipboard.writeText(el.innerText)
    .then(() => alert("Copied!"))
    .catch(err => alert("Copy failed: " + err));
}
</script>

