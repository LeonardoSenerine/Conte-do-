"""Story pra divulgar o site da Scarpetta, com espaço pra figurinha de link. 1080x1920."""

CSS = r'''
:root { --verde:#0f3d2c; --noite:#0a2b1f; --creme:#efe5c8; --papel:#f6f0df; --manj:#a9c99a; --ink:#1e1d1e; --blue:#0a63b2; --sky:#7cbcf2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1920px; overflow:hidden; font-family:"Inter Tight",sans-serif; }
.s > * { position:absolute; }
.verde { background:var(--verde); color:var(--creme); }
.noite { background:var(--noite); color:var(--creme); }
.papel { background:var(--papel); color:var(--noite); }
.preto { background:var(--ink); color:#f2efea; }
.h { left:72px; right:72px; font-weight:800; line-height:.92; letter-spacing:-.06em; z-index:3; }
.h i { font-family:"Fraunces",serif; font-weight:400; font-style:italic; letter-spacing:-.03em; font-size:1.06em; }
.verde .h i, .noite .h i { color:var(--manj); }
.papel .h i { color:var(--verde); }
.preto .h i { font-family:"Instrument Serif",serif; color:var(--sky); font-size:1.12em; }
.h .sc { font-family:"Pinyon Script",cursive; font-weight:400; letter-spacing:0; font-size:1.25em; line-height:.7; }
.sm { left:72px; bottom:72px; width:860px; font-size:26px; font-weight:600; line-height:1.25; letter-spacing:-.01em; text-transform:uppercase; z-index:3; }
.arrow { right:72px; bottom:66px; font-size:56px; line-height:1; z-index:3; }
.rot { left:72px; top:80px; font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.08em; text-transform:uppercase; opacity:.7; z-index:3; }
.ui { z-index:3; }
.phone { border-radius:54px; padding:12px; background:#0b0b0b; z-index:2; outline:2px solid rgba(239,229,200,.14); }
.phone .sc2 { border-radius:42px; overflow:hidden; height:100%; background:#fff; }
.phone .sc2 img { display:block; width:100%; }
.shot { border-radius:6px; overflow:hidden; z-index:2; }
.shot img { display:block; width:100%; }
.pill { height:84px; border-radius:999px; background:#fff; color:#1e1d1e; display:inline-grid; place-items:center; padding:0 48px; font-family:-apple-system,"Inter Tight",sans-serif; font-size:32px; font-weight:500; }
.img { z-index:1; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:screen; filter:invert(1); opacity:.07;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.papel .grain { mix-blend-mode:multiply; filter:none; opacity:.14; }
'''

T = "../../elementos/tinta/"
C = "../../elementos/clientes/scarpetta/"
S = f"""<section class="s noite" id="s1">
  <img src="{T}videira-claro.png" style="left:420px;top:-120px;width:900px;opacity:.16">
  <p class="rot" style="top:250px">senerine.dev · site novo no ar</p>
  <h1 class="h" style="top:320px;font-size:130px">o site da<br><span class="sc" style="font-size:1.6em">Scarpetta</span><br><i>está no ar.</i></h1>
  <div class="phone" style="left:260px;top:720px;width:560px;height:660px;rotate:-3deg"><div class="sc2"><img src="{C}site.webp"></div></div>
  <p style="left:72px;top:1420px;width:936px;text-align:center;font-family:'Fraunces',serif;font-style:italic;font-size:44px;color:var(--manj);z-index:3">cardápio, reserva e o salão, num link só</p>
  <div style="left:190px;top:1500px;width:700px;height:150px;z-index:3">
    <i style="position:absolute;left:0;top:0;width:44px;height:44px;border-left:5px solid var(--creme);border-top:5px solid var(--creme)"></i>
    <i style="position:absolute;right:0;top:0;width:44px;height:44px;border-right:5px solid var(--creme);border-top:5px solid var(--creme)"></i>
    <i style="position:absolute;left:0;bottom:0;width:44px;height:44px;border-left:5px solid var(--creme);border-bottom:5px solid var(--creme)"></i>
    <i style="position:absolute;right:0;bottom:0;width:44px;height:44px;border-right:5px solid var(--creme);border-bottom:5px solid var(--creme)"></i>
    <p style="position:absolute;inset:0;display:grid;place-items:center;font-family:'JetBrains Mono',monospace;font-size:22px;letter-spacing:.08em;text-transform:uppercase;opacity:.6">link aqui</p>
  </div>
  <div class="grain"></div>
</section>"""
open("scarpetta-link.html", "w").write(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head><body>{S}</body></html>""")
