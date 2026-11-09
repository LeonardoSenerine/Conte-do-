"""Carrossel do case Scarpetta Cucina: o link da bio saiu do Linktree e virou site. Linguagem editorial na "sala"
do cliente (verde garrafa, creme, Fraunces e a assinatura em Pinyon Script), capturas reais do site, rabiscos à mão.
Textos tirados da página de proposta do repositório Scarpetta. A cidade foi apagada da captura do Linktree.
9 slides 1080x1440. Gerar: python3 scarpetta.py && node ../render.mjs scarpetta.html saida 1080 1440 9"""

CSS = r'''
:root { --verde:#0f3d2c; --noite:#0a2b1f; --creme:#efe5c8; --papel:#f6f0df; --manj:#a9c99a; --ink:#1e1d1e; --blue:#0a63b2; --sky:#7cbcf2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; font-family:"Inter Tight",sans-serif; }
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


def slide(n, cor, inner, sm="", arrow=True, rot="senerine.dev · case scarpetta"):
    r = f'<p class="rot">{rot}</p>' if rot else ""
    pe = f'<p class="sm">{sm}</p>' if sm else ""
    ar = '<p class="arrow">→</p>' if arrow else ""
    return f'<section class="s {cor}" id="s{n}">{r}{inner}{pe}{ar}<div class="grain"></div></section>'


def phone(src, x, y, w, h, rot=0, extra=""):
    return f'<div class="phone" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;rotate:{rot}deg;{extra}"><div class="sc2"><img src="{C}{src}"></div></div>'

import math
U = "../../elementos/senerine/"


def risco(d, cor="#0a63b2", w=7):
    """Traço à mão em SVG, nas coordenadas do slide."""
    return f'<svg class="ui" style="left:0;top:0;z-index:5;pointer-events:none" width="1080" height="1440"><path d="{d}" fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def oval(cx, cy, rx, ry, rot=-4, cor="#1e1d1e", w=6):
    """Círculo feito à mão: uma volta e um pouco, que não fecha certinho."""
    pts = []
    for k in range(66):
        t = -0.4 + k / 64 * (2 * math.pi + 0.7)
        r = 1 + 0.035 * math.sin(3 * t) + 0.03 * k / 64
        x, y = rx * r * math.cos(t), ry * r * math.sin(t)
        a = math.radians(rot)
        pts.append((cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)))
    return risco("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts), cor, w)


def seta(x1, y1, x2, y2, cor="#0a63b2", w=6, curva=-80):
    mx, my = (x1 + x2) / 2 + curva, (y1 + y2) / 2 - abs(curva) / 2
    ang = math.atan2(y2 - my, x2 - mx)
    h1 = (x2 - 34 * math.cos(ang - .5), y2 - 34 * math.sin(ang - .5))
    h2 = (x2 - 34 * math.cos(ang + .5), y2 - 34 * math.sin(ang + .5))
    return risco(f"M {x1} {y1} Q {mx:.0f} {my:.0f} {x2} {y2} M {h1[0]:.0f} {h1[1]:.0f} L {x2} {y2} L {h2[0]:.0f} {h2[1]:.0f}", cor, w)


def xis(x, y, s, cor="#0a63b2", w=10):
    return risco(f"M {x} {y} Q {x+s*.55:.0f} {y+s*.45:.0f} {x+s} {y+s*1.02:.0f} M {x+s*1.04:.0f} {y-4} Q {x+s*.4:.0f} {y+s*.5:.0f} {x-6} {y+s*.98:.0f}", cor, w)


def nota_mao(x, y, txt, cor="var(--sky)", rot=-4, size=40):
    return f'<p class="ui" style="left:{x}px;top:{y}px;font-family:\'Instrument Serif\',serif;font-style:italic;font-size:{size}px;line-height:1;color:{cor};rotate:{rot}deg;z-index:6">{txt}</p>'



MANJ, CREME, VERDE = "#a9c99a", "#efe5c8", "#0f3d2c"


def troca(n, cor, botoes, titulo, img, texto, alto=True):
    risc = MANJ if cor != "papel" else VERDE
    pills = "".join(f'<span class="ui pill" style="left:72px;top:{560 + i*110}px;rotate:{-3 + i*2}deg">{b}</span>' for i, b in enumerate(botoes))
    strikes = "".join(risco(f"M 60 {602 + i*110} Q 220 {590 + i*110} {130 + len(b)*19} {600 + i*110}", risc, 7) for i, b in enumerate(botoes))
    nota = nota_mao(80, 560 + len(botoes) * 110 + 30, "no linktree", "var(--manj)" if cor != "papel" else VERDE, -5, 44)
    arte = phone(img, 640, 540, 380, 740, 3) if alto else f'<div class="shot" style="left:470px;top:800px;width:540px;rotate:3deg"><img src="{C}{img}"></div>'
    return slide(n, cor, f'<h1 class="h" style="top:150px;font-size:150px">{titulo}</h1>{pills}{strikes}{nota}'
                 + seta(330, 560 + len(botoes) * 110 + 90, 540, 900, risc, 6, curva=-60) + arte, texto)


S = [
    # 1 · capa: o linktree cinza atrás, o site na frente
    slide(1, "noite", f'<img class="img" src="{T}videira-claro.png" style="left:560px;top:-160px;width:700px;opacity:.16">'
          + '<h1 class="h" style="top:170px;font-size:150px">o link da bio<br>da <span class="sc">Scarpetta</span><br><i>virou casa.</i></h1>'
          + phone("linktree-sem-cidade.png", 90, 700, 330, 620, -8, "filter:grayscale(1) brightness(.85)")
          + phone("site.webp", 560, 640, 400, 750, 4)
          + seta(330, 690, 600, 760, MANJ, 6, curva=-40)
          + nota_mao(250, 600, "antes → depois", "var(--manj)", -6, 44), "", True),
    # 2 · antes: o linktree, com as anotações
    slide(2, "papel", '<h1 class="h" style="top:170px;font-size:170px">antes:<br><i>um linktree.</i></h1>'
          + phone("linktree-sem-cidade.png", 560, 520, 420, 800, 3)
          + nota_mao(72, 620, "fundo cinza, igual<br>a qualquer perfil", VERDE, -4, 44)
          + nota_mao(72, 820, "nenhum prato,<br>nenhuma foto", VERDE, -3, 44)
          + nota_mao(72, 1020, "cada botão leva<br>pra outro lugar", VERDE, -5, 44)
          + seta(390, 650, 600, 700, VERDE, 5, curva=-30) + seta(360, 1050, 620, 980, VERDE, 5, curva=40),
          "o mesmo link da bio. quem ainda estava<br>decidindo onde comer não tinha motivo pra escolher."),
    # 3 · depois: o site com a cara da casa
    slide(3, "verde", '<h1 class="h" style="top:170px;font-size:170px">depois:<br><i>a cara<br>da casa.</i></h1>'
          + phone("site.webp", 560, 520, 420, 800, -3)
          + nota_mao(72, 820, "verde garrafa<br>e creme", "var(--manj)", -4, 46)
          + nota_mao(72, 990, "o tomate do logo", "var(--manj)", -3, 46)
          + nota_mao(72, 1110, "e a assinatura<br>manuscrita", "var(--manj)", -5, 46)
          + seta(380, 1150, 640, 700, MANJ, 5, curva=-60),
          "e nenhum botão do linktree se perdeu."),
    troca(4, "papel", ["Reservas"], "a reserva<br><i>chega pronta.</i>", "reserva.webp",
          "o cliente escolhe dia, horário e pessoas, e o<br>whatsapp da casa recebe a mensagem completa."),
    troca(5, "verde", ["Menu"], "o cardápio<br><i>com foto e preço.</i>", "cardapio.webp",
          "pratos com foto, descrição e preço,<br>separados por categoria."),
    troca(6, "papel", ["Peça pelo Ifood", "Peça pelo nosso delivery"], "pedidos<br><i>num lugar só.</i>", "delivery.webp",
          "o ifood e o delivery próprio,<br>lado a lado, com as mesmas massas e pizzas.", alto=False),
    troca(7, "verde", ["Eventos e confraternizações"], "eventos<br><i>com orçamento.</i>", "eventos.webp",
          "as ocasiões, como o menu é servido<br>e o pedido de orçamento direto."),
    # 8 · o que o linktree nunca mostrou
    slide(8, "noite", '<h1 class="h" style="top:170px;font-size:150px">e o que o<br>linktree<br><i>nunca mostrou.</i></h1>'
          + phone("executivo.webp", 110, 700, 340, 560, -4) + phone("salao.webp", 620, 680, 340, 560, 4)
          + nota_mao(110, 630, "o menu da semana", "var(--manj)", -5, 40)
          + nota_mao(600, 616, "o salão no meio da mata", "var(--manj)", 4, 40),
          "antes do primeiro contato, quem chega já vê<br>o prato, o preço e o lugar."),
    # 9 · chamada, de volta às cores da senerine
    slide(9, "preto", '<div style="left:72px;top:170px;width:120px;height:120px;border-radius:50%;background:var(--blue)"></div>'
          + f'<img class="img" src="{T}andorinhas-claro.png" style="left:660px;top:120px;height:560px">'
          + '<h1 class="h" style="top:600px;font-size:140px">o seu link<br>da bio também<br>pode <i>virar casa.</i></h1>',
          "me chama no direct.<br>quem responde sou eu.", False, rot="senerine.dev"),
]

open("scarpetta.html", "w").write(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>""")
