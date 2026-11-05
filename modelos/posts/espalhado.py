"""Carrossel "você precisa de um site." (editorial, v2): o negócio espalhado (forms, linktree, pdf, direct),
com pedaços de interface em cada dor, e prova social com os 4 clientes reais (textos dos estudos de caso do site).
12 slides 1080x1440, bem estilizado: colagem de interfaces, rabiscos à mão, carimbo "no ar" e antes/depois nas provas. Gerar: python3 espalhado.py && node ../render.mjs espalhado.html saida 1080 1440 12"""

CSS = r'''
:root { --cream:#f2efea; --ink:#1e1d1e; --blue:#0a63b2; --sky:#7cbcf2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; font-family:"Inter Tight",sans-serif; }
.s > * { position:absolute; }
.cream { background:var(--cream); color:var(--ink); }
.black { background:var(--ink); color:var(--cream); }
.blue { background:var(--blue); color:var(--cream); }
.h { left:72px; right:72px; font-weight:800; line-height:.9; letter-spacing:-.06em; z-index:3; }
.h i { font-family:"Instrument Serif",serif; font-weight:400; font-style:italic; letter-spacing:-.025em; font-size:1.12em; line-height:.8; }
.cream .h i { color:var(--blue); }
.black .h i { color:var(--sky); }
.blue .h i { color:var(--ink); }
.sm { left:72px; font-size:26px; font-weight:600; line-height:1.25; letter-spacing:-.01em; text-transform:uppercase; z-index:3; }
.arrow { right:72px; font-size:56px; font-weight:400; line-height:1; z-index:3; }
.img { z-index:2; }
.tag { left:72px; top:110px; display:flex; align-items:center; gap:14px; font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.08em; text-transform:uppercase; z-index:4; }
.tag i { display:none; }

.shot { border-radius:6px; overflow:hidden; z-index:2;  }
.shot img { display:block; width:100%; }
.phone { border-radius:56px; padding:12px; background:#121112; z-index:2; outline:2px solid rgba(242,239,234,.14); }
.phone .sc { border-radius:44px; overflow:hidden; height:100%; }
.phone .sc img { display:block; width:100%; }
.ui { z-index:3; font-family:"Inter Tight",sans-serif; }
.card { background:#fff; color:#3a3838; border-radius:6px; padding:34px 36px;  }
.card .lb { font-size:20px; color:#8a8783; margin:18px 0 8px; }
.card .in { height:44px; border-bottom:2px solid #d8d5cf; }
.btn { display:inline-block; margin-top:26px; background:#5b5958; color:#fff; font-weight:600; font-size:22px; padding:14px 26px; border-radius:10px; }
.pill { width:600px; height:76px; border-radius:999px; background:#fff; color:#5b5958; display:grid; place-items:center; font-size:28px; font-weight:500;  }
.file { display:flex; align-items:center; gap:18px; background:#fff; color:#3a3838; border-radius:4px; padding:18px 24px; font-family:"JetBrains Mono",monospace; font-size:24px;  }
.file b { background:#5b5958; color:#fff; font-size:18px; padding:8px 10px; border-radius:6px; }
.bub { background:#f2efea; color:#1e1d1e; border-radius:28px 28px 28px 8px; padding:20px 28px; font-size:32px; font-weight:500; display:inline-flex; gap:18px; align-items:baseline; }
.stamp { border:5px solid currentColor; padding:10px 20px 8px; font-family:"JetBrains Mono",monospace; font-weight:800; font-size:30px; letter-spacing:.14em; text-transform:uppercase; z-index:6; border-radius:6px; }
.antes { left:72px; font-size:24px; font-weight:600; letter-spacing:-.01em; text-transform:uppercase; opacity:.55; z-index:3; }
.antes s { text-decoration:line-through; text-decoration-thickness:3px; }
.chk { display:inline-flex; align-items:center; gap:16px; background:#fff; color:#1e1d1e; border-radius:999px; padding:16px 28px 16px 18px; font-size:32px; font-weight:600; letter-spacing:-.02em;  }
.chk i { width:40px; height:40px; border-radius:50%; background:var(--blue); color:#fff; display:grid; place-items:center; font-style:normal; font-size:24px; }
.bub small { font-family:"JetBrains Mono",monospace; font-size:18px; opacity:.55; }

.cream .img { mix-blend-mode:multiply; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.12;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.black .grain, .blue .grain { mix-blend-mode:screen; filter:invert(1); opacity:.08; }
'''
T = "../../elementos/tinta/"


def slide(n, cor, inner, sm="", arrow=True):
    pe = f'<p class="sm" style="bottom:72px;width:860px">{sm}</p>' if sm else ""
    ar = '<p class="arrow" style="bottom:66px">→</p>' if arrow else ""
    return f'<section class="s {cor}" id="s{n}">{inner}{pe}{ar}<div class="grain"></div></section>'


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


