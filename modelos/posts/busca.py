"""Carrossel "você não precisa de um site, precisa que te achem" (zine nº 05): busca, perfil no Google
e informação igual em todo lugar. Só imagens do banco. Textos de busca tirados do FAQ do site, sem prometer posição.
8 slides 1080x1440. Gerar: python3 busca.py && node ../render.mjs busca.html saida 1080 1440 8"""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; --off:#f2efea; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; background:var(--paper); color:var(--ink); font-family:"Inter Tight",sans-serif; }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.04em; text-transform:uppercase; }
.top { left:64px; right:64px; top:56px; display:flex; justify-content:space-between; padding-bottom:16px; border-bottom:3px solid var(--ink); z-index:7; }
.bot { left:64px; right:64px; top:1352px; display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:3px solid var(--ink); z-index:7; }
.bot b { font-weight:700; }
.h { font-family:"Anton",sans-serif; font-weight:400; text-transform:uppercase; line-height:1.08; letter-spacing:-.005em; z-index:3; }
.h .b { color:var(--blue); mix-blend-mode:multiply; }
.it { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; letter-spacing:-.02em; line-height:1; z-index:3; }
.it .b { color:var(--blue); mix-blend-mode:multiply; }
.lab { background:var(--ink); color:var(--paper); padding:.06em .22em .02em; display:inline-block; }
.dot { border-radius:50%; background:var(--blue); mix-blend-mode:multiply; }
.img { mix-blend-mode:multiply; z-index:2; }
.tx { font-family:"JetBrains Mono",monospace; font-size:27px; line-height:1.45; letter-spacing:-.01em; z-index:3; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.2;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.note { border-top:2px solid var(--ink); padding-top:14px; z-index:5; }
.ln { left:0; top:0; z-index:5; pointer-events:none; }
.stamp { border:4px solid var(--blue); color:var(--blue); padding:10px 18px; font-family:"JetBrains Mono",monospace; font-weight:700; font-size:24px; letter-spacing:.1em; text-transform:uppercase; mix-blend-mode:multiply; z-index:6; }
s { text-decoration:none; position:relative; }
s::after { content:""; position:absolute; left:-4%; right:-4%; top:52%; height:.16em; background:var(--blue); mix-blend-mode:multiply; rotate:-3deg; }
.list { left:64px; right:64px; z-index:3; }
.list div { display:flex; align-items:baseline; gap:28px; padding:20px 0 18px; border-top:3px solid var(--ink); }
.list div:last-child { border-bottom:3px solid var(--ink); }
.list .n { font-family:"Anton",sans-serif; font-size:64px; line-height:1; color:var(--blue); mix-blend-mode:multiply; width:84px; }
.list .t { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; font-size:54px; line-height:1.05; letter-spacing:-.02em; }
.list .t small { display:block; font-family:"JetBrains Mono",monospace; font-style:normal; font-weight:400; font-size:24px; letter-spacing:0; margin-top:8px; }
.crop { overflow:hidden; mix-blend-mode:multiply; z-index:2; }
.crop img { position:absolute; }
.s.fundo .top span, .s.fundo .bot span { background:var(--paper); padding:2px 8px; margin:0 -8px; }
.s.fundo .note { text-shadow:0 0 4px var(--paper), 0 0 8px var(--paper), 0 0 14px var(--paper), 0 0 20px var(--paper); }
.list.c .t { font-size:44px; }
'''

T = "../../elementos/tinta/"


def slide(n, inner, nxt="vira a página →", cls=""):
    return f'''<section class="s {cls}" id="s{n}">
  {inner}
  <div class="grain"></div>
</section>'''


def nota(x, y, w, ax, ay, texto, ponto=True):
    """Texto solto no papel sobre um fio; uma linha fina liga a ponta do fio ao detalhe da imagem
    (ax, ay), onde fica um ponto azul. ponto=False quando a linha já encosta num ponto do slide."""
    jx = x + w if ax > x + w / 2 else x
    ln = f'<line x1="{ax}" y1="{ay}" x2="{jx}" y2="{y}"'
    dot = f'<circle cx="{ax}" cy="{ay}" r="11" fill="#0a63b2" stroke="#e8e6e0" stroke-width="4"/>' if ponto else ""
    return (f'<p class="tx note" style="left:{x}px;top:{y}px;width:{w}px">{texto}</p>'
            f'<svg class="ln" width="1080" height="1440">{ln} stroke="#e8e6e0" stroke-width="8" stroke-linecap="round"/>'
            f'{ln} stroke="#121112" stroke-width="2"/>{dot}</svg>')


S = []

# 1 · capa: todo mundo olhando pro mesmo ponto; a lua do eclipse é o ponto azul
S.append(slide(1, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:150px">Você não<br>precisa de<br>um site.</h1>
  <p class="it" style="left:64px;top:600px;font-size:76px">Precisa que <span class="b">te achem.</span></p>
  <img class="img" src="{T}eclipse.png" style="left:300px;top:700px;width:640px">
  <div class="dot" style="left:569px;top:893px;width:110px;height:110px"></div>
  {nota(64, 760, 250, 624, 948, 'Por que aparecer na busca vale mais que um site bonito.', ponto=False)}"""))

# 2 · Washington apontando pra baixo: ele procura antes de chamar
S.append(slide(2, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:140px">Antes de<br>te chamar,<br>ele <span class="b">procura.</span></h1>
  <img class="img" src="{T}washington.png" style="left:40px;top:540px;width:1000px">
  {nota(64, 1250, 700, 585, 1145, 'Nome do negócio, “perto de mim”, o que você vende. Quem não aparece nessa busca nem entra na conversa.')}"""))

# 3 · a domadora no meio dos leões: a concorrência está na mesma busca
S.append(slide(3, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:120px">No meio da<br><span class="b">concorrência,</span></h1>
  <p class="it" style="left:64px;top:370px;width:900px;font-size:60px">quem é fácil de achar sai na frente.</p>
  <img class="img" src="{T}leoes.png" style="left:0;top:-60px;width:1080px">
  {nota(64, 1180, 620, 895, 760, 'Na mesma busca aparecem os seus concorrentes. Quem mostra logo o que faz, onde fica e como chamar leva a vez.')}"""))

# 4 · pássaros borrados: o site bonito que a busca não enxerga
S.append(slide(4, f"""
  <img class="img fundo" src="{T}passaros-borrados.png" style="left:560px;top:420px;height:1440px">
  <h1 class="h" style="left:64px;top:96px;font-size:130px">Site bonito<br>que o Google<br><span class="b">não lê.</span></h1>
  {nota(64, 1000, 440, 860, 1120, 'Texto dentro de imagem, página sem título, endereço escondido. Pra quem passa é bonito. Pra busca, é uma página vazia.')}""", cls="fundo"))

# 5 · estrelas: o perfil da empresa no Google
S.append(slide(5, f"""
  <img class="img" src="{T}estrelas.png" style="left:600px;top:80px;height:1300px">
  <h1 class="h" style="left:64px;top:96px;font-size:116px">O Google<br>também olha<br>o seu <span class="b">perfil.</span></h1>
  {nota(64, 760, 560, 850, 640, 'Endereço, horário, fotos e avaliações no perfil da empresa no Google. O que está ali pesa na hora de alguém escolher.')}"""))

# 6 · cisnes: site, Google e Instagram dizendo a mesma coisa
S.append(slide(6, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:150px">Tudo igual<br>em todo<br><span class="b">lugar.</span></h1>
  <img class="img" src="{T}cisnes.png" style="left:40px;top:420px;width:1000px">
  {nota(64, 1200, 700, 539, 855, 'Mesmo nome, telefone e horário no site, no Google e no Instagram. Informação que bate passa confiança.')}"""))

# 7 · ser justo: ninguém garante o primeiro lugar
S.append(slide(7, f"""
  <p class="it" style="left:64px;top:110px;font-size:84px">Ninguém garante</p>
  <h1 class="h" style="left:64px;top:214px;font-size:150px">o primeiro<br><span class="b">lugar.</span></h1>
  <img class="img" src="{T}borboletas.png" style="left:300px;top:480px;width:760px">
  {nota(64, 1220, 800, 640, 800, 'Quem promete o topo do Google está chutando. O que dá pra fazer é deixar o site pronto pra ser encontrado: endereço, horário e páginas que o Google consegue ler.')}"""))

# 8 · chamada: o eclipse de novo, só o sol com o ponto
S.append(slide(8, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:160px">Quer que<br>te <span class="b">achem?</span></h1>
  <img class="img" src="{T}eclipse-sol.png" style="left:160px;top:560px;width:760px">
  <div class="dot" style="left:479px;top:789px;width:130px;height:130px"></div>
  {nota(64, 1200, 700, 544, 854, 'Faço sites e aplicações que já saem prontos pra busca. Me chama no direct.', ponto=False)}"""))

html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>"""
open("busca.html", "w").write(html)
