#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>La Bibbia_di_Python - Dal principiante al Business Analyst</title>
<style>
:root{
  --bg:#FAFAF7;--surface:#FFFFFF;--surface-2:#F1EFE8;--text:#2C2C2A;--text-2:#5F5E5A;--text-3:#888780;
  --border:#D3D1C7;--border-2:#B4B2A9;
  --purple:#3C3489;--purple-l:#EEEDFE;--purple-m:#AFA9EC;
  --teal:#0F6E56;--teal-l:#E1F5EE;--teal-m:#5DCAA5;
  --amber:#633806;--amber-l:#FAEEDA;--amber-m:#EF9F27;
  --blue:#0C447C;--blue-l:#E6F1FB;--blue-m:#85B7EB;
  --coral:#712B13;--coral-l:#FAECE7;--coral-m:#F0997B;
  --green:#27500A;--green-l:#EAF3DE;--green-m:#97C459;
  --red:#791F1F;--red-l:#FCEBEB;--red-m:#F09595;
  --pink:#72243E;--pink-l:#FBEAF0;--pink-m:#ED93B1;
  --radius:8px;--radius-lg:12px;
  --mono:'SF Mono', Monaco, Menlo, Consolas, 'Courier New', monospace;
  --sans:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
@media(prefers-color-scheme:dark){
  :root{
    --bg:#1A1A18;--surface:#26261F;--surface-2:#2C2C24;--text:#E8E6DC;--text-2:#B4B2A9;--text-3:#888780;
    --border:#3D3D36;--border-2:#4A4A42;
    --purple-l:#26215C;--teal-l:#04342C;--amber-l:#412402;--blue-l:#042C53;
    --coral-l:#4A1B0C;--green-l:#173404;--red-l:#501313;--pink-l:#4B1528;
  }
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:var(--sans);background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh;}
.app{display:grid;grid-template-columns:280px 1fr;min-height:100vh;}
.sidebar{background:var(--surface);border-right:0.5px solid var(--border);padding:20px 16px;overflow-y:auto;position:sticky;top:0;height:100vh;}
.sidebar-header{padding:0 8px 16px;border-bottom:0.5px solid var(--border);margin-bottom:16px;}
.logo{font-size:16px;font-weight:600;color:var(--text);margin-bottom:4px;}
.logo-sub{font-size:12px;color:var(--text-2);}
.progress-global{margin:14px 0 8px;}
.progress-label{font-size:11px;color:var(--text-2);margin-bottom:5px;display:flex;justify-content:space-between;}
.progress-bar-wrap{height:5px;background:var(--surface-2);border-radius:10px;overflow:hidden;}
.progress-bar{height:100%;background:linear-gradient(90deg,var(--purple) 0%,var(--teal) 100%);transition:width 0.4s;}
.phase-list{list-style:none;}
.phase-group{margin-bottom:6px;}
.phase-header{padding:8px 10px;font-size:11px;font-weight:600;color:var(--text-3);text-transform:uppercase;letter-spacing:0.05em;}
.phase-item{display:flex;align-items:center;gap:10px;padding:8px 10px;font-size:13px;color:var(--text-2);cursor:pointer;border-radius:var(--radius);transition:all 0.15s;border:none;background:none;width:100%;text-align:left;font-family:inherit;}
.phase-item:hover{background:var(--surface-2);color:var(--text);}
.phase-item.active{background:var(--purple-l);color:var(--purple);font-weight:500;}
.phase-item.done{color:var(--teal);}
.phase-dot{width:18px;height:18px;border-radius:50%;background:var(--surface-2);display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:600;color:var(--text-3);flex-shrink:0;}
.phase-item.active .phase-dot{background:var(--purple);color:#fff;}
.phase-item.done .phase-dot{background:var(--teal);color:#fff;}
.phase-item.done .phase-dot::after{content:'✓';}
.phase-item.done .phase-num{display:none;}
.main{padding:32px 40px;max-width:1000px;overflow-x:hidden;}
.page{display:none;animation:fade 0.3s ease;}
.page.active{display:block;}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.page-header{margin-bottom:24px;padding-bottom:16px;border-bottom:0.5px solid var(--border);}
.page-kicker{font-size:12px;color:var(--purple);font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;}
.page-title{font-size:26px;font-weight:600;color:var(--text);margin-bottom:8px;}
.page-sub{font-size:14px;color:var(--text-2);max-width:680px;line-height:1.7;}
.section{margin-bottom:32px;}
.section-title{font-size:18px;font-weight:600;color:var(--text);margin-bottom:4px;display:flex;align-items:center;gap:10px;}
.section-sub{font-size:13px;color:var(--text-2);margin-bottom:16px;line-height:1.6;}
.card{background:var(--surface);border:0.5px solid var(--border);border-radius:var(--radius-lg);padding:16px 20px;margin-bottom:14px;}
.card-title{font-size:14px;font-weight:600;color:var(--text);margin-bottom:8px;display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.card-body{font-size:13.5px;color:var(--text-2);line-height:1.75;margin-bottom:10px;}
.card-body strong{color:var(--text);font-weight:600;}
.badge{display:inline-block;padding:2px 9px;border-radius:6px;font-size:11px;font-weight:600;letter-spacing:0.01em;}
.b-purple{background:var(--purple-l);color:var(--purple);}
.b-teal{background:var(--teal-l);color:var(--teal);}
.b-amber{background:var(--amber-l);color:var(--amber);}
.b-blue{background:var(--blue-l);color:var(--blue);}
.b-coral{background:var(--coral-l);color:var(--coral);}
.b-green{background:var(--green-l);color:var(--green);}
.b-red{background:var(--red-l);color:var(--red);}
.b-pink{background:var(--pink-l);color:var(--pink);}
.code{background:var(--surface-2);border-radius:var(--radius);padding:12px 14px;font-family:var(--mono);font-size:13px;line-height:1.7;white-space:pre;overflow-x:auto;margin:8px 0;border:0.5px solid var(--border);}
code.inline{background:var(--surface-2);padding:1px 6px;border-radius:4px;font-family:var(--mono);font-size:12.5px;color:var(--text);}
.kw{color:var(--purple);font-weight:600;}
.str{color:var(--teal);}
.num{color:var(--amber);}
.cm{color:var(--text-3);font-style:italic;}
.fn{color:var(--blue);}
.note{border-left:3px solid var(--purple-m);background:var(--purple-l);padding:10px 14px;border-radius:0 var(--radius) var(--radius) 0;font-size:13px;color:var(--purple);margin:10px 0;line-height:1.7;}
.warn{border-left:3px solid var(--amber-m);background:var(--amber-l);padding:10px 14px;border-radius:0 var(--radius) var(--radius) 0;font-size:13px;color:var(--amber);margin:10px 0;line-height:1.7;}
.ok{border-left:3px solid var(--teal-m);background:var(--teal-l);padding:10px 14px;border-radius:0 var(--radius) var(--radius) 0;font-size:13px;color:var(--teal);margin:10px 0;line-height:1.7;}
.err{border-left:3px solid var(--red-m);background:var(--red-l);padding:10px 14px;border-radius:0 var(--radius) var(--radius) 0;font-size:13px;color:var(--red);margin:10px 0;line-height:1.7;}
.pro-tip{border-left:3px solid var(--coral-m);background:var(--coral-l);padding:10px 14px;border-radius:0 var(--radius) var(--radius) 0;font-size:13px;color:var(--coral);margin:10px 0;line-height:1.7;}
.pro-tip::before{content:'⚡ PRO TIP ';font-weight:700;letter-spacing:0.03em;}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;}
@media(max-width:700px){.grid2,.grid3{grid-template-columns:1fr;}.app{grid-template-columns:1fr;}.sidebar{position:relative;height:auto;}.main{padding:20px;}}
.editor-wrap{margin:12px 0;}
.editor-bar{display:flex;justify-content:space-between;align-items:center;padding:6px 10px;background:var(--surface-2);border:0.5px solid var(--border);border-bottom:none;border-radius:var(--radius) var(--radius) 0 0;font-size:11px;color:var(--text-2);}
.editor{width:100%;min-height:140px;padding:12px 14px;border:0.5px solid var(--border);border-top:none;border-radius:0 0 var(--radius) var(--radius);background:var(--surface);font-family:var(--mono);font-size:13px;color:var(--text);line-height:1.7;resize:vertical;outline:none;tab-size:4;}
.editor:focus{border-color:var(--purple-m);box-shadow:0 0 0 2px rgba(127,119,221,0.15);}
.btn-row{display:flex;gap:8px;margin-top:10px;align-items:center;flex-wrap:wrap;}
.btn{padding:7px 16px;border-radius:var(--radius);font-size:13px;cursor:pointer;font-weight:500;border:none;font-family:inherit;transition:all 0.15s;}
.btn-primary{background:var(--purple);color:#fff;}
.btn-primary:hover{background:#2a2466;}
.btn-ghost{background:transparent;color:var(--text-2);border:0.5px solid var(--border);}
.btn-ghost:hover{background:var(--surface-2);color:var(--text);}
.output{margin-top:10px;padding:12px 14px;border-radius:var(--radius);font-family:var(--mono);font-size:12.5px;min-height:40px;line-height:1.7;white-space:pre-wrap;border:0.5px solid var(--border);}
.out-ok{background:var(--teal-l);color:var(--teal);border-color:var(--teal-m);}
.out-err{background:var(--red-l);color:var(--red);border-color:var(--red-m);}
.out-empty{background:var(--surface-2);color:var(--text-3);}
.tbl{width:100%;border-collapse:collapse;font-size:13px;margin:10px 0;border-radius:var(--radius);overflow:hidden;border:0.5px solid var(--border);}
.tbl th{text-align:left;padding:10px 12px;background:var(--surface-2);font-weight:600;color:var(--text);font-size:12px;border-bottom:0.5px solid var(--border);}
.tbl td{padding:9px 12px;border-top:0.5px solid var(--border);}
.tbl td.c{font-family:var(--mono);font-size:12px;color:var(--text);}
.tbl tr:hover{background:var(--surface-2);}
.mem-viz{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0;padding:14px;background:var(--surface-2);border-radius:var(--radius);}
.mem-cell{background:var(--surface);border:1.5px solid var(--purple-m);border-radius:var(--radius);padding:8px 12px;min-width:80px;text-align:center;}
.mem-label{font-size:10px;color:var(--text-3);margin-bottom:3px;text-transform:uppercase;letter-spacing:0.05em;}
.mem-val{font-family:var(--mono);font-size:13px;font-weight:600;color:var(--purple);}
.mem-type{font-size:10px;color:var(--text-3);margin-top:2px;}
.ex-card{background:var(--surface);border:0.5px solid var(--border);border-radius:var(--radius-lg);padding:18px 22px;margin-bottom:16px;position:relative;}
.ex-head{display:flex;justify-content:space-between;align-items:start;gap:12px;margin-bottom:10px;flex-wrap:wrap;}
.ex-title{font-size:14px;font-weight:600;color:var(--text);}
.ex-tag{font-size:10px;padding:3px 8px;border-radius:5px;font-weight:600;letter-spacing:0.03em;text-transform:uppercase;}
.ex-easy{background:var(--green-l);color:var(--green);}
.ex-med{background:var(--amber-l);color:var(--amber);}
.ex-hard{background:var(--red-l);color:var(--red);}
.ex-biz{background:var(--purple-l);color:var(--purple);}
.ex-desc{font-size:13px;color:var(--text-2);margin-bottom:10px;line-height:1.7;}
.hint-btn{font-size:12px;color:var(--purple);cursor:pointer;background:none;border:none;padding:0;text-decoration:underline;font-family:inherit;}
.hint{display:none;margin-top:8px;padding:9px 12px;font-size:12.5px;color:var(--purple);background:var(--purple-l);border-radius:var(--radius);line-height:1.7;}
.hint.show{display:block;}
.solution-btn{font-size:12px;color:var(--teal);cursor:pointer;background:none;border:none;padding:0;text-decoration:underline;font-family:inherit;margin-left:14px;}
.sol{display:none;margin-top:8px;padding:10px 12px;font-size:12.5px;color:var(--teal);background:var(--teal-l);border-radius:var(--radius);}
.sol.show{display:block;}
.sol pre{font-family:var(--mono);font-size:12px;white-space:pre-wrap;margin-top:4px;line-height:1.6;}
.nav-controls{display:flex;justify-content:space-between;align-items:center;padding:20px;margin-top:30px;border-top:0.5px solid var(--border);}
.shortcut{font-family:var(--mono);font-size:11px;background:var(--surface-2);color:var(--text-2);padding:2px 6px;border-radius:4px;border:0.5px solid var(--border);}
.concept-row{display:flex;gap:10px;align-items:start;padding:12px;background:var(--surface-2);border-radius:var(--radius);margin:8px 0;}
.concept-num{background:var(--purple);color:#fff;width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0;}
.concept-text{font-size:13px;color:var(--text-2);line-height:1.7;}
.flashcard{background:var(--surface);border:0.5px solid var(--border);border-radius:var(--radius-lg);padding:14px 18px;margin:8px 0;cursor:pointer;transition:all 0.15s;}
.flashcard:hover{border-color:var(--purple-m);}
.flashcard-q{font-size:13px;font-weight:600;color:var(--text);margin-bottom:6px;}
.flashcard-a{display:none;font-size:12.5px;color:var(--text-2);padding-top:8px;margin-top:8px;border-top:0.5px solid var(--border);line-height:1.7;}
.flashcard.open .flashcard-a{display:block;}
.flashcard-toggle{font-size:11px;color:var(--purple);font-weight:500;}
.stats-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:16px 0;}
.stat-card{background:var(--surface-2);border-radius:var(--radius);padding:12px 14px;}
.stat-label{font-size:11px;color:var(--text-2);margin-bottom:4px;text-transform:uppercase;letter-spacing:0.05em;}
.stat-val{font-size:22px;font-weight:600;color:var(--text);}
.stat-sub{font-size:11px;color:var(--text-3);margin-top:2px;}
.toc{background:var(--surface-2);border-radius:var(--radius);padding:14px 18px;margin-bottom:20px;}
.toc-title{font-size:12px;font-weight:600;color:var(--text-2);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:8px;}
.toc-list{list-style:none;}
.toc-list li{padding:4px 0;font-size:13px;color:var(--text-2);}
.toc-list li::before{content:'→ ';color:var(--purple-m);}
.kb{display:inline-flex;gap:4px;align-items:center;}
.key{font-family:var(--mono);font-size:11px;padding:2px 7px;background:var(--surface);border:0.5px solid var(--border);border-bottom:1.5px solid var(--border-2);border-radius:4px;color:var(--text);}
.sidebar-toggle{display:none;position:fixed;top:10px;left:10px;z-index:100;background:var(--surface);border:0.5px solid var(--border);border-radius:var(--radius);padding:6px 10px;font-size:18px;cursor:pointer;}
@media(max-width:700px){.sidebar-toggle{display:block;}.sidebar{position:fixed;z-index:50;width:260px;transform:translateX(-100%);transition:transform 0.3s;}.sidebar.open{transform:none;}}
</style>
</head>
<body>
<button class="sidebar-toggle" onclick="document.getElementById('sb').classList.toggle('open')">☰</button>
<div class="app">
<aside class="sidebar" id="sb">
  <div class="sidebar-header">
    <div class="logo">La Bibbia di Python</div>
    <div class="logo-sub">Dal principiante al Business Analyst</div>
    <div class="progress-global">
      <div class="progress-label"><span>Progresso totale</span><span id="pg-pct">0%</span></div>
      <div class="progress-bar-wrap"><div class="progress-bar" id="pg-bar" style="width:0%"></div></div>
      <div class="progress-label" style="margin-top:4px;"><span id="pg-count">0 / 46 lezioni</span></div>
    </div>
  </div>
  <nav class="phase-list" id="nav"></nav>
  <div style="padding:14px 10px;margin-top:10px;border-top:0.5px solid var(--border);font-size:11px;color:var(--text-3);line-height:1.6;">
    <div style="margin-bottom:6px;font-weight:600;color:var(--text-2);">Scorciatoie</div>
    <div><span class="shortcut">Ctrl+↵</span> Esegui codice</div>
    <div><span class="shortcut">↑ ↓</span> Naviga lezioni</div>
    <div><span class="shortcut">Ctrl+K</span> Reset sezione</div>
  </div>
</aside>
</main>
<main class="main" id="main">
  <h1 style="font-size:22px;margin-bottom:10px;color:var(--text);">La Bibbia di Python</h1>
  <p style="color:var(--text-2);">Se vedi questo testo, il server risponde correttamente. Se la pagina rimane vuota, controlla la console del browser e il log del server.</p>
</main>
</div>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(html)


if __name__ == '__main__':
  # Bind to all interfaces and use an explicit port so it's reachable
  # disable the automatic reloader which sets signal handlers
  # that may not be supported in some execution environments
  print('Starting Flask on http://0.0.0.0:5000')
  app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
