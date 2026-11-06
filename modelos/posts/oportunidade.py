"""Carrossel "a oportunidade está mais perto do que você imagina" (zine): por que falar do
próprio trabalho. Imagens que nunca entraram em post, capa testada em 3 versões, ponte pro site com o caso real do Gordinho.
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
.shot { overflow:hidden; z-index:2; }
.shot img { display:block; }
.cal { z-index:3; font-family:"JetBrains Mono",monospace; font-size:24px; text-transform:uppercase; }
.cal > div { display:flex; gap:28px; margin-bottom:26px; }
.cal .d span { width:100px; text-align:center; }
.cal i { width:100px; height:100px; border-radius:50%; border:3px solid var(--ink); display:block; }
.cal i.on { background:var(--blue); border-color:var(--blue); mix-blend-mode:multiply; }
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

U = "../../elementos/senerine/"

N1 = nota(64, 1040, 300, 630, 930, 'Ele já está por perto: te segue, passa na sua porta, ouviu seu nome de alguém. Só não sabe ainda o que você faz.')
N2 = nota(64, 960, 380, 700, 900, 'Enquanto você faz bem feito e fica quieto, quem fala mais alto fica com o cliente.')
N3 = nota(64, 900, 300, 846, 981, 'Mostra o antes e o depois, o bastidor, o detalhe que só você vê. Não é se exibir: é deixar quem está perto te encontrar.', ponto=False)
N4 = nota(64, 1100, 520, 712, 1150, 'Quem viu o seu trabalho uma vez lembra de você quando precisar. E quem te indica tem o que mostrar.', ponto=False)
N5 = nota(64, 1050, 620, 560, 960, 'Gordinho Lanches: 34 anos de história que só existiam num mural na parede. Hoje tem linha do tempo desde 1992, horário do dia e pedido pelo WhatsApp e iFood.')
N6 = nota(64, 1130, 560, 242, 1093, 'Constância vale mais que volume. Pouco e sempre já mostra que você está ali.', ponto=False)
N7 = nota(64, 1010, 560, 762, 1170, 'E se esse alguém é você: faço sites e aplicações que mostram o seu trabalho do jeito que ele é. Me chama no direct.', ponto=False)

DIAS = "".join(f'<span>{d}</span>' for d in ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"])
SEMANAS = "".join('<div>' + "".join(f'<i class="{"on" if d == 1 else ""}"></i>' for d in range(7)) + '</div>' for _ in range(4))

S = []

# 1 · capa: a coruja olhando de cima; o cliente já está de olho
S.append(slide(1, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:150px;line-height:1.22">Seu próximo<br>cliente já<br>te <span class="b">segue.</span></h1>
  <div class="crop" style="left:380px;top:700px;width:700px;height:740px"><img src="{T}coruja.png" style="left:0;top:-20px;width:760px"></div>
  {N1}'''))

# 2 · o homem de terno com a mão na boca: trabalha bem e fica calado
S.append(slide(2, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:120px;line-height:1.22">Você trabalha<br>bem. Só que<br>ninguém <span class="b">sabe.</span></h1>
  <div class="crop" style="left:480px;top:600px;width:600px;height:840px"><img src="{T}vilao.png" style="left:-130px;top:-93px;height:1300px"></div>
  {N2}'''))

# 3 · a explosão de tinta saindo do ponto: fala do seu trabalho (falar não é gritar)
S.append(slide(3, f'''
  <div class="crop" style="left:380px;top:520px;width:700px;height:920px"><img src="{T}explosao.png" style="left:0;top:0;width:700px"></div>
  <div class="dot" style="left:846px;top:901px;width:160px;height:160px;z-index:3"></div>
  <h1 class="h" style="left:64px;top:128px;font-size:140px">Fala do seu<br><span class="b">trabalho.</span></h1>
  <p class="it" style="left:64px;top:452px;font-size:64px">Falar não é gritar.</p>
  {N3}'''))

# 4 · só tipografia: o ponto é o que fica na memória
S.append(slide(4, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:220px">Quem vê,<br><span class="b">lembra.</span></h1>
  <p class="it" style="left:64px;top:640px;font-size:110px">Quem lembra,<br>chama.</p>
  <div class="dot" style="left:710px;top:1000px;width:300px;height:300px"></div>
  {N4}'''))

# 5 · a ponte pro site, com prova real: a história do Gordinho que só existia na parede
S.append(slide(5, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:120px;line-height:1.22">E quando ele<br>vem te ver,<br>acha <span class="b">o quê?</span></h1>
  <p class="mono" style="left:64px;top:610px;z-index:3">cliente real · no ar</p>
  <div class="shot" style="left:64px;top:650px;width:952px;height:317px"><img src="{U}gordinho-desde-1992.jpg" style="width:952px"></div>
  {N5}'''))

# 6 · ser justo, só tipografia: um ponto por semana já é constância
S.append(slide(6, f'''
  <p class="it" style="left:64px;top:140px;font-size:84px">Não precisa</p>
  <h1 class="h" style="left:64px;top:240px;font-size:128px">postar <span class="b">todo dia.</span></h1>
  <div class="cal" style="left:64px;top:560px"><div class="d">{DIAS}</div>{SEMANAS}</div>
  {N6}'''))

# 7 · chamada grande: manda pra alguém
S.append(slide(7, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:150px">Manda pra<br>quem trabalha<br>bem e fala<br><span class="b">pouco.</span></h1>
  <div class="dot" style="left:760px;top:1050px;width:240px;height:240px"></div>
  {N7}''', nxt="salva pra depois"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>'''
open("oportunidade.html", "w").write(html)
