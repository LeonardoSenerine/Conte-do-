"""Carrossel "você precisa de um site." (afirmativo, a pedido dele) na linguagem editorial (referência: feed do estúdio Herground):
uma frase forte por slide, Inter Tight 800 em minúsculas com uma palavra em Instrument Serif itálica,
três fundos se alternando (creme, preto, azul) e imagens do banco grandes. Refaz o zine nº 05, que ficou genérico.
8 slides 1080x1440. Gerar: python3 busca-editorial.py && node ../render.mjs busca-editorial.html saida 1080 1440 8"""

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
    pe = f'<p class="sm" style="bottom:72px;width:640px">{sm}</p>' if sm else ""
    ar = '<p class="arrow" style="bottom:66px">→</p>' if arrow else ""
    return f'<section class="s {cor}" id="s{n}">{inner}{pe}{ar}<div class="grain"></div></section>'


S = [
    slide(1, "cream", '<h1 class="h" style="top:330px;font-size:210px">você<br><i>precisa</i> de<br>um site.</h1>',
          "e não é pra dizer que tem.<br>é pra vender."),
    slide(2, "black", f'''<img class="img" src="{T}eclipse-sol-claro.png" style="left:300px;top:640px;width:900px;opacity:.9">
      <div style="left:680px;top:914px;width:150px;height:150px;border-radius:50%;background:var(--blue);z-index:2;box-shadow:0 0 60px rgba(74,163,234,.5)"></div>
      <h1 class="h" style="top:110px;font-size:150px">seu cliente<br>já está te<br><i>procurando.</i></h1>''',
          "no google, no mapa, no “perto de mim”.<br>a pergunta é o que ele encontra."),
    slide(3, "blue", '<h1 class="h" style="top:420px;font-size:190px">instagram<br>é <i>aluguel.</i><br>site é seu.</h1>',
          "o perfil segue as regras de outra empresa.<br>o endereço do site é seu."),
    slide(4, "cream", f'''<img class="img" src="{T}estrelas.png" style="left:640px;top:40px;height:1360px">
      <h1 class="h" style="top:110px;font-size:140px">confiança<br>vem <i>antes</i><br>do primeiro<br>oi.</h1>''',
          "endereço, fotos, cardápio, avaliações.<br>quem vê antes chama mais seguro."),
    slide(5, "black", f'''<img class="img" src="{T}cisnes-claro.png" style="left:90px;top:560px;width:900px">
      <h1 class="h" style="top:110px;font-size:150px">site <i>trabalha</i><br>enquanto<br>você dorme.</h1>''',
          "a vitrine que não fecha e responde<br>as mesmas perguntas por você."),
    slide(6, "cream", f'''<img class="img" src="{T}washington.png" style="left:40px;top:620px;width:1000px">
      <h1 class="h" style="top:110px;font-size:150px"><i>sem site,</i><br>você depende<br>de sorte.</h1>''',
          "do algoritmo, do story certo<br>na hora certa.", arrow=True),
    slide(7, "blue", '<h1 class="h" style="top:330px;font-size:180px">site é a<br><i>vitrine.</i><br>a busca<br>é a <i>rua.</i></h1>',
          "e o seu negócio precisa<br>estar nas duas."),
    slide(8, "black", '''<div style="left:72px;top:150px;width:120px;height:120px;border-radius:50%;background:var(--blue);box-shadow:0 0 50px rgba(74,163,234,.55)"></div>
      <h1 class="h" style="top:420px;font-size:200px">vamos<br>fazer o<br><i>seu?</i></h1>''',
          "me chama no direct.<br>quem responde sou eu.", arrow=False),
]
S[-1] = S[-1].replace('<div class="grain">', '<p class="sm" style="right:72px;left:auto;bottom:72px;text-align:right">senerine.dev</p><div class="grain">')

open("busca-editorial.html", "w").write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>''')
