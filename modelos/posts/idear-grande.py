"""Case Idear Empreendimentos no estilo "grande" (o mesmo dos cases Scarpetta e Multsystems, inspirado no Teacher Leal):
poucos elementos e todos grandes, título enorme em Cormorant Garamond (a fonte dos títulos da Idear) com a palavra em
itálico no bronze, render sangrando, celular gigante cortado pela borda atravessando pro slide seguinte, o computador
com a galeria atravessando do 3 pro 4, renders em grade, paleta e posts do guia da marca.
Capturas do site rodando local, sem a cidade e sem os números provisórios da prévia (regra do portfólio).
O "antes" vem do comparativo da proposta (site antigo em 14/11/2026). Textos tirados do site e da proposta.
8 slides 1080x1440 em panorama. Gerar: python3 idear-grande.py && node ../render.mjs idear-grande.html saida 1080 1440 8 panorama"""

N, W, H = 8, 1080, 1440
X = lambda n, x=0: (n - 1) * W + x
C = "../../elementos/clientes/idear/"
NAVY, DEEP, BRONZE, BRONZE_E, BRONZE_C, MARFIM, AREIA, PEDRA, LINHA = (
    "#07324F", "#052640", "#756B48", "#635A3A", "#C4B992", "#FAF8F4", "#F1EDE5", "#5B6570", "#DDD7CB")
FUNDO = {1: "foto", 2: AREIA, 3: MARFIM, 4: NAVY, 5: AREIA, 6: MARFIM, 7: DEEP, 8: "foto"}
FOTO = {1: ("casa/fachada-frontal.jpg", "center 30%"), 8: ("casa/piscina.jpg", "center")}

CSS = r'''
* { box-sizing:border-box; margin:0; padding:0; }
body { width:8640px; height:1440px; overflow:hidden; position:relative; font-family:"Manrope",sans-serif; }
.a { position:absolute; }
.bg { top:0; width:1080px; height:1440px; }
.bg img { width:100%; height:100%; object-fit:cover; display:block; }
.top, .pe { font-size:26px; font-weight:600; letter-spacing:-.01em; z-index:6; }
.h { font-family:"Cormorant Garamond",serif; font-weight:500; line-height:.92; letter-spacing:-.02em; z-index:5; }
.h i { font-style:italic; }
.sub { font-weight:600; letter-spacing:.16em; text-transform:uppercase; z-index:5; }
.p { font-size:34px; line-height:1.4; letter-spacing:-.015em; z-index:5; }
.cel { border-radius:64px; padding:14px; background:#0b1620; z-index:4; box-shadow:0 60px 90px -30px rgba(5,38,64,.55); }
.cel img { display:block; width:100%; border-radius:50px; }
.jan { border-radius:14px; overflow:hidden; background:#0b1620; z-index:3; box-shadow:0 50px 90px -30px rgba(5,38,64,.5); }
.jan .barra { height:44px; background:#ebe6dc; display:flex; align-items:center; gap:10px; padding:0 20px; }
.jan .barra i { width:13px; height:13px; border-radius:50%; background:#cfc6b2; }
.jan img { display:block; width:100%; }
.ft { overflow:hidden; z-index:4; box-shadow:0 40px 70px -30px rgba(5,38,64,.45); }
.ft img { width:100%; height:100%; object-fit:cover; display:block; }
.tag { background:#FAF8F4; color:#07324F; font-size:22px; font-weight:600; padding:10px 16px; z-index:5; letter-spacing:-.01em; }
.chip { font-size:30px; font-weight:600; color:#07324F; letter-spacing:-.01em; display:flex; align-items:center; gap:16px; }
.chip::before { content:""; width:11px; height:11px; background:#756B48; rotate:45deg; }
.bt { font-size:36px; font-weight:700; letter-spacing:-.02em; padding:30px 0; width:440px; text-align:center; z-index:5; border-radius:2px; }
.cor { z-index:5; }
.cor div { width:128px; height:128px; border-radius:2px; }
.cor p { font-size:20px; font-weight:600; color:#C4B992; letter-spacing:.06em; margin-top:12px; }
'''

E = []
for n, f in FUNDO.items():
    if f == "foto":
        img, pos = FOTO[n]
        E.append(f'<div class="a bg" style="left:{X(n)}px"><img src="{C}{img}" style="object-position:{pos}"></div>')
        E.append(f'<div class="a bg" style="left:{X(n)}px;background:linear-gradient(180deg, rgba(5,38,64,{.55 if n == 1 else .8}) 0%, rgba(5,38,64,.15) 35%, rgba(5,38,64,.85) 62%, {DEEP} 100%)"></div>')
    else:
        E.append(f'<div class="a bg" style="left:{X(n)}px;background:{f}"></div>')
