---
layout: default
title: Hélène Colinet
published: true
---

<canvas id="trajectory-canvas"></canvas>
<div id="trajectory-ball"></div>

<div id="menu-arrow">
  <img src="/assets/images/arrow.png" alt="Menu">
</div>

<div id="menu-container">
  <img src="/assets/images/line.png" alt="" class="menu-line">
  <div class="menu-items">
    <a href="/assets/CV.pdf" target="_blank">
      <img src="/assets/images/cv.png" alt="CV" class="menu-item menu-cv">
    </a>
    <a href="https://github.com/helenedanslalune" target="_blank">
      <img src="/assets/images/github.png" alt="GitHub" class="menu-item menu-github">
    </a>
    <a href="/publications">
      <img src="/assets/images/publications.png" alt="Publications" class="menu-item menu-publications">
    </a>
    <a href="/blog">
      <img src="/assets/images/blog.png" alt="Blog" class="menu-item menu-blog">
    </a>
    <a href="/projects">
      <img src="/assets/images/projects.png" alt="Projects" class="menu-item menu-projects">
    </a>
  </div>
  <img src="/assets/images/line2.png" alt="" class="menu-line">
</div>

<div class="handwriting-container">
  <div class="opening-block">
    <img src="/assets/images/left.png" alt="Left" class="opening-left">
    <div class="opening-content">
      <div class="hi-centered">
        <img src="/assets/images/hi.png" alt="Hi" class="handwriting-hi">
      </div>
      <div class="name-line">
        <img src="/assets/images/imhelene.png" alt="I'm Hélène" class="handwriting-name">
      </div>
    </div>
    <img src="/assets/images/right.png" alt="Right" class="opening-right">
  </div>
  <div class="physics-line">
    <img src="/assets/images/imaphysicist.png" alt="I'm a physicist" class="handwriting-physics">
    <img src="/assets/images/specializingin.png" alt="specializing in" class="handwriting-consulting">
    <img src="/assets/images/complexsystems.png" alt="complex systems" class="handwriting-financial">
    <img src="/assets/images/hright.png" alt="HRight" class="handwriting-hright">
  </div>
  <div class="interested-line">
    <img src="/assets/images/3left.png" alt="3Left" class="handwriting-3left">
    <img src="/assets/images/iminterestedin.png" alt="Interested In" class="handwriting-interested">
    <img src="/assets/images/3right.png" alt="3Right" class="handwriting-3right">
  </div>
  <div class="interests-list">
    <img src="/assets/images/smallthings.png" alt="Small Things" class="handwriting-smallthings">
    <img src="/assets/images/continuousprocesses.png" alt="Continuous Processes" class="handwriting-continuous">
    <img src="/assets/images/scales.png" alt="Scales" class="handwriting-scales">
    <canvas id="emergence-canvas" class="handwriting-emergence"></canvas>
    <img src="/assets/images/limits.png" alt="Limits" class="handwriting-limits">
  </div>
  <div class="contact-line">
    <img src="/assets/images/contact.png" alt="Contact" class="handwriting-contact">
    <a href="mailto:hello@helenecoli.net">
      <img src="/assets/images/email.png" alt="Email" class="handwriting-email">
    </a>
  </div>
</div>

<script>
// First visit detection (must run first)
(function() {
  const hasVisited = localStorage.getItem('hasVisited');

  if (!hasVisited) {
    document.body.classList.add('first-visit');
    localStorage.setItem('hasVisited', 'true');
  }
})();

(function() {
  const canvas = document.getElementById('emergence-canvas');
  const ctx = canvas.getContext('2d');
  const img = new Image();

  // Only animate on first visit
  const isFirstVisit = document.body.classList.contains('first-visit');

  if (!isFirstVisit) {
    // Show immediately without animation
    canvas.style.opacity = '1';
    img.onload = function() {
      canvas.width = img.width;
      canvas.height = img.height;
      ctx.drawImage(img, 0, 0);
    };
    img.src = '/assets/images/emergence.png';
    return;
  }

  // Read timing from CSS variable
  const emergenceTime = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--time-emergence')) * 1000;

  img.onload = function() {
    canvas.width = img.width;
    canvas.height = img.height;

    const cols = 80;
    const rows = 8;
    const tileWidth = img.width / cols;
    const tileHeight = img.height / rows;
    const totalTiles = cols * rows;

    // Create array of tile indices and shuffle
    const tiles = Array.from({length: totalTiles}, (_, i) => i);
    for (let i = tiles.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [tiles[i], tiles[j]] = [tiles[j], tiles[i]];
    }

    let currentTile = 0;

    function drawTile() {
      // Draw 10 tiles at once for speed
      for (let i = 0; i < 10 && currentTile < totalTiles; i++) {
        const tileIndex = tiles[currentTile];
        const col = tileIndex % cols;
        const row = Math.floor(tileIndex / cols);

        ctx.drawImage(
          img,
          col * tileWidth, row * tileHeight, tileWidth, tileHeight,
          col * tileWidth, row * tileHeight, tileWidth, tileHeight
        );

        currentTile++;
      }

      if (currentTile < totalTiles) {
        setTimeout(drawTile, 8);
      }
    }

    // Start based on CSS variable timing
    setTimeout(() => {
      canvas.style.opacity = '1';
      drawTile();
    }, emergenceTime);
  };

  img.src = '/assets/images/emergence.png';
})();

