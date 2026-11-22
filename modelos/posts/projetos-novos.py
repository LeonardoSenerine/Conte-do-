"""Projetos novos no ar: carrossel simples de 2 slides, uma foto por projeto (Multsystems e Idear Empreendimentos).
Foto do cliente sangrando, o site no celular grande e a frase na linguagem editorial da Senerine
(Inter Tight 800 minúscula + uma palavra em Instrument Serif itálica, ponto azul).
Gerar: python3 projetos-novos.py && node ../render.mjs projetos-novos.html saida 1080 1440 2 panorama"""

N, W, H = 2, 1080, 1440
X = lambda n, x=0: (n - 1) * W + x
E_ = "../../elementos/"
AZUL, CREME = "#0a63b2", "#f6f1e7"

slides = [
    dict(foto="clientes/multsystems/fachada.jpg", pos="55% center", cel="clientes/multsystems/m-home.jpg",
         num="01", nome="Multsystems", seg="Loja de informática desde 1995",
         titulo='dois projetos<br>novos <i>no ar</i><span class="ponto"></span>'),
    dict(foto="clientes/idear/casa/fachada-frontal.jpg", pos="center 30%", cel="clientes/idear/m-casa.jpg",
         num="02", nome="Idear Empreendimentos", seg="Casas de alto padrão",
         titulo='o próximo<br>pode ser <i>o seu</i><span class="ponto"></span>'),
]

CSS = r'''
* { box-sizing:border-box; margin:0; padding:0; }
body { width:2160px; height:1440px; overflow:hidden; position:relative; font-family:"Inter Tight",sans-serif; color:#f6f1e7; }
.a { position:absolute; }
.bg { top:0; width:1080px; height:1440px; overflow:hidden; }
.bg img { width:100%; height:100%; object-fit:cover; display:block; }
.top { font-size:26px; font-weight:600; letter-spacing:-.01em; opacity:.85; z-index:6; }
.h { font-weight:800; font-size:136px; line-height:.9; letter-spacing:-.055em; text-transform:lowercase; z-index:5; }
.h i { font-family:"Instrument Serif",serif; font-weight:400; font-style:italic; letter-spacing:-.02em; font-size:1.12em; }
.ponto { display:inline-block; width:.2em; height:.2em; border-radius:50%; background:#0a63b2; margin-left:.06em; box-shadow:0 0 40px rgba(10,99,178,.8); }
.cel { border-radius:60px; padding:13px; background:#0d0d0f; z-index:4; box-shadow:0 60px 90px -30px rgba(0,0,0,.6); }
.cel img { display:block; width:100%; border-radius:48px; }
.rot { z-index:5; text-shadow:0 2px 24px rgba(0,0,0,.55); display:flex; gap:22px; align-items:baseline; }
.rot b { font-family:"JetBrains Mono",monospace; font-size:26px; font-weight:500; color:#8fbff0; }
.rot span { font-size:38px; font-weight:700; letter-spacing:-.03em; }
.rot small { display:block; font-size:26px; font-weight:500; opacity:.75; letter-spacing:-.01em; margin-top:6px; }
.nota { font-size:30px; line-height:1.4; letter-spacing:-.01em; z-index:5; opacity:.9; }
'''

E = []
for i, s in enumerate(slides, 1):
    E.append(f'<div class="a bg" style="left:{X(i)}px"><img src="{E_}{s["foto"]}" style="object-position:{s["pos"]}"></div>')
    E.append(f'<div class="a bg" style="left:{X(i)}px;background:linear-gradient(180deg, rgba(8,10,14,.78) 0%, rgba(8,10,14,.45) 20%, rgba(8,10,14,.05) 36%, rgba(8,10,14,.35) 55%, rgba(8,10,14,.92) 82%, #08090c 100%)"></div>')
    E.append(f'<p class="a top" style="left:{X(i,72)}px;top:60px">@senerine.dev</p>')
    E.append(f'<p class="a top" style="left:{X(i,608)}px;width:400px;text-align:right;top:60px">{i:02d} / {N:02d}{" · arrasta →" if i < N else ""}</p>')
    E.append(f'<div class="a cel" style="left:{X(i,650)}px;top:170px;width:390px;rotate:{4 if i == 1 else -4}deg"><img src="{E_}{s["cel"]}"></div>')
    E.append(f'<div class="a rot" style="left:{X(i,72)}px;top:250px;width:520px"><b>{s["num"]}</b><span>{s["nome"]}<small>{s["seg"]}</small></span></div>')
    E.append(f'<h2 class="a h" style="left:{X(i,72)}px;top:1010px;width:960px">{s["titulo"]}</h2>')

E.append(f'<p class="a nota" style="left:{X(1,72)}px;top:1290px;width:900px">Uma loja e uma incorporadora, cada uma com a sua cara.</p>')
E.append(f'<p class="a nota" style="left:{X(2,72)}px;top:1290px;width:900px">Me chama no direct. Quem responde sou eu.</p>')

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(E)}<script>document.fonts.ready.then(() => document.body.dataset.ok = 1)</script></body></html>'''
open("projetos-novos.html", "w").write(html)