# o símbolo da Idear em traço bronze, grande e apagado, atravessando o 7 e o 8
E.append(f'<img class="a" src="{C}marca/symbol-bronze.png" style="left:{X(7,560)}px;top:120px;height:980px;opacity:.10;z-index:2">')
for n in range(1, N + 1):
    escuro = FUNDO[n] in ("foto", NAVY, DEEP)
    cor = MARFIM if escuro else NAVY
    E.append(f'<div class="a" style="left:{X(n,56)}px;top:0;width:2px;height:1440px;background:{BRONZE_C if escuro else BRONZE};opacity:.55;z-index:2"></div>')
    seta = " · arrasta →" if n < N else ""
    E.append(f'<p class="a top" style="left:{X(n,104)}px;top:56px;color:{cor};opacity:.8">@senerine.dev</p>')
    E.append(f'<p class="a top" style="left:{X(n,604)}px;width:400px;text-align:right;top:56px;color:{cor};opacity:.8">{n:02d} / {N:02d}{seta}</p>')
    E.append(f'<p class="a pe" style="left:{X(n,400 if n == 2 else 104)}px;top:1350px;color:{cor}">Idear Empreendimentos · case</p>')


def cel(src, x, y, w, rot=0):
    return f'<div class="a cel" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg"><img src="{C}{src}"></div>'


def jan(src, x, y, w, rot=0):
    return f'<div class="a jan" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg"><div class="barra"><i></i><i></i><i></i></div><img src="{C}{src}"></div>'


def ft(src, x, y, w, h, rot=0, pos="center", z=4):
    return f'<div class="a ft" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;rotate:{rot}deg;z-index:{z}"><img src="{C}{src}" style="object-position:{pos}"></div>'


def h(n, txt, top, size, cor, left=104, w=920):
    return f'<h2 class="a h" style="left:{X(n,left)}px;top:{top}px;width:{w}px;font-size:{size}px;color:{cor}">{txt}</h2>'


def sub(n, txt, top, cor, size=26, left=104, w=880):
    return f'<p class="a sub" style="left:{X(n,left)}px;top:{top}px;width:{w}px;font-size:{size}px;color:{cor}">{txt}</p>'


def p(n, txt, top, cor, w=840, left=104):
    return f'<p class="a p" style="left:{X(n,left)}px;top:{top}px;width:{w}px;color:{cor}">{txt}</p>'


I = lambda t, c: f'<i style="color:{c}">{t}</i>'

# 1 · capa: o render da fachada de fundo, título enorme e o celular gigante entrando no slide 2
E.append(sub(1, "Idear Empreendimentos", 790, BRONZE_C, 26, 104, 620))
E.append(h(1, f"Site novo<br>{I('no ar.', BRONZE_C)}", 850, 170, MARFIM, 104, 680))
E.append(p(1, "Casas de alto padrão, uma por vez. Agora com um site à altura delas.", 1180, MARFIM, 600))
E.append(cel("m-casa.jpg", X(1, 760), 170, 620, 4))

# 2 · antes: o modelo pronto, com texto de exemplo
E.append(h(2, f"Antes,<br>{I('um modelo<br>pronto.', BRONZE)}", 160, 120, NAVY, 400, 640))
E.append(p(2, "Com frase de exemplo no lugar da Idear.", 540, NAVY, 600, 404))
E.append(jan("d-antigo.jpg", X(2, 560), 700, 470, 2))
E.append(cel("m-antigo.jpg", X(2, 400), 690, 280, -3))
E.append(p(2, "Não mostrava a casa à venda nem quem constrói.", 1110, PEDRA, 340, 720))

# 3 · a página da casa: lista do que ela tem e a galeria num computador grande que atravessa pro 4
E.append(h(3, f"Uma página<br>{I('só pra casa.', BRONZE)}", 160, 150, NAVY))
chips = ["Galeria", "Planta", "Acabamentos", "Localização", "Visita"]
E.append(f'<div class="a" style="left:{X(3,104)}px;top:480px;width:900px;display:flex;flex-wrap:wrap;gap:18px 40px;z-index:5">'
         + "".join(f'<span class="chip">{c}</span>' for c in chips) + '</div>')
E.append(jan("d-galeria.jpg", X(3, 150), 640, 1060, -2))

