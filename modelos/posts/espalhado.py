"""Carrossel "você precisa de um site." (editorial): o negócio espalhado em agenda no Forms, Linktree,
cardápio em PDF e preço no direct; o site junta tudo; prova real na D'Conde (dados do estudo de caso).
9 slides 1080x1440. Gerar: python3 espalhado.py && node ../render.mjs espalhado.html saida 1080 1440 9"""

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


S = [
    slide(1, "cream", '<h1 class="h" style="top:330px;font-size:210px">você<br><i>precisa</i> de<br>um site.</h1>',
          "porque hoje o seu negócio<br>está espalhado."),
    slide(2, "black", '<h1 class="h" style="top:420px;font-size:200px">agenda<br>no <i>forms.</i></h1>',
          "o cliente preenche e fica esperando<br>você conferir, confirmar e responder."),
    slide(3, "blue", '<h1 class="h" style="top:420px;font-size:200px">links no<br><i>linktree.</i></h1>',
          "uma lista igual à de todo mundo, com o<br>nome de outra empresa no endereço."),
    slide(4, "cream", f"""<img class="img" src="{T}fim.png" style="left:220px;top:380px;width:820px">
      <h1 class="h" style="top:110px;font-size:200px">cardápio<br>em <i>pdf.</i></h1>""",
          "abre pequeno no celular, ninguém lê<br>direito e o google não acha."),
    slide(5, "black", '<h1 class="h" style="top:360px;font-size:190px">preço<br>só no<br><i>direct.</i></h1>',
          "a mesma pergunta respondida<br>o dia inteiro, por você."),
    slide(6, "blue", f"""<img class="img" src="{T}passaros-borrados.png" style="left:460px;top:-80px;height:1600px">
      <h1 class="h" style="top:110px;font-size:170px">tudo<br>espalhado.<br><i>nada<br>é seu.</i></h1>""",
          "cada ferramenta com uma cara,<br>um login e uma regra diferente."),
    slide(7, "cream", f"""<img class="img" src="{T}cisnes.png" style="left:40px;top:560px;width:1000px">
      <h1 class="h" style="top:110px;font-size:170px">um site<br><i>junta tudo.</i></h1>""",
          "agenda, cardápio, preço, links e contato.<br>num endereço só, com a sua cara."),
    slide(8, "black", f"""<img src="../../elementos/senerine/dconde-agenda.jpg" style="left:72px;top:620px;width:936px;border-radius:24px;z-index:2">
      <h1 class="h" style="top:110px;font-size:124px">na d’conde,<br>a agenda <i>saiu<br>do whatsapp.</i></h1>""",
          "o cliente marca em 4 passos, vê só os<br>horários livres e recebe lembrete 3 horas antes."),
    slide(9, "blue", """<div style="left:72px;top:150px;width:120px;height:120px;border-radius:50%;background:var(--cream);box-shadow:0 0 50px rgba(242,239,234,.35)"></div>
      <h1 class="h" style="top:420px;font-size:200px">vamos<br>juntar o<br><i>seu?</i></h1>""",
          "me chama no direct.<br>quem responde sou eu.", arrow=False),
]
S[-1] = S[-1].replace('<div class="grain">', '<p class="sm" style="right:72px;left:auto;bottom:72px;text-align:right">senerine.dev</p><div class="grain">')

open("espalhado.html", "w").write(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>""")
