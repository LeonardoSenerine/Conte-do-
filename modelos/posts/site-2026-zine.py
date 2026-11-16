"""Carrossel "ainda vale a pena ter um site em 2026?", no zine clássico (a versão anti design ficou
"bem ruim"): papel, Anton + Bodoni, imagens em tinta que ele mandou, o ponto azul e notas com linha.
Sem cabeçalho nem rodapé. 8 slides 1080x1440. Gerar: python3 site-2026-zine.py && node ../render.mjs site-2026-zine.html saida 1080 1440 8"""

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
.note { border-top:2px solid currentColor; padding-top:14px; z-index:5; }
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
.s { --bg:var(--paper); --pt:var(--blue); }
.s.azul { --bg:var(--blue); --pt:var(--off); background:var(--blue); color:var(--off); }
.s.azul .h .b, .s.azul .it .b { color:var(--ink); mix-blend-mode:normal; }
.s.azul .dot { background:var(--off); mix-blend-mode:normal; }
.s.preto { --bg:var(--ink); --pt:#4aa3ea; background:var(--ink); color:var(--off); }
.s.preto .h .b, .s.preto .it .b { color:#4aa3ea; mix-blend-mode:normal; }
.s.preto .dot { mix-blend-mode:normal; }
.s.preto .img { filter:invert(1); mix-blend-mode:screen; }
.s.azul .grain, .s.preto .grain { mix-blend-mode:screen; opacity:.14;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.cel { z-index:4; border:10px solid var(--ink); border-radius:46px; overflow:hidden; background:var(--ink); }
.cel img { display:block; width:100%; }
.tape { height:46px; background:rgba(236,232,220,.78); box-shadow:0 1px 2px rgba(0,0,0,.12); z-index:8; }
'''

T = "../../elementos/tinta/"



import math

TINTA, OFF, AZUL, CLARO = "#121112", "#f2efea", "#0a63b2", "#4aa3ea"


def _r(d, cor, w):
    return f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def oval(cx, cy, rx, ry, cor, rot=-4, w=7):
    """Círculo à mão: uma volta e um pouco, que não fecha certinho."""
    pts = []
    for k in range(70):
        t = -0.4 + k / 68 * (2 * math.pi + 0.7)
        r = 1 + 0.035 * math.sin(3 * t) + 0.04 * k / 68
        x, y = rx * r * math.cos(t), ry * r * math.sin(t)
        a = math.radians(rot)
        pts.append((cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)))
    return _r("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts), cor, w)


def sublinha(x1, x2, y, cor, w=9):
    """Sublinhado à mão: passa um pouco do fim e volta."""
    return _r(f"M {x1} {y+4} Q {(x1+x2)/2:.0f} {y-10} {x2} {y+2} Q {x2-60} {y+12} {x2-160} {y+16}", cor, w)


def seta(x1, y1, x2, y2, cor, w=6, curva=-70):
    mx, my = (x1 + x2) / 2 + curva, (y1 + y2) / 2 - abs(curva) / 2
    ang = math.atan2(y2 - my, x2 - mx)
    h1 = (x2 - 30 * math.cos(ang - .5), y2 - 30 * math.sin(ang - .5))
    h2 = (x2 - 30 * math.cos(ang + .5), y2 - 30 * math.sin(ang + .5))
    return _r(f"M {x1} {y1} Q {mx:.0f} {my:.0f} {x2} {y2} M {h1[0]:.0f} {h1[1]:.0f} L {x2} {y2} L {h2[0]:.0f} {h2[1]:.0f}", cor, w)


def rabisco(*partes):
    return f'<svg class="ln" width="1080" height="1440" style="z-index:6">{"".join(partes)}</svg>'


def mao(x, y, txt, cor, rot=-4, size=46):
    """Anotação à mão em serifa itálica."""
    return (f'<p style="left:{x}px;top:{y}px;font-family:\'Instrument Serif\',serif;font-style:italic;'
            f'font-size:{size}px;line-height:1.05;color:{cor};rotate:{rot}deg;z-index:7">{txt}</p>')


def fita(x, y, rot, w=170):
    return f'<div class="tape" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg"></div>'


def carimbo(x, y, txt, cor, rot=-10):
    return (f'<p style="left:{x}px;top:{y}px;border:5px solid {cor};color:{cor};padding:10px 20px 8px;'
            f'font-family:\'JetBrains Mono\',monospace;font-weight:800;font-size:28px;letter-spacing:.14em;'
            f'text-transform:uppercase;rotate:{rot}deg;z-index:8">{txt}</p>')


EXTRA = {
    1: rabisco(oval(307, 627, 280, 112, OFF, -5)) + mao(64, 790, "spoiler<br>no fim →", OFF, -6, 50) + fita(780, 92, -7, 150),
    2: rabisco(sublinha(64, 680, 712, AZUL)) + mao(620, 740, "logo, “quem somos”<br>e um telefone. só.", AZUL, 5, 40)
       + rabisco(seta(700, 850, 650, 950, AZUL, 5, 40)),
    3: rabisco(sublinha(330, 690, 470, CLARO)) + mao(720, 330, "e o cliente<br>cai fora", CLARO, 6, 48)
       + rabisco(seta(820, 450, 760, 600, CLARO, 5, 50)),
    4: rabisco(oval(290, 520, 260, 98, AZUL, -3)) + fita(745, 300, -8, 150) + fita(930, 1020, 14, 120)
       + carimbo(860, 236, "no ar", AZUL, 10) + mao(64, 1010, "um toque e ele<br>tá no seu WhatsApp", AZUL, -4, 40),
    5: rabisco(sublinha(64, 900, 540, TINTA)) + mao(720, 610, "aberta de madrugada,<br>no feriado, no domingo", OFF, -4, 40),
    6: rabisco(oval(380, 610, 110, 88, CLARO, 6)) + mao(540, 575, "e ela te indica?", CLARO, -5, 54)
       + rabisco(seta(560, 660, 480, 720, CLARO, 5, -40)),
    7: rabisco(sublinha(64, 960, 545, TINTA, 10))
       + '<img class="img" src="' + T + 'estrelas.png" style="left:672px;top:430px;height:420px;rotate:90deg;transform-origin:50% 50%;z-index:2">'
       + mao(700, 700, "e o que dizem<br>de você também", AZUL, 4, 38),
    8: rabisco(sublinha(340, 930, 455, TINTA)) + mao(64, 520, "um estúdio de<br>uma pessoa só.", OFF, -4, 50)
       + '<img class="img" src="' + T + 'flores-tinta.png" style="left:820px;top:-60px;height:520px;rotate:12deg">',
}


def slide(n, inner, cls=""):
    return f'''<section class="s {cls}" id="s{n}">
  {inner}
  {EXTRA.get(n, "")}
  <div class="grain"></div>
</section>'''


def nota(x, y, w, ax, ay, texto, ponto=True):
    """Texto solto no papel sobre um fio; uma linha fina liga a ponta do fio ao detalhe da imagem
    (ax, ay), onde fica um ponto azul. ponto=False quando a linha já encosta num ponto do slide."""
    jx = x + w if ax > x + w / 2 else x
    ln = f'<line x1="{ax}" y1="{ay}" x2="{jx}" y2="{y}"'
    dot = f'<circle cx="{ax}" cy="{ay}" r="11" style="fill:var(--pt);stroke:var(--bg)" stroke-width="4"/>' if ponto else ""
    return (f'<p class="tx note" style="left:{x}px;top:{y}px;width:{w}px">{texto}</p>'
            f'<svg class="ln" width="1080" height="1440">{ln} style="stroke:var(--bg)" stroke-width="8" stroke-linecap="round"/>'
            f'{ln} stroke="currentColor" stroke-width="2"/>{dot}</svg>')

N1 = nota(64, 1110, 400, 760, 900, 'Resposta curta: vale. Mas não do jeito que todo mundo fazia. Arrasta.', ponto=False)
N2 = nota(64, 1110, 952, 620, 1020, 'Site era item de lista: ter pra dizer que tinha. Uma página com logo, “quem somos” e um telefone. Ninguém pensava em quem ia entrar, nem no que essa pessoa queria fazer ali.')
N3 = nota(64, 1070, 952, 640, 880, 'Abre devagar no celular. Não mostra o preço. Esconde o WhatsApp lá embaixo. Não diz o que faz logo de cara. A pessoa não acha o que veio buscar e volta pro Google.<br><b style="color:var(--pt)">O site existe, mas não trabalha.</b>')
N4 = nota(64, 1130, 952, 905, 958, 'Vitrine mostra e espera alguém entrar. Um site feito pro seu cliente tira a dúvida antes da pergunta e leva ao próximo passo. É o que eu fiz no senerine.dev: logo na primeira tela, você sabe o que eu faço, vê quem faz e chama no WhatsApp com um toque.')
N5 = nota(64, 1190, 952, 192, 796, 'Todo mundo passa por ela: pesquisando, comparando, perguntando. O perfil é uma banca na calçada, com as regras de outro. O site é o seu endereço: seu domínio, do seu jeito, aberto de madrugada.')
N6 = nota(64, 700, 400, 800, 960, 'Ele pergunta pro ChatGPT, pro Claude: “onde tem uma barbearia boa aqui perto?”. A IA responde com o que encontra escrito na internet. Se o que você faz, onde fica e quanto custa só existe no stories e no direct, fica difícil ela te achar.')
N7 = nota(64, 640, 420, 842, 866, 'Aparecer, hoje, é:<br><br>01 ser achado quando alguém pesquisa;<br>02 estar escrito de um jeito que o Google e a IA conseguem ler;<br>03 convencer em segundos quem chega.')
N8 = nota(64, 1180, 900, 873, 1000, 'Senerine.dev é um estúdio digital autoral. Faço sites e aplicações pensados pra serem encontrados, entendidos e usados pelo seu cliente. Me chama no direct.<br><br><b style="color:var(--pt)">Manda pra quem acha que site já era.</b>', ponto=False)

S = []

# 1 · capa: os lírios na faixa preta, bonitos e de pé; o ponto atrás
S.append(slide(1, f'''
  <div class="dot" style="left:650px;top:520px;width:300px;height:300px"></div>
  <img class="img" src="{T}lirios-faixa.png" style="left:520px;top:100px;height:1300px">
  <p class="it" style="left:64px;top:120px;font-size:72px">Ainda vale a pena<br>ter um</p>
  <h1 class="h" style="left:64px;top:300px;font-size:200px">site em<br><span class="b">2026?</span></h1>
  {N1}''', cls="azul"))

# 2 · antigamente, por fazer: "focus" borrado, sem foco em quem ia entrar
S.append(slide(2, f'''
  <p class="it" style="left:64px;top:120px;font-size:72px">Antigamente,</p>
  <h1 class="h" style="left:64px;top:220px;font-size:150px">todo mundo<br>fazia site<br><span class="b">por fazer.</span></h1>
  <div class="dot" style="left:560px;top:930px;width:130px;height:130px"></div>
  <img class="img" src="{T}foco.png" style="left:420px;top:760px;width:620px">
  {N2}'''))

# 3 · hoje sobra site ruim: o homem caindo, o cliente cai fora
S.append(slide(3, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:160px">Hoje, sobra<br>site <span class="b">ruim.</span></h1>
  <div class="dot" style="left:520px;top:600px;width:380px;height:380px"></div>
  <img class="img" src="{T}queda.png" style="left:260px;top:360px;width:960px">
  {N3}''', cls="preto"))

# 4 · vitrine só mostra, site único capta: os cisnes se encontrando, o ponto no coração
S.append(slide(4, f'''
  <p class="it" style="left:64px;top:120px;font-size:72px">Vitrine só mostra.</p>
  <h1 class="h" style="left:64px;top:230px;font-size:150px">Site único<br><span class="b">capta.</span></h1>
  <img class="img" src="{T}cisnes.png" style="left:-40px;top:520px;width:640px">
  <div class="dot" style="left:247px;top:812px;width:76px;height:76px;z-index:3"></div>
  <div class="cel" style="left:650px;top:330px;width:350px;height:720px;rotate:4deg"><img src="../../elementos/senerine/m-hero.png"></div>
  {N4}'''))

# 5 · a rua mais movimentada: o cavalo galopando
S.append(slide(5, f'''
  <p class="it" style="left:64px;top:120px;font-size:72px">A internet é a</p>
  <h1 class="h" style="left:64px;top:220px;font-size:150px">rua mais<br><span class="b">movimentada.</span></h1>
  <div class="dot" style="left:430px;top:780px;width:260px;height:260px"></div>
  <img class="img" src="{T}cavalo.png" style="left:150px;top:520px;width:780px">
  {N5}''', cls="azul"))

# 6 · o cliente pergunta pra IA: as andorinhas, uma descendo até a outra
S.append(slide(6, f'''
  <p class="it" style="left:64px;top:120px;font-size:64px">Seu cliente não pesquisa<br>só no Google.</p>
  <h1 class="h" style="left:64px;top:320px;font-size:150px">Ele pergunta<br>pra <span class="b">IA.</span></h1>
  <div class="dot" style="left:640px;top:1000px;width:240px;height:240px"></div>
  <img class="img" src="{T}andorinhas.png" style="left:470px;top:620px;width:600px">
  {N6}''', cls="preto"))

# 7 · aparecer: a câmera (sem a marca), o ponto atrás da lente
S.append(slide(7, f'''
  <p class="it" style="left:64px;top:120px;font-size:72px">Não basta existir.<br>Você precisa</p>
  <h1 class="h" style="left:64px;top:300px;font-size:230px"><span class="b">aparecer.</span></h1>
  <div class="dot" style="left:560px;top:1115px;width:200px;height:200px"></div>
  <img class="img" src="{T}camera.png" style="left:500px;top:820px;width:560px">
  {N7}'''))

# 8 · esse é o meu trabalho: no meio dos leões, a figura parada; o ponto atrás dela
S.append(slide(8, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:150px">Esse é o<br>meu <span class="b">trabalho.</span></h1>
  <div class="dot" style="left:763px;top:784px;width:220px;height:220px"></div>
  <img class="img" src="{T}leoes.png" style="left:0;top:-60px;width:1080px">
  {N8}''', cls="azul"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>'''
open("site-2026-zine.html", "w").write(html)
