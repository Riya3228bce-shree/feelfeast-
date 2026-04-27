<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Mood Food Explorer</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --accent: #D85A30;
      --accent-light: #FAECE7;
      --accent-dark: #993C1D;
      --green: #3B6D11;
      --green-light: #EAF3DE;
      --blue: #185FA5;
      --blue-light: #E6F1FB;
      --blue-dark: #0C447C;
      --bg: #FAFAF8;
      --surface: #FFFFFF;
      --border: rgba(0,0,0,0.10);
      --text: #1a1a18;
      --muted: #5F5E5A;
      --hint: #888780;
      --radius: 12px;
      --radius-sm: 8px;
    }

    body {
      font-family: 'DM Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
    }

    /* ── HEADER ── */
    header {
      background: var(--surface);
      border-bottom: 0.5px solid var(--border);
      padding: 1.25rem 2rem;
      display: flex;
      align-items: center;
      gap: 14px;
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .logo-mark {
      width: 38px; height: 38px;
      background: var(--accent);
      border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      font-size: 20px;
      flex-shrink: 0;
    }
    header h1 {
      font-family: 'Playfair Display', serif;
      font-size: 20px;
      font-weight: 700;
      color: var(--text);
    }
    header p {
      font-size: 12px;
      color: var(--muted);
      margin-top: 1px;
    }

    /* ── LAYOUT ── */
    .container {
      max-width: 840px;
      margin: 0 auto;
      padding: 2rem 1.5rem 4rem;
    }

    /* ── SECTION LABELS ── */
    .section-label {
      font-size: 10px;
      font-weight: 500;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--hint);
      margin-bottom: 12px;
    }

    /* ── MOOD GRID ── */
    .mood-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-bottom: 2rem;
    }
    @media (max-width: 480px) {
      .mood-grid { grid-template-columns: repeat(2, 1fr); }
    }
    .mood-btn {
      padding: 16px 10px;
      border: 0.5px solid var(--border);
      border-radius: var(--radius);
      background: var(--surface);
      cursor: pointer;
      text-align: center;
      transition: all 0.15s ease;
      user-select: none;
    }
    .mood-btn:hover { background: var(--bg); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
    .mood-btn.active { background: var(--accent-light); border-color: var(--accent); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(216,90,48,0.15); }
    .mood-icon { font-size: 28px; display: block; margin-bottom: 6px; }
    .mood-name { font-size: 12px; font-weight: 500; color: var(--muted); }
    .mood-btn.active .mood-name { color: var(--accent-dark); }

    /* ── PREF ROW ── */
    .pref-row {
      display: flex;
      gap: 10px;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }
    .pref-btn {
      flex: 1;
      min-width: 120px;
      padding: 11px 16px;
      border: 0.5px solid var(--border);
      border-radius: var(--radius-sm);
      background: var(--surface);
      cursor: pointer;
      font-family: 'DM Sans', sans-serif;
      font-size: 13px;
      font-weight: 500;
      color: var(--muted);
      transition: all 0.15s;
    }
    .pref-btn:hover { background: var(--bg); }
    .pref-btn.active-veg { background: var(--green-light); border-color: var(--green); color: var(--green); }
    .pref-btn.active-nonveg { background: var(--accent-light); border-color: var(--accent); color: var(--accent-dark); }
    .pref-btn.active-both { background: var(--blue-light); border-color: var(--blue); color: var(--blue-dark); }

    /* ── CUISINE PILLS ── */
    .cuisine-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 2rem;
    }
    .cuisine-pill {
      padding: 7px 16px;
      border: 0.5px solid var(--border);
      border-radius: 20px;
      background: var(--surface);
      cursor: pointer;
      font-family: 'DM Sans', sans-serif;
      font-size: 12px;
      font-weight: 500;
      color: var(--muted);
      transition: all 0.15s;
    }
    .cuisine-pill:hover { background: var(--bg); }
    .cuisine-pill.active { background: var(--blue-light); border-color: var(--blue); color: var(--blue-dark); }

    /* ── GO BUTTON ── */
    .go-btn {
      width: 100%;
      padding: 15px;
      background: var(--accent);
      color: #fff;
      border: none;
      border-radius: var(--radius);
      font-family: 'DM Sans', sans-serif;
      font-size: 15px;
      font-weight: 500;
      cursor: pointer;
      margin-bottom: 2.5rem;
      transition: background 0.15s, transform 0.1s;
      letter-spacing: 0.01em;
    }
    .go-btn:hover { background: var(--accent-dark); transform: translateY(-1px); }
    .go-btn:active { transform: scale(0.99); }
    .go-btn:disabled { background: #D3D1C7; color: #888780; cursor: not-allowed; transform: none; }

    /* ── TABS ── */
    .tabs {
      display: flex;
      border: 0.5px solid var(--border);
      border-radius: var(--radius-sm);
      overflow: hidden;
      margin-bottom: 2rem;
      background: var(--surface);
    }
    .tab-btn {
      flex: 1;
      padding: 11px;
      background: transparent;
      border: none;
      cursor: pointer;
      font-family: 'DM Sans', sans-serif;
      font-size: 13px;
      font-weight: 500;
      color: var(--muted);
      border-right: 0.5px solid var(--border);
      transition: all 0.15s;
    }
    .tab-btn:last-child { border-right: none; }
    .tab-btn.active { background: var(--accent-light); color: var(--accent-dark); }
    .tab-btn:hover:not(.active) { background: var(--bg); }

    .tab-content { display: none; }
    .tab-content.active { display: block; }

    /* ── RESULT AREA ── */
    .result-area { display: none; }
    .result-area.visible { display: block; }

    /* ── LOADING ── */
    .loading-msg { text-align: center; padding: 3rem 1rem; }
    .spinner {
      width: 32px; height: 32px;
      border: 2.5px solid var(--border);
      border-top-color: var(--accent);
      border-radius: 50%;
      animation: spin 0.7s linear infinite;
      margin: 0 auto 14px;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    .loading-msg p { font-size: 13px; color: var(--muted); }

    /* ── RESULT HEADER ── */
    .result-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 14px;
      padding-bottom: 14px;
      border-bottom: 0.5px solid var(--border);
      flex-wrap: wrap;
    }
    .badge {
      padding: 4px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 500;
    }
    .badge-mood { background: var(--accent-light); color: var(--accent-dark); }
    .badge-veg { background: var(--green-light); color: var(--green); }
    .badge-nonveg { background: var(--accent-light); color: var(--accent-dark); }
    .badge-both { background: var(--blue-light); color: var(--blue-dark); }
    .result-headline {
      font-size: 13px;
      color: var(--muted);
      margin-bottom: 1.5rem;
      line-height: 1.7;
    }

    /* ── DISH CARDS ── */
    .dish-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 2rem;
    }
    @media (max-width: 560px) {
      .dish-grid { grid-template-columns: 1fr; }
    }
    .dish-card {
      background: var(--surface);
      border: 0.5px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      transition: box-shadow 0.15s;
    }
    .dish-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.07); }
    .dish-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 6px;
    }
    .dish-name {
      font-family: 'Playfair Display', serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--text);
      line-height: 1.3;
      flex: 1;
    }
    .dish-type-tag {
      font-size: 10px;
      font-weight: 500;
      padding: 3px 9px;
      border-radius: 10px;
      margin-left: 10px;
      flex-shrink: 0;
    }
    .tag-veg { background: var(--green-light); color: var(--green); }
    .tag-nonveg { background: var(--accent-light); color: var(--accent-dark); }
    .dish-origin { font-size: 11px; color: var(--hint); margin-bottom: 8px; }
    .dish-desc { font-size: 12px; color: var(--muted); line-height: 1.65; }

    /* ── WORLD CUISINES ── */
    .country-block { margin-bottom: 2rem; }
    .country-header {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    }
    .country-flag { font-size: 26px; line-height: 1; margin-top: 2px; }
    .country-name {
      font-family: 'Playfair Display', serif;
      font-size: 17px;
      font-weight: 700;
      color: var(--text);
      line-height: 1.2;
    }
    .country-culture { font-size: 12px; color: var(--muted); margin-top: 3px; line-height: 1.5; }

    .country-dishes-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    @media (max-width: 560px) {
      .country-dishes-grid { grid-template-columns: 1fr; }
    }
    .mini-dish-card {
      background: var(--surface);
      border: 0.5px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }
    .type-dot {
      width: 9px; height: 9px;
      border-radius: 50%;
      margin-top: 5px;
      flex-shrink: 0;
    }
    .dot-veg { background: var(--green); }
    .dot-nonveg { background: var(--accent); }
    .mini-dish-name { font-size: 13px; font-weight: 500; color: var(--text); margin-bottom: 3px; }
    .mini-dish-note { font-size: 11px; color: var(--muted); line-height: 1.55; }

    .divider { border: none; border-top: 0.5px solid var(--border); margin: 1.75rem 0; }

    /* ── LEGEND ── */
    .legend {
      display: flex;
      gap: 16px;
      align-items: center;
      margin-bottom: 1rem;
      font-size: 12px;
      color: var(--muted);
    }
    .legend-item { display: flex; align-items: center; gap: 6px; }
    .legend-dot { width: 9px; height: 9px; border-radius: 50%; }

    /* ── ERROR ── */
    .error-msg {
      background: #FCEBEB;
      border: 0.5px solid #E24B4A;
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      font-size: 13px;
      color: #A32D2D;
    }

    /* ── FOOTER ── */
    footer {
      text-align: center;
      padding: 2rem;
      font-size: 11px;
      color: var(--hint);
      border-top: 0.5px solid var(--border);
    }
  </style>
