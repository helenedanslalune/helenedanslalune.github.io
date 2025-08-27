---
layout: post
title: Hélène's Suggestion Of Passwords
subtitle: That You Could Use For Your Main Bank Account Maybe
date: 2025-06-09
permalink: /passwords/
published: true
---

<div id="password-container"></div>

<script>
// List of passwords - just add new ones to this array
const passwords = [
  "12345",
  "123456", 
  "1235813",
  "MrHandsome",
  "MrHandsome123",
  "pleasedonthackme",
  "hubbahubba",
];

// Generate HTML for all passwords
function generatePasswordList() {
  const container = document.getElementById('password-container');
  
  passwords.forEach((password, index) => {
    const passwordDiv = document.createElement('div');
    passwordDiv.style.cssText = 'display: flex; align-items: center; gap: 10px; margin-bottom: 1em;';
    
    const preElement = document.createElement('pre');
    preElement.id = `copy-target-${index}`;
    preElement.style.margin = '0';
    preElement.textContent = password;
    
    const button = document.createElement('button');
    button.textContent = 'Copy';
    button.onclick = () => copyText(`copy-target-${index}`);
    
    passwordDiv.appendChild(preElement);
    passwordDiv.appendChild(button);
    container.appendChild(passwordDiv);
  });
}

function copyText(id) {
  const el = document.getElementById(id);
  if (!el) {
    alert("Element not found.");
    return;
  }
  navigator.clipboard.writeText(el.innerText)
    .then(() => alert("Copied!"))
    .catch(err => alert("Copy failed: " + err));
}

// Generate the password list when page loads
document.addEventListener('DOMContentLoaded', generatePasswordList);
</script>