def FORM(x, y, w, rot, extra=""):
    return (f'<div class="ui card" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg;{extra}">'
            '<p style="font-size:34px;font-weight:700;color:#1e1d1e">Agende seu horário</p>'
            '<p class="lb">Nome</p><div class="in"></div><p class="lb">Telefone</p><div class="in"></div>'
            '<p class="lb">Dia e horário que prefere</p><div class="in"></div><span class="btn">Enviar</span></div>')


def PILL(x, y, t, rot, w=600):
    return f'<div class="ui pill" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg">{t}</div>'


def PDF(x, y, rot):
    return f'<div class="ui file" style="left:{x}px;top:{y}px;rotate:{rot}deg"><b>PDF</b>cardapio_FINAL_v3_agora_vai.pdf</div>'


def BUB(x, y, t, h, rot=0):
    return f'<span class="ui bub" style="left:{x}px;top:{y}px;rotate:{rot}deg">{t} <small>{h}</small></span>'


def prova(n, cor, cliente, titulo, antes, depois, arte, carimbo):
    return slide(n, cor, f'<p class="tag"><i></i>{cliente}</p>{titulo}{arte}{carimbo}'
                 f'<p class="antes" style="bottom:150px"><s>antes: {antes}</s></p>', depois)


S = [
    # 1 · capa: o título no meio e o negócio espalhado em volta, como colagem
    slide(1, "cream", FORM(640, 70, 520, 8, "transform:scale(.62);transform-origin:top left")
          + BUB(80, 170, "qual o preço?", "09:12", -6).replace('rotate:-6deg', 'rotate:-6deg;background:#fff')
          + PILL(560, 1040, "Cardápio", -7, 420) + PILL(600, 1130, "WhatsApp", -3, 420)
          + PDF(70, 1080, 5)
          + '<h1 class="h" style="top:390px;font-size:210px">você<br><i>precisa</i> de<br>um site.</h1>'
          + oval(350, 688, 352, 124, -3),
          "porque hoje o seu negócio<br>está espalhado."),
    # 2 · agenda no forms: o formulário riscado e o cliente esperando
    slide(2, "black", '<h1 class="h" style="top:110px;font-size:200px">agenda<br>no <i>forms.</i></h1>'
          + FORM(150, 600, 780, -3) + xis(470, 760, 170)
          + f'<img class="img" src="{T}pressa-claro.png" style="left:50px;top:930px;width:380px;z-index:4">'
          + nota_mao(520, 1190, "…e o cliente indo embora.", rot=-5, size=44),
          "o cliente preenche e fica esperando<br>você conferir, confirmar e responder."),
    # 3 · links no linktree: a lista igual, com o nome deles riscado
    slide(3, "blue", '<h1 class="h" style="top:110px;font-size:200px">links no<br><i>linktree.</i></h1>'
          + "".join(PILL(110 + i * 14, 600 + i * 104, t, -4 + i * 2, 540) for i, t in enumerate(["Cardápio", "WhatsApp", "Instagram", "Localização"]))
          + f'<img class="img" src="{T}tvs.png" style="left:700px;top:780px;height:430px">' + '<p class="ui" style="left:110px;top:1040px;font-family:\'JetBrains Mono\',monospace;font-size:30px">linktr.ee/seunegocio</p>'
          + risco("M 102 1062 Q 200 1052 295 1060", "#f2efea", 7)
          + nota_mao(330, 1100, "o nome que aparece<br>é o deles", "#f2efea", -3, 42),
          "uma lista igual à de todo mundo, com o<br>nome de outra empresa no endereço."),
    # 4 · cardápio em pdf: o homem do jornal tentando ler
    slide(4, "cream", f'<img class="img" src="{T}fim.png" style="left:220px;top:380px;width:820px">'
          + PDF(110, 1070, -4) + seta(300, 1050, 540, 880, curva=-110)
          + nota_mao(72, 900, "ninguém lê<br>no celular", "var(--blue)", -6, 46)
          + '<h1 class="h" style="top:110px;font-size:200px">cardápio<br>em <i>pdf.</i></h1>',
          "abre pequeno no celular, ninguém lê<br>direito e o google não acha."),
    # 5 · preço só no direct: a mesma pergunta o dia todo, circulada
    slide(5, "black", '<h1 class="h" style="top:110px;font-size:190px">preço<br>só no<br><i>direct.</i></h1>'
          + BUB(80, 760, "qual o preço?", "09:12") + BUB(140, 860, "oi, quanto custa?", "13:40")
          + BUB(80, 960, "tem valor?", "18:05") + BUB(170, 1060, "preço?", "21:57")
          + oval(330, 950, 330, 230, 4, "#7cbcf2", 5) + f'<img class="img" src="{T}megafone-claro.png" style="left:640px;top:560px;width:520px">'
          + nota_mao(420, 1180, "de novo.", rot=-8, size=64),
          "a mesma pergunta respondida<br>o dia inteiro, por você."),
    # 6 · tudo espalhado: os pedaços voando junto com os pássaros
    slide(6, "blue", f'<img class="img" src="{T}passaros-borrados.png" style="left:460px;top:-80px;height:1600px">'
          + FORM(580, 640, 520, 14, "transform:scale(.55);transform-origin:top left")
          + PILL(520, 1030, "Localização", -12, 380) + PDF(80, 900, 8) + BUB(660, 1150, "preço?", "21:57", 6)
          + '<h1 class="h" style="top:110px;font-size:170px">tudo<br>espalhado.<br><i>nada<br>é seu.</i></h1>',
          "cada ferramenta com uma cara,<br>um login e uma regra diferente."),
    # 7 · um site junta tudo: os mesmos pedaços, agora em ordem
    slide(7, "cream", f'<img class="img" src="{T}cisnes.png" style="left:500px;top:40px;width:520px">'
          + '<h1 class="h" style="top:470px;font-size:170px">um site<br><i>junta tudo.</i></h1>'
          + '<p class="ui" style="left:72px;top:860px;width:936px;font-size:64px;font-weight:800;letter-spacing:-.05em;line-height:1.05">agenda, cardápio, preço, links, contato <i style="font-family:Instrument Serif;font-weight:400;color:var(--blue);font-size:1.15em">e a sua cara.</i></p>'
          + risco("M 80 940 Q 300 930 520 944", "#0a63b2", 6),
          "e não é teoria. olha quem já juntou →"),
    prova(8, "black", "doce&sabor", '<h1 class="h" style="top:170px;font-size:120px">três serviços<br>espalhados,<br><i>uma página só.</i></h1>',
          "tudo combinado na conversa", "marmitas, personal chef e feijoada. cada serviço<br>com o seu botão e a mensagem já escrita.",
          f'<img class="img" src="{T}lirios-ramo-claro.png" style="left:30px;top:620px;height:640px;opacity:.9">' f'<div class="phone" style="left:330px;top:540px;width:420px;height:660px;rotate:-3deg"><div class="sc"><img src="{U}docesabor-celular.jpg"></div></div>',
          '<div class="stamp" style="left:740px;top:620px;color:var(--sky);rotate:9deg">no ar</div>'),
    prova(9, "cream", "cantina pôr do sol", '<h1 class="h" style="top:170px;font-size:130px">a reserva<br><i>já chega<br>pronta.</i></h1>',
          "toda reserva fechada no whatsapp", "o painel monta a mensagem pro whatsapp e conhece<br>as regras da casa: rodízio só de quinta a sábado.",
          f'<img class="img" src="{T}eclipse-sol.png" style="left:30px;top:500px;width:560px">' f'<div class="shot" style="left:340px;top:560px;width:640px;rotate:3deg"><img src="{U}cantina-reserva.jpg"></div>',
          '<div class="stamp" style="left:120px;top:860px;color:var(--blue);rotate:-8deg">no ar</div>'),
    prova(10, "black", "d’conde barbearia", '<h1 class="h" style="top:170px;font-size:124px">a agenda <i>saiu<br>do whatsapp.</i></h1>',
          "agenda combinada à mão no whatsapp", "o cliente marca em 4 passos, vê só os<br>horários livres e recebe lembrete 3 horas antes.",
          f'<div class="shot" style="left:72px;top:520px;width:936px;rotate:-1.5deg"><img src="{U}dconde-agenda.jpg"></div>',
          '<div class="stamp" style="left:820px;top:480px;color:var(--sky);rotate:8deg">no ar</div>'),
    prova(11, "blue", "gordinho lanches", '<h1 class="h" style="top:170px;font-size:124px">34 anos de<br>história que<br><i>ninguém achava.</i></h1>',
          "quem procurava achava pouca coisa", "agora tem linha do tempo desde 1992,<br>horário do dia e pedido pelo whatsapp e ifood.",
          f'<div class="shot" style="left:400px;top:560px;width:540px;rotate:3deg"><img src="{U}gordinho-hamburguer.jpg"></div>' f'<img class="img" src="{T}menino.png" style="left:20px;top:820px;height:460px;z-index:3">',
          '<div class="stamp" style="left:120px;top:640px;color:var(--cream);rotate:-9deg">no ar</div>'),
    slide(12, "black", '<div style="left:72px;top:150px;width:120px;height:120px;border-radius:50%;background:var(--blue)"></div>'
          + f'<img class="img" src="{T}andorinhas-claro.png" style="left:640px;top:90px;height:620px">'
          + '<h1 class="h" style="top:520px;font-size:200px">vamos<br>juntar o<br><i>seu?</i></h1>'
          + seta(660, 1180, 380, 1300, "#7cbcf2", 6, curva=90)
          + nota_mao(680, 1120, "é só chamar", rot=-5, size=52),
          "me chama no direct.<br>quem responde sou eu.", arrow=False),
]
S[-1] = S[-1].replace('<div class="grain">', '<p class="sm" style="right:72px;left:auto;bottom:72px;text-align:right">senerine.dev</p><div class="grain">')

open("espalhado.html", "w").write(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>""")
