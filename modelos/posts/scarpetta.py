"""Carrossel do case Scarpetta Cucina: o link da bio saiu do Linktree e virou site. Linguagem editorial na "sala"
do cliente (verde garrafa, creme, Fraunces e a assinatura em Pinyon Script), capturas reais do site, grade limpa (versão "bonitinha": um celular reto por slide, sem rabiscos).
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
.phone .sc2 { border-radius:42px; overflow:hidden; height:100%; background:#0b0b0b; }
.phone .sc2 img { display:block; width:100%; }
.shot { border-radius:6px; overflow:hidden; z-index:2; }
.shot img { display:block; width:100%; }
.pill { height:84px; border-radius:999px; background:#fff; color:#1e1d1e; display:inline-grid; place-items:center; padding:0 48px; font-family:-apple-system,"Inter Tight",sans-serif; font-size:32px; font-weight:500; }
.img { z-index:1; }
.sub { left:72px; width:900px; font-size:30px; font-weight:500; line-height:1.35; letter-spacing:-.015em; opacity:.85; z-index:3; }
.de { left:50%; transform:translateX(-50%); font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.06em; text-transform:uppercase; z-index:3; white-space:nowrap; }
.de b { font-weight:400; text-decoration:line-through; text-decoration-thickness:2px; opacity:.6; margin-left:10px; }
.lista { left:72px; width:900px; font-size:30px; font-weight:500; line-height:1.3; letter-spacing:-.015em; z-index:3; }
.lista li { list-style:none; padding:14px 0; border-top:1.5px solid currentColor; display:flex; gap:22px; }
.lista li:last-child { border-bottom:1.5px solid currentColor; }
.lista li span { font-family:"Fraunces",serif; font-style:italic; opacity:.7; width:34px; flex:none; }
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


def centro(src, top=560, w=420, h=820, extra=""):
    return phone(src, (1080 - w) // 2, top, w, h, 0, extra)


def lista(itens, top):
    return f'<ul class="lista" style="top:{top}px">' + "".join(f"<li><span>{i+1}</span>{t}</li>" for i, t in enumerate(itens)) + "</ul>"


def troca(n, cor, de, titulo, img, texto, curto=False):
    arte = (f'<div class="shot" style="left:190px;top:640px;width:700px"><img src="{C}{img}"></div>' if curto else centro(img, 520, 400, 650))
    return slide(n, cor, f'<h1 class="h" style="top:150px;font-size:130px">{titulo}</h1>'
                 f'<p class="de" style="top:440px">no linktree era<b>{de}</b></p>' + arte, texto)


S = [
    # 1 · capa: o nome da casa e os dois celulares lado a lado
    slide(1, "noite", '<h1 class="h" style="top:150px;font-size:130px;text-align:center">do linktree<br>ao site da<br><span class="sc" style="font-size:1.5em">Scarpetta</span></h1>'
          + phone("linktree-sem-cidade.png", 150, 700, 320, 586, 0, "filter:grayscale(1);opacity:.75")
          + phone("site.webp", 590, 670, 340, 617, 0)
          + '<p class="de" style="top:1320px;left:310px">antes</p><p class="de" style="top:1320px;left:760px">depois</p>', "", False),
    # 2 · antes
    slide(2, "papel", '<h1 class="h" style="top:150px;font-size:150px">antes:<br><i>um linktree.</i></h1>'
          + lista(["fundo cinza, igual ao de qualquer perfil", "nenhum prato, nenhuma foto do salão", "cada botão leva pra outro lugar"], 470)
          + centro("linktree-sem-cidade.png", 740, 340, 625), ""),
    # 3 · depois
    slide(3, "verde", '<h1 class="h" style="top:150px;font-size:150px">depois:<br><i>a cara da casa.</i></h1>'
          + lista(["verde garrafa e creme", "o tomate do logo", "a assinatura manuscrita"], 470)
          + centro("site.webp", 740, 340, 617), ""),
    troca(4, "papel", "Reservas", "a reserva<br><i>chega pronta.</i>", "reserva.webp",
          "dia, horário e pessoas: o whatsapp da casa<br>recebe a mensagem completa."),
    troca(5, "verde", "Menu", "o cardápio<br><i>com foto e preço.</i>", "cardapio.webp",
          "pratos com foto, descrição e preço,<br>separados por categoria."),
    troca(6, "papel", "Peça pelo Ifood · Peça pelo nosso delivery", "pedidos<br><i>num lugar só.</i>", "delivery.webp",
          "o ifood e o delivery próprio, lado a lado.", curto=True),
    troca(7, "verde", "Eventos e confraternizações", "eventos<br><i>com orçamento.</i>", "eventos.webp",
          "as ocasiões, como o menu é servido<br>e o pedido de orçamento direto."),
    # 8 · o que o linktree nunca mostrou
    slide(8, "noite", '<h1 class="h" style="top:150px;font-size:130px">e o que o linktree<br><i>nunca mostrou.</i></h1>'
          + phone("executivo.webp", 130, 560, 380, 608, 0) + phone("salao.webp", 570, 560, 380, 608, 0)
          + '<p class="de" style="top:1200px;left:320px">menu da semana</p><p class="de" style="top:1200px;left:760px">o salão</p>', ""),
    # 9 · chamada nas cores da senerine
    slide(9, "preto", '<div style="left:72px;top:170px;width:110px;height:110px;border-radius:50%;background:var(--blue)"></div>'
          + '<h1 class="h" style="top:560px;font-size:150px">o seu link<br>da bio também<br>pode <i>virar casa.</i></h1>',
          "me chama no direct.<br>quem responde sou eu.", False, rot="senerine.dev"),
]

open("scarpetta.html", "w").write(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>""")
