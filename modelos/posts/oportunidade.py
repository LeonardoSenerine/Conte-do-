"""Carrossel "a oportunidade está mais perto do que você imagina" (zine): por que falar do
próprio trabalho. Mesmo sistema do "modelo pronto", só com imagens que nunca entraram em post (pedido dele).
7 slides 1080x1440, sem cabeçalho nem rodapé. Gerar: python3 oportunidade.py && node ../render.mjs oportunidade.html saida 1080 1440 7"""

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

N2 = nota(64, 900, 320, 630, 560, 'Quem precisa do que você faz já está por perto: te segue, passa na sua porta, ouviu seu nome de alguém.')
N3 = nota(64, 1000, 400, 491, 624, 'Enquanto você faz bem feito e fica quieto, quem fala mais alto fica com o cliente.')
N4 = nota(64, 900, 300, 846, 981, 'Mostra o antes e o depois, o bastidor, o detalhe que só você vê. Não é se exibir: é deixar quem está perto te encontrar.', ponto=False)
N5 = nota(64, 1000, 400, 724, 1162, 'Quem viu o seu trabalho uma vez lembra de você quando precisar. E quem te indica tem o que mostrar.')
N6 = nota(64, 1040, 340, 520, 1000, 'Constância vale mais que volume. Pouco e sempre já mostra que você está ali.')
N7 = nota(64, 1010, 360, 545, 880, 'Faço sites e aplicações que mostram o seu trabalho do jeito que ele é. Me chama no direct.<br><br><b style="color:var(--blue)">Manda pra alguém que trabalha bem e fala pouco.</b>', ponto=False)

S = []

# 1 · capa: as pombas voando em volta dela; a oportunidade já está do lado
S.append(slide(1, f'''
  <div class="crop" style="left:200px;top:560px;width:880px;height:880px"><img src="{T}mulher-pombas.png" style="left:0;top:-70px;width:880px"></div>
  <div class="dot" style="left:560px;top:810px;width:90px;height:90px;z-index:3"></div>
  <p class="it" style="left:64px;top:140px;font-size:84px">A oportunidade está</p>
  <h1 class="h" style="left:64px;top:240px;font-size:196px"><span class="b">mais perto</span></h1>
  <p class="it" style="left:64px;top:470px;font-size:84px">do que você imagina.</p>'''))

# 2 · a coruja olhando: quem precisa de você já está olhando
S.append(slide(2, f'''
  <div class="crop" style="left:380px;top:330px;width:700px;height:1110px"><img src="{T}coruja.png" style="left:0;top:-20px;width:760px"></div>
  <h1 class="h" style="left:64px;top:128px;font-size:140px">Ela já está<br>te <span class="b">olhando.</span></h1>
  {N2}'''))

# 3 · os gansos saindo da faixa: trabalho bom calado passa batido
S.append(slide(3, f'''
  <img class="img" src="{T}gansos-faixa.png" style="left:285px;top:0;height:1440px">
  <h1 class="h" style="left:64px;top:128px;font-size:120px">Trabalho bom<br>calado passa<br><span class="b">batido.</span></h1>
  {N3}'''))

# 4 · a explosão de tinta saindo do ponto: fala do seu trabalho (falar não é gritar)
S.append(slide(4, f'''
  <div class="crop" style="left:380px;top:520px;width:700px;height:920px"><img src="{T}explosao.png" style="left:0;top:0;width:700px"></div>
  <div class="dot" style="left:846px;top:901px;width:160px;height:160px;z-index:3"></div>
  <h1 class="h" style="left:64px;top:128px;font-size:140px">Fala do seu<br><span class="b">trabalho.</span></h1>
  <p class="it" style="left:64px;top:452px;font-size:64px">Falar não é gritar.</p>
  {N4}'''))

# 5 · as andorinhas (que sempre voltam): quem vê lembra, quem lembra chama
S.append(slide(5, f'''
  <img class="img" src="{T}andorinhas-faixa.png" style="left:285px;top:0;height:1440px">
  <h1 class="h" style="left:64px;top:128px;font-size:150px">Quem vê,<br><span class="b">lembra.</span></h1>
  <p class="it" style="left:64px;top:470px;font-size:64px">Quem lembra, chama.</p>
  {N5}'''))

# 6 · a íris: ser justo, não precisa postar todo dia
S.append(slide(6, f'''
  <div class="dot" style="left:600px;top:640px;width:230px;height:230px"></div>
  <div class="crop" style="left:260px;top:470px;width:820px;height:970px"><img src="{T}iris.png" style="left:0;top:0;width:820px"></div>
  <p class="it" style="left:64px;top:140px;font-size:84px">Não precisa</p>
  <h1 class="h" style="left:64px;top:240px;font-size:128px">postar <span class="b">todo dia.</span></h1>
  {N6}'''))

# 7 · chamada: o pégaso diante do ponto azul, como um sol
S.append(slide(7, f'''
  <div class="dot" style="left:540px;top:620px;width:420px;height:420px"></div>
  <img class="img" src="{T}pegaso.png" style="left:160px;top:300px;width:1100px">
  <h1 class="h" style="left:64px;top:128px;font-size:130px">Seu trabalho<br>merece ser<br><span class="b">visto.</span></h1>
  {N7}''', nxt="salva pra depois"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>'''
open("oportunidade.html", "w").write(html)
