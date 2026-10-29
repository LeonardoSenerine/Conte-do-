"""4 stories da série zine (link na bio), 1080x1920. Cada um quebra o padrão de um jeito:
fundo azul, papel, preto e papel de novo, misturando Anton, Bodoni Moda, Instrument Serif e mono.
As áreas com cantoneiras ficam livres pras figurinhas (post, enquete, quiz, caixinha)."""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1920px; overflow:hidden; background:var(--paper); color:var(--ink); }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:24px; letter-spacing:.06em; text-transform:uppercase; }
.anton { font-family:"Anton",sans-serif; text-transform:uppercase; line-height:.86; }
.bod { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; line-height:.8; letter-spacing:-.04em; }
.ins { font-family:"Instrument Serif",serif; line-height:.95; letter-spacing:-.02em; }
.ins i { font-style:italic; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.28;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.grain.lt { mix-blend-mode:screen; opacity:.18; filter:invert(1); }
.st { z-index:6; }
.st i { position:absolute; width:46px; height:46px; border:0 solid currentColor; }
.st i:nth-child(1) { left:0; top:0; border-left-width:5px; border-top-width:5px; }
.st i:nth-child(2) { right:0; top:0; border-right-width:5px; border-top-width:5px; }
.st i:nth-child(3) { left:0; bottom:0; border-left-width:5px; border-bottom-width:5px; }
.st i:nth-child(4) { right:0; bottom:0; border-right-width:5px; border-bottom-width:5px; }
.st p { position:absolute; inset:0; display:grid; place-items:center; }
'''


def sticker(x, y, w, h, label, color):
    return f'<div class="st" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;color:{color}"><i></i><i></i><i></i><i></i><p class="mono" style="font-size:22px;opacity:.7">{label}</p></div>'


S = []

# 1 · post novo: fundo azul, pétala preta saindo da borda, "novo" em Bodoni gigante
S.append(f'''<section class="s" id="s1" style="background:var(--blue);color:var(--paper)">
  <img src="../../elementos/tinta/petala.png" style="left:-40px;top:250px;height:1560px">
  <p class="mono" style="left:72px;top:250px;z-index:3">senerine.dev ● zine nº 01</p>
  <p class="anton" style="right:-38px;top:250px;font-size:330px;writing-mode:vertical-rl;color:var(--ink);z-index:2">Post</p>
  <p class="bod" style="left:40px;top:690px;font-size:430px;z-index:3">novo</p>
  <p class="ins" style="left:76px;top:1080px;width:700px;font-size:76px;z-index:3">no feed, sobre o <i>link</i><br>da sua bio.</p>
  {sticker(140, 1360, 800, 250, "post aqui ↓", "#e8e6e0")}
  <div class="grain"></div>
</section>''')

# 2 · enquete: o eclipse vira o ponto azul; todo mundo olhando pro mesmo lugar
S.append(f'''<section class="s" id="s2">
  <img src="../../elementos/tinta/eclipse.png" style="left:-8px;top:346px;width:1096px">
  <div style="left:466px;top:670px;width:170px;height:170px;border-radius:50%;background:var(--blue);z-index:2"></div>
  <p class="ins" style="left:72px;top:250px;width:936px;font-size:118px;z-index:3">Todo mundo olha<br>pro <i>mesmo lugar:</i></p>
  <p class="anton" style="left:72px;top:1120px;font-size:200px;z-index:3">a sua <span style="color:var(--blue)">bio.</span></p>
  {sticker(140, 1440, 800, 230, "", "#e8e6e0")}
  <p class="mono" style="left:72px;right:72px;top:1720px;text-align:center;color:var(--paper);z-index:4">o link dela leva pra onde?</p>
  <div class="grain"></div>
</section>''')

# 3 · quiz no fundo preto: o mundo em papel, os dois endereços em fontes que brigam
S.append(f'''<section class="s" id="s3" style="background:#111011;color:var(--paper)">
  <img src="../../elementos/tinta/mundo-claro.png" style="left:150px;top:560px;width:780px;opacity:.9">
  <p class="mono" style="left:72px;top:250px;color:#7cbcf2">quiz ● responde aí</p>
  <p class="bod" style="left:66px;top:310px;font-size:136px;font-weight:600">Qual passa<br>mais <span style="color:#4aa3ea">confiança?</span></p>
  <div style="left:0;right:0;top:1290px;z-index:3">
    <p style="margin-left:72px;font-family:'JetBrains Mono',monospace;font-size:68px;letter-spacing:-.02em;background:var(--paper);color:var(--ink);display:inline-block;padding:6px 18px"><b style="color:var(--blue)">A</b> linktr.ee/seunegocio</p><br>
    <p class="anton" style="margin:26px 0 0 72px;font-size:106px;background:var(--blue);color:#fff;display:inline-block;padding:14px 22px 6px"><span style="font-family:'JetBrains Mono';font-size:68px;vertical-align:.6em;margin-right:16px">B</span>seunegocio.com.br</p>
  </div>
  {sticker(240, 1640, 600, 130, "quiz aqui", "#e8e6e0")}
  <div class="grain lt"></div>
</section>''')

# 4 · caixinha: avaliação sem dó, o cão latindo de baixo pra cima
S.append(f'''<section class="s" id="s4">
  <img src="../../elementos/tinta/cao.png" style="left:0;top:0;width:1080px">
  <p class="mono" style="left:72px;top:250px">avaliação de link na bio</p>
  <p class="anton" style="left:60px;top:300px;font-size:390px;line-height:1">Sem</p>
  <p class="anton" style="left:60px;top:650px;font-size:390px;line-height:1">dó<span style="color:var(--blue)">.</span></p>
  <p class="ins" style="left:600px;top:760px;width:420px;font-size:62px"><i>Manda o link</i> da sua bio que eu digo o que eu mudaria.</p>
  {sticker(140, 1090, 800, 200, "caixinha aqui", "#121112")}
  <div class="grain"></div>
</section>''')

open("stories.html", "w").write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>''')