(function() {
  // Only animate on first visit
  const isFirstVisit = document.body.classList.contains('first-visit');

  const canvasWidth = window.innerWidth * 0.95;
  const trajectoryHeight = window.innerHeight * 0.35;
  const startX = window.innerWidth * -0.05;
  const startY = window.innerHeight * 0.15;

  const canvas = document.getElementById('trajectory-canvas');
  const ball = document.getElementById('trajectory-ball');

  if (!isFirstVisit) {
    // Hide trajectory canvas but show ball at final position on return visits
    canvas.style.display = 'none';

    async function positionBall() {
      const response = await fetch('fullpot.csv');
      const text = await response.text();
      const lines = text.trim().split('\n');

      const trajectoryData = [];
      for (let i = 0; i < lines.length; i += 2) {
        const value = parseFloat(lines[i].trim());
        if (!isNaN(value)) trajectoryData.push(value);
      }

      // Position ball at end of trajectory
      const lastValue = trajectoryData[trajectoryData.length - 1];
      const normalizedY = (lastValue - 9) / (35 - 9);
      const finalX = startX + canvasWidth;
      const finalY = startY + (1 - normalizedY) * trajectoryHeight;

      ball.style.left = (finalX - 30) + 'px';
      ball.style.top = (finalY - 30) + 'px';
    }

    positionBall();
    return;
  }

  let trajectoryData = [];
  let trajectoryPoints = [];
  let animationStartTime = null;
  let fadeOutStartTime = null;

  // Read timing from CSS variable
  const trajectoryTime = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--time-trajectory')) * 1000;

  const animationDuration = 3800; // 3.75 seconds total animation time
  const fadeOutDuration = 1000; // 1 second fade out

  const ctx = canvas.getContext('2d');

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  async function loadData() {
    const response = await fetch('fullpot.csv');
    const text = await response.text();
    const lines = text.trim().split('\n');

    for (let i = 0; i < lines.length; i += 2) {
      const value = parseFloat(lines[i].trim());
      if (!isNaN(value)) trajectoryData.push(value);
    }

    const firstValue = trajectoryData[0];
    const normalizedY = (firstValue - 9) / (35 - 9);
    const initialY = startY + (1 - normalizedY) * trajectoryHeight;
    ball.style.left = (startX - 30) + 'px';
    ball.style.top = (initialY - 30) + 'px';

    // Start based on CSS variable timing
    setTimeout(() => {
      animationStartTime = performance.now();
      requestAnimationFrame(animate);
    }, trajectoryTime);
  }

  function animate(currentTime) {
    if (!animationStartTime) return;

    const elapsed = currentTime - animationStartTime;
    const progress = Math.min(elapsed / animationDuration, 1);
    const currentIndex = Math.floor(progress * (trajectoryData.length - 1));

    // Apply fading
    if (progress >= 1) {
      if (!fadeOutStartTime) {
        fadeOutStartTime = currentTime;
      }
      const fadeElapsed = currentTime - fadeOutStartTime;
      if (fadeElapsed >= fadeOutDuration) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        return;
      }
      const fadeStrength = 0.3;
      ctx.fillStyle = `rgba(0, 0, 0, ${fadeStrength})`;
    } else {
      const fadeStrength = 0.05;
      ctx.fillStyle = `rgba(0, 0, 0, ${fadeStrength})`;
    }

    ctx.globalCompositeOperation = 'destination-out';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.globalCompositeOperation = 'source-over';

    if (progress < 1) {
      const x = startX + (progress * canvasWidth);
      const yValue = trajectoryData[currentIndex];
      const normalizedY = (yValue - 9) / (35 - 9);
      const y = startY + (1 - normalizedY) * trajectoryHeight;

      trajectoryPoints.push({x, y});

      if (trajectoryPoints.length > 2) {
        const p0 = trajectoryPoints[trajectoryPoints.length - 3];
        const p1 = trajectoryPoints[trajectoryPoints.length - 2];
        const p2 = trajectoryPoints[trajectoryPoints.length - 1];

        ctx.strokeStyle = 'black';
        ctx.lineWidth = 2;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.beginPath();
        ctx.moveTo(p0.x, p0.y);
        ctx.quadraticCurveTo(p1.x, p1.y, p2.x, p2.y);
        ctx.stroke();
      } else if (trajectoryPoints.length === 2) {
        const p0 = trajectoryPoints[0];
        const p1 = trajectoryPoints[1];
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 2;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.beginPath();
        ctx.moveTo(p0.x, p0.y);
        ctx.lineTo(p1.x, p1.y);
        ctx.stroke();
      }

      ball.style.left = (x - 30) + 'px';
      ball.style.top = (y - 30) + 'px';
    }

    requestAnimationFrame(animate);
  }

  loadData();
})();

// Menu toggle
(function() {
  const arrow = document.getElementById('menu-arrow');
  const menu = document.getElementById('menu-container');
  const body = document.body;

  arrow.addEventListener('click', function(event) {
    event.stopPropagation();
    menu.classList.toggle('open');
    body.classList.toggle('menu-open');
  });

  // Close menu when clicking outside
  document.addEventListener('click', function(event) {
    if (!menu.contains(event.target)) {
      menu.classList.remove('open');
      body.classList.remove('menu-open');
    }
  });
})();
</script>