# 4 · o vídeo: o render ganhou movimento
E.append(h(4, f"O render<br>{I('ganhou<br>movimento.', BRONZE_C)}", 160, 138, MARFIM, 260, 800))
E.append(p(4, "O vídeo de abertura nasce do render da fachada, com profundidade em 2.5D.", 620, "rgba(250,248,244,.82)", 700, 260))
E.append(ft("video/q-0.jpg", X(4, 260), 800, 640, 500, -2, "center 60%"))
E.append(f'''<div class="a" style="left:{X(4,300)}px;top:1200px;width:560px;z-index:6;padding:14px 22px;background:rgba(5,38,64,.78);display:flex;align-items:center;gap:18px;color:{MARFIM};font-size:22px;font-weight:600;rotate:-2deg">
  <span style="width:46px;height:46px;border-radius:50%;background:{MARFIM};display:grid;place-items:center"><span style="width:0;height:0;border-left:15px solid {NAVY};border-top:10px solid transparent;border-bottom:10px solid transparent;margin-left:4px"></span></span>
  <span style="flex:1;height:4px;background:rgba(250,248,244,.35)"><span style="display:block;width:45%;height:100%;background:{BRONZE_C}"></span></span>em loop</div>''')

# 5 · os ambientes e os materiais, em renders grandes
E.append(h(5, f"Cada detalhe,<br>{I('com nome.', BRONZE)}", 160, 140, NAVY))
E.append(p(5, "Pedra, madeira, granilite: a página diz o material de cada parte da casa.", 450, NAVY, 820))
E.append(ft("casa/gourmet-churrasqueira.jpg", X(5, 104), 650, 520, 650, -1.5))
E.append(f'<p class="a tag" style="left:{X(5,124)}px;top:1220px;rotate:-1.5deg">Forro ripado de madeira</p>')
E.append(ft("casa/banho-suite-principal.jpg", X(5, 650), 640, 340, 310, 2))
E.append(f'<p class="a tag" style="left:{X(5,668)}px;top:900px;rotate:2deg">Granilite</p>')
E.append(ft("casa/acab-fachada.jpg", X(5, 670), 990, 310, 310, -1, "center 40%"))
E.append(f'<p class="a tag" style="left:{X(5,688)}px;top:1250px;rotate:-1deg">Pedra em filetes</p>')

# 6 · a visita: os dois botões do celular e o formulário
E.append(h(6, f"Gostou?<br>{I('Agenda<br>a visita.', BRONZE)}", 160, 140, NAVY, 104, 560))
E.append(p(6, "WhatsApp fixo no celular e pedido de visita em cada página.", 620, NAVY, 460))
E.append(f'<div class="a bt" style="left:{X(6,104)}px;top:860px;background:{MARFIM};color:{NAVY};border:2px solid {NAVY}">Agendar visita</div>')
E.append(f'<div class="a bt" style="left:{X(6,104)}px;top:990px;background:{BRONZE};color:{MARFIM}">WhatsApp</div>')
E.append(cel("m-agendar.jpg", X(6, 600), 300, 440, 4))

# 7 · a marca: paleta e posts do guia
E.append(h(7, f"E a marca<br>{I('veio junto.', BRONZE_C)}", 160, 150, MARFIM))
E.append(p(7, "Guia da marca e a coleção de lançamento: posts, carrossel, stories e capas de destaque.", 470, "rgba(250,248,244,.82)", 820))
cores = [(NAVY, "07324F"), (BRONZE, "756B48"), (BRONZE_E, "635A3A"), (BRONZE_C, "C4B992"), (MARFIM, "FAF8F4"), (AREIA, "F1EDE5")]
E.append(f'<div class="a cor" style="left:{X(7,104)}px;top:640px;display:flex;gap:18px">'
         + "".join(f'<span><div style="background:{c};{"outline:2px solid rgba(250,248,244,.35)" if c == NAVY else ""}"></div><p>#{hx}</p></span>' for c, hx in cores) + '</div>')
for i, (f, x, y, r) in enumerate([("post-05-area-gourmet", 104, 870, -5), ("post-12-arquitetura", 380, 840, 0), ("post-08-suite-master", 656, 870, 5)]):
    E.append(ft(f"guia/{f}.jpg", X(7, x), y, 320, 400, r, z=4 + (i == 1)))

# 8 · chamada
E.append(f'<div class="a" style="left:{X(8,104)}px;top:180px;width:150px;height:150px;border-radius:50%;overflow:hidden;z-index:5"><img src="../../elementos/senerine/leonardo-ponto.webp" style="width:100%;height:100%"></div>')
E.append(f'<p class="a" style="left:{X(8,280)}px;top:214px;font-size:34px;font-weight:700;color:{MARFIM};z-index:5">Leonardo Senerine</p><p class="a" style="left:{X(8,280)}px;top:262px;font-size:26px;color:{MARFIM};opacity:.8;z-index:5">senerine.dev · sites e aplicações</p>')
E.append(h(8, f"A sua empresa<br>também merece<br>{I('um site assim.', BRONZE_C)}", 700, 130, MARFIM))
E.append(p(8, "Me chama no direct. Quem responde sou eu.", 1150, MARFIM, 760))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(E)}<script>document.fonts.ready.then(() => document.body.dataset.ok = 1)</script></body></html>'''
open("idear-grande.html", "w").write(html)