</head>
<body>

  <header>
    <div class="logo-mark">🍽️</div>
    <div>
      <h1>Mood Food Explorer</h1>
      <p>AI-powered global cuisine recommendations</p>
    </div>
  </header>

  <div class="container">

    <!-- MOOD SELECTOR -->
    <div class="section-label">How are you feeling right now?</div>
    <div class="mood-grid" id="moodGrid">
      <button class="mood-btn" data-mood="Happy"><span class="mood-icon">😄</span><span class="mood-name">Happy</span></button>
      <button class="mood-btn" data-mood="Sad"><span class="mood-icon">😢</span><span class="mood-name">Sad</span></button>
      <button class="mood-btn" data-mood="Stressed"><span class="mood-icon">😤</span><span class="mood-name">Stressed</span></button>
      <button class="mood-btn" data-mood="Romantic"><span class="mood-icon">🥰</span><span class="mood-name">Romantic</span></button>
      <button class="mood-btn" data-mood="Adventurous"><span class="mood-icon">🤠</span><span class="mood-name">Adventurous</span></button>
      <button class="mood-btn" data-mood="Tired"><span class="mood-icon">😴</span><span class="mood-name">Tired</span></button>
      <button class="mood-btn" data-mood="Lazy"><span class="mood-icon">🛋️</span><span class="mood-name">Lazy</span></button>
      <button class="mood-btn" data-mood="Energetic"><span class="mood-icon">⚡</span><span class="mood-name">Energetic</span></button>
    </div>

    <!-- PREFERENCE -->
    <div class="section-label">Dietary preference</div>
    <div class="pref-row" id="prefRow">
      <button class="pref-btn active-veg" data-pref="Veg">🌿 Vegetarian</button>
      <button class="pref-btn" data-pref="Non-Veg">🍗 Non-Vegetarian</button>
      <button class="pref-btn" data-pref="Both">🍽️ Show Both</button>
    </div>

    <!-- CUISINE FILTER -->
    <div class="section-label">Cuisine preference</div>
    <div class="cuisine-row" id="cuisineRow">
      <button class="cuisine-pill active" data-cuisine="All">🌍 All</button>
      <button class="cuisine-pill" data-cuisine="Indian">🇮🇳 Indian</button>
      <button class="cuisine-pill" data-cuisine="Italian">🇮🇹 Italian</button>
      <button class="cuisine-pill" data-cuisine="Chinese">🇨🇳 Chinese</button>
      <button class="cuisine-pill" data-cuisine="Mexican">🇲🇽 Mexican</button>
      <button class="cuisine-pill" data-cuisine="Japanese">🇯🇵 Japanese</button>
      <button class="cuisine-pill" data-cuisine="Middle Eastern">🥙 Middle Eastern</button>
      <button class="cuisine-pill" data-cuisine="French">🇫🇷 French</button>
      <button class="cuisine-pill" data-cuisine="Thai">🇹🇭 Thai</button>
    </div>

    <!-- GO BUTTON -->
    <button class="go-btn" id="goBtn" disabled>Select a mood to get recommendations</button>

    <!-- RESULT AREA -->
    <div class="result-area" id="resultArea">
      <div class="tabs">
        <button class="tab-btn active" data-tab="mood">🍛 Mood-Based Picks</button>
        <button class="tab-btn" data-tab="world">🌍 World Cuisines</button>
      </div>

      <!-- MOOD TAB -->
      <div class="tab-content active" id="tab-mood">
        <div class="loading-msg" id="loadingMood">
          <div class="spinner"></div>
          <p>Finding the perfect dishes for your mood…</p>
        </div>
        <div id="moodResults"></div>
      </div>

      <!-- WORLD TAB -->
      <div class="tab-content" id="tab-world">
        <div class="loading-msg" id="loadingWorld">
          <div class="spinner"></div>
          <p>Exploring world cuisines…</p>
        </div>
        <div id="worldResults"></div>
      </div>
    </div>

  </div>

  <footer>Powered by Claude AI &nbsp;·&nbsp; Mood Food Explorer &copy; 2025</footer>

  <script>
    let selMood = null, selPref = 'Veg', selCuisine = 'All';

    // Mood selection
    document.getElementById('moodGrid').addEventListener('click', e => {
      const btn = e.target.closest('.mood-btn');
      if (!btn) return;
      document.querySelectorAll('.mood-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selMood = btn.dataset.mood;
      const goBtn = document.getElementById('goBtn');
      goBtn.disabled = false;
      goBtn.textContent = `Get food recommendations for "${selMood}" mood →`;
    });

    // Preference selection
    document.getElementById('prefRow').addEventListener('click', e => {
      const btn = e.target.closest('.pref-btn');
      if (!btn) return;
      document.querySelectorAll('.pref-btn').forEach(b => b.classList.remove('active-veg','active-nonveg','active-both'));
      selPref = btn.dataset.pref;
      if (selPref === 'Veg') btn.classList.add('active-veg');
      else if (selPref === 'Non-Veg') btn.classList.add('active-nonveg');
      else btn.classList.add('active-both');
    });

    // Cuisine selection
    document.getElementById('cuisineRow').addEventListener('click', e => {
      const btn = e.target.closest('.cuisine-pill');
      if (!btn) return;
      document.querySelectorAll('.cuisine-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selCuisine = btn.dataset.cuisine;
    });

    // Tab switching
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
        btn.classList.add('active');
        document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
      });
    });

    // Main action
    document.getElementById('goBtn').addEventListener('click', async () => {
      if (!selMood) return;

      const resultArea = document.getElementById('resultArea');
      resultArea.className = 'result-area visible';
      document.getElementById('moodResults').innerHTML = '';
      document.getElementById('worldResults').innerHTML = '';
      document.getElementById('loadingMood').style.display = 'block';
      document.getElementById('loadingWorld').style.display = 'block';
      document.querySelectorAll('.tab-btn')[0].click();

      const prefLabel = selPref === 'Veg' ? 'vegetarian only' : selPref === 'Non-Veg' ? 'non-vegetarian only' : 'both vegetarian and non-vegetarian';
      const cuisineNote = selCuisine === 'All'
        ? 'from various cuisines including Indian, Italian, Chinese, Japanese, Mexican, French, Thai, Middle Eastern'
        : `from ${selCuisine} cuisine specifically`;

      const moodPrompt = `You are a world-class food expert and nutritionist. The user is feeling "${selMood}" and wants ${prefLabel} food recommendations ${cuisineNote}.

Return ONLY valid JSON (no markdown, no backticks, no preamble):
{
  "mood": "${selMood}",
  "pref": "${selPref}",
  "headline": "One warm, encouraging sentence about this mood and how food can help",
  "dishes": [
    {
      "name": "Exact Dish Name",
      "origin": "Country or Region",
      "cuisine": "Cuisine Category",
      "type": "Veg or Non-Veg",
      "desc": "2 sentences: what the dish is and specifically why it suits this mood"
    }
  ]
}

Include exactly 6 dishes. Make them authentic, specific, culturally accurate real dishes. Include a mix of national (Indian) and international dishes unless a specific cuisine was chosen. Match the mood psychology to the food properties.`;

      const worldPrompt = `You are a cultural food historian and culinary expert. Provide authentic famous traditional dishes from 6 countries: India, Italy, Japan, Mexico, France, and Morocco.

Return ONLY valid JSON (no markdown, no backticks, no preamble):
{
  "countries": [
    {
      "name": "Country Name",
      "flag": "Flag emoji",
      "culture_note": "One vivid sentence about the food culture, traditions, or philosophy of this country",
      "dishes": [
        {
          "name": "Exact Dish Name",
          "type": "Veg or Non-Veg",
          "note": "One sentence about this dish's cultural significance or origin story"
        }
      ]
    }
  ]
}

Include exactly 3 dishes per country. Mix veg and non-veg where culturally authentic. Be specific — no generic names, only real dishes.`;

      try {
        const [moodRes, worldRes] = await Promise.all([
          fetch("https://api.anthropic.com/v1/messages", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              model: "claude-sonnet-4-20250514",
              max_tokens: 1000,
              messages: [{ role: "user", content: moodPrompt }]
            })
          }),
          fetch("https://api.anthropic.com/v1/messages", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              model: "claude-sonnet-4-20250514",
              max_tokens: 1200,
              messages: [{ role: "user", content: worldPrompt }]
            })
          })
        ]);

        const [moodData, worldData] = await Promise.all([moodRes.json(), worldRes.json()]);

        document.getElementById('loadingMood').style.display = 'none';
        document.getElementById('loadingWorld').style.display = 'none';

        // ── Render Mood Results ──
        try {
          const raw = moodData.content.map(i => i.text || '').join('');
          const clean = raw.replace(/```json|```/g, '').trim();
          const parsed = JSON.parse(clean);

          const prefBadgeClass = selPref === 'Veg' ? 'badge-veg' : selPref === 'Non-Veg' ? 'badge-nonveg' : 'badge-both';

          let html = `
            <div class="result-header">
              <span class="badge badge-mood">${parsed.mood}</span>
              <span class="badge ${prefBadgeClass}">${parsed.pref}</span>
              ${selCuisine !== 'All' ? `<span class="badge badge-both">${selCuisine}</span>` : ''}
            </div>
            <p class="result-headline">${parsed.headline}</p>
            <div class="dish-grid">
          `;

          parsed.dishes.forEach(d => {
            const isVeg = d.type === 'Veg';
            html += `
              <div class="dish-card">
                <div class="dish-top">
                  <div class="dish-name">${d.name}</div>
                  <span class="dish-type-tag ${isVeg ? 'tag-veg' : 'tag-nonveg'}">${d.type}</span>
                </div>
                <div class="dish-origin">${d.origin} &nbsp;·&nbsp; ${d.cuisine}</div>
                <div class="dish-desc">${d.desc}</div>
              </div>
            `;
          });

          html += '</div>';
          document.getElementById('moodResults').innerHTML = html;
        } catch (e) {
          document.getElementById('moodResults').innerHTML = '<div class="error-msg">Could not parse mood recommendations. Please try again.</div>';
        }

        // ── Render World Cuisine Results ──
        try {
          const raw2 = worldData.content.map(i => i.text || '').join('');
          const clean2 = raw2.replace(/```json|```/g, '').trim();
          const parsed2 = JSON.parse(clean2);

          let html2 = `
            <div class="legend">
              <div class="legend-item"><div class="legend-dot" style="background:var(--green)"></div> Vegetarian</div>
              <div class="legend-item"><div class="legend-dot" style="background:var(--accent)"></div> Non-Vegetarian</div>
            </div>
          `;

          parsed2.countries.forEach((c, idx) => {
            html2 += `
              <div class="country-block">
                <div class="country-header">
                  <span class="country-flag">${c.flag}</span>
                  <div>
                    <div class="country-name">${c.name}</div>
                    <div class="country-culture">${c.culture_note}</div>
                  </div>
                </div>
                <div class="country-dishes-grid">
            `;

            c.dishes.forEach(d => {
              const isVeg = d.type === 'Veg';
              html2 += `
                <div class="mini-dish-card">
                  <div class="type-dot ${isVeg ? 'dot-veg' : 'dot-nonveg'}"></div>
                  <div>
                    <div class="mini-dish-name">${d.name}</div>
                    <div class="mini-dish-note">${d.note}</div>
                  </div>
                </div>
              `;
            });

            html2 += '</div>';
            if (idx < parsed2.countries.length - 1) html2 += '<hr class="divider">';
            html2 += '</div>';
          });

          document.getElementById('worldResults').innerHTML = html2;
        } catch (e) {
          document.getElementById('worldResults').innerHTML = '<div class="error-msg">Could not parse world cuisines. Please try again.</div>';
        }

      } catch (err) {
        document.getElementById('loadingMood').style.display = 'none';
        document.getElementById('loadingWorld').style.display = 'none';
        document.getElementById('moodResults').innerHTML = '<div class="error-msg">Network error. Please check your connection and try again.</div>';
      }
    });
  </script>
</body>
</html>
