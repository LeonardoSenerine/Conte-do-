"""Stories "sumi" (aviso de pausa): 3 stories 1080x1920 no zine, um fundo diferente em cada (azul, papel, preto),
sem figurinha. Só imagens do banco. Gerar: python3 sumido.py && node ../render.mjs sumido.html saida 1080 1920 3"""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1920px; overflow:hidden; background:var(--paper); color:var(--ink); }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:24px; letter-spacing:.06em; text-transform:uppercase; }
.anton { font-family:"Anton",sans-serif; text-transform:uppercase; line-height:1; }
.bod { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; line-height:.95; letter-spacing:-.03em; }
.ins { font-family:"Instrument Serif",serif; line-height:1.05; letter-spacing:-.015em; }
.ins i { font-style:italic; }
.img { mix-blend-mode:multiply; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.26;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.grain.lt { mix-blend-mode:screen; opacity:.16; filter:invert(1); }
'''
T = "../../elementos/tinta/"
S = []

# 1 · azul: "sumi." e o terno sem cabeça saindo de cena
S.append(f'''<section class="s" id="s1" style="background:var(--blue);color:var(--paper)">
  <p class="anton" style="left:60px;top:250px;font-size:420px">Sumi.</p>
  <p class="bod" style="left:72px;top:690px;font-size:150px;color:var(--ink)">eu sei.</p>
  <p class="ins" style="left:72px;top:900px;width:460px;font-size:58px;z-index:3">Muita coisa mudou na rotina nas últimas semanas, e o perfil ficou <i>mais quieto do que eu queria.</i></p>
  <img class="img" src="{T}terno.png" style="left:380px;top:760px;height:1200px">
  <div class="grain"></div>
</section>''')

# 2 · papel: "mas não parei.", as pombas saindo da estátua
S.append(f'''<section class="s" id="s2">
  <img class="img" src="{T}mulher-pombas.png" style="left:180px;top:760px;width:1000px">
  <p class="anton" style="left:60px;top:250px;font-size:250px">Mas não<br><span style="color:var(--blue);mix-blend-mode:multiply">parei.</span></p>
  <p class="ins" style="left:72px;top:800px;width:440px;font-size:60px;z-index:3">Tem projeto novo vindo por aí. <i>Alguns eu ainda não posso mostrar.</i></p>
  <div class="grain"></div>
</section>''')

# 3 · preto: o sol do eclipse com o ponto azul no lugar da lua
S.append(f'''<section class="s" id="s3" style="background:#111011;color:var(--paper)">
  <img src="{T}eclipse-sol-claro.png" style="left:110px;top:560px;width:860px">
  <div style="left:470px;top:820px;width:150px;height:150px;border-radius:50%;background:var(--blue);box-shadow:0 0 60px rgba(74,163,234,.6)"></div>
  <p class="mono" style="left:72px;top:250px;color:#7cbcf2">senerine.dev ● fica de olho</p>
  <p class="anton" style="left:60px;top:1260px;font-size:230px">Em breve.</p>
  <p class="bod" style="left:72px;top:1500px;font-size:96px;font-weight:700">volto com <span style="color:#4aa3ea">novidade.</span></p>
  <div class="grain lt"></div>
</section>''')

open("sumido.html", "w").write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>''')
