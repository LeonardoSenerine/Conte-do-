"""Case Multsystems no estilo "grande" (o mesmo do case Scarpetta, inspirado no Teacher Leal): poucos elementos e
todos grandes, título enorme em Manrope (a fonte do site), foto da loja sangrando, celular gigante cortado pela borda
atravessando pro slide seguinte, grade de produtos reais do catálogo, passos da assistência e a elipse do logo.
Capturas do site rodando local, com o que cita a cidade escondido (regra do portfólio). Textos tirados do site e do BRIEFING.
8 slides 1080x1440 em panorama. Gerar: python3 multsystems-grande.py && node ../render.mjs multsystems-grande.html saida 1080 1440 8 panorama"""

N, W, H = 8, 1080, 1440
X = lambda n, x=0: (n - 1) * W + x
C = "../../elementos/clientes/multsystems/"
NAVY, BRAND, INK, TINT, LINE, CLARO, ZAP, BRANCO = "#1C2F5C", "#2E4686", "#1E2A46", "#EEF2FB", "#DCE3F2", "#9fb4ea", "#25D366", "#ffffff"
FUNDO = {1: "foto", 2: TINT, 3: BRANCO, 4: NAVY, 5: TINT, 6: BRANCO, 7: "foto", 8: "foto"}
FOTO = {1: ("fachada.jpg", "60% center"), 7: ("bancada.jpg", "center"), 8: ("fachada-noite.jpg", "center")}

CSS = r'''
* { box-sizing:border-box; margin:0; padding:0; }
body { width:8640px; height:1440px; overflow:hidden; position:relative; font-family:"Manrope",sans-serif; }
.a { position:absolute; }
.bg { top:0; width:1080px; height:1440px; }
.bg img { width:100%; height:100%; object-fit:cover; display:block; }
.top, .pe { font-size:26px; font-weight:600; letter-spacing:-.01em; z-index:6; }
.h { font-weight:800; line-height:.98; letter-spacing:-.045em; z-index:5; }
.sub { font-weight:600; letter-spacing:-.02em; z-index:5; }
.p { font-size:34px; line-height:1.38; letter-spacing:-.015em; z-index:5; }
.cel { border-radius:64px; padding:14px; background:#0d1526; z-index:4; box-shadow:0 60px 90px -30px rgba(10,20,45,.55); }
.cel img { display:block; width:100%; border-radius:50px; }
.jan { border-radius:18px; overflow:hidden; background:#0d1526; z-index:3; box-shadow:0 50px 90px -30px rgba(10,20,45,.45); }
.jan .barra { height:46px; background:#e6ebf5; display:flex; align-items:center; gap:10px; padding:0 20px; }
.jan .barra i { width:13px; height:13px; border-radius:50%; background:#c3cde3; }
.jan img { display:block; width:100%; }
.card { background:#fff; border-radius:16px; z-index:4; box-shadow:0 4px 16px rgb(28 47 92 / .06); border:1px solid #DCE3F2; overflow:hidden; }
.card .ft { height:250px; display:grid; place-items:center; background:#fff; }
.card .ft img { max-width:82%; max-height:86%; }
.card p { padding:0 22px; }
.passo { display:flex; gap:28px; align-items:baseline; padding:26px 0; border-top:2px solid rgba(255,255,255,.18); font-size:44px; font-weight:700; letter-spacing:-.03em; color:#fff; }
.passo b { font-size:30px; color:#9fb4ea; width:50px; font-weight:800; }
.passo small { display:block; font-size:28px; font-weight:500; color:rgba(255,255,255,.7); letter-spacing:-.01em; margin-top:6px; }
'''

E = []
for n, f in FUNDO.items():
    if f == "foto":
        img, pos = FOTO[n]
        E.append(f'<div class="a bg" style="left:{X(n)}px"><img src="{C}{img}" style="object-position:{pos}"></div>')
        E.append(f'<div class="a bg" style="left:{X(n)}px;background:linear-gradient(180deg, rgba(28,47,92,.72) 0%, rgba(28,47,92,.35) 40%, rgba(28,47,92,.88) 70%, {NAVY} 100%)"></div>')
    else:
        E.append(f'<div class="a bg" style="left:{X(n)}px;background:{f}"></div>')
# a elipse em pincelada do logo, em traço claro, atravessando a capa e o slide 2
E.append(f'<svg class="a" style="left:{X(1,-200)}px;top:120px;z-index:2;opacity:.14" width="2300" height="1300" viewBox="0 0 2300 1300"><ellipse cx="1150" cy="650" rx="1080" ry="520" transform="rotate(-12 1150 650)" fill="none" stroke="#fff" stroke-width="26" stroke-linecap="round" stroke-dasharray="5600 900"/></svg>')
for n in range(1, N + 1):
    E.append(f'<div class="a" style="left:{X(n,56)}px;top:0;width:2px;height:1440px;background:{CLARO};opacity:.6;z-index:2"></div>')
    claro = FUNDO[n] in ("foto", NAVY)
    cor = "#fff" if claro else INK
    seta = " · arrasta →" if n < N else ""
    E.append(f'<p class="a top" style="left:{X(n,104)}px;top:56px;color:{cor};opacity:.8">@senerine.dev</p>')
    E.append(f'<p class="a top" style="left:{X(n,604)}px;width:400px;text-align:right;top:56px;color:{cor};opacity:.8">{n:02d} / {N:02d}{seta}</p>')
    E.append(f'<p class="a pe" style="left:{X(n,400 if n == 2 else 104)}px;top:1350px;color:{cor}">Multsystems · case</p>')


def cel(src, x, y, w, rot=0):
    return f'<div class="a cel" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg"><img src="{C}{src}"></div>'


def jan(src, x, y, w, rot=0, alto=None):
    st = f"height:{alto}px;object-fit:cover;object-position:top" if alto else ""
    return f'<div class="a jan" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg"><div class="barra"><i></i><i></i><i></i></div><img src="{C}{src}" style="{st}"></div>'


def h(n, txt, top, size, cor, left=104, w=900):
    return f'<h2 class="a h" style="left:{X(n,left)}px;top:{top}px;width:{w}px;font-size:{size}px;color:{cor}">{txt}</h2>'


def sub(n, txt, top, cor, size=44, left=104, w=880):
    return f'<p class="a sub" style="left:{X(n,left)}px;top:{top}px;width:{w}px;font-size:{size}px;color:{cor}">{txt}</p>'


def p(n, txt, top, cor, w=840, left=104):
    return f'<p class="a p" style="left:{X(n,left)}px;top:{top}px;width:{w}px;color:{cor}">{txt}</p>'


L = lambda t, c=CLARO: f'<span style="color:{c}">{t}</span>'

# 1 · capa: a fachada de fundo, título enorme e o celular gigante entrando no slide 2
E.append(h(1, f"Site novo<br>{L('no ar.')}", 830, 128, "#fff", 104, 700))
E.append(sub(1, "Multsystems · informática desde 1995", 1110, CLARO, 36, 104, 620))
E.append(p(1, "Uma loja para empresa e para casa, agora inteira no site.", 1170, "#fff", 600))
E.append(cel("m-home.jpg", X(1, 760), 190, 620, 4))

# 2 · antes: o site antigo, com muito texto e pouca foto
E.append(h(2, f"Antes,<br>{L('muito texto.', BRAND)}", 170, 104, INK, 400, 640))
E.append(sub(2, "E quase nenhuma foto.", 400, BRAND, 44, 404, 600))
E.append(jan("d-antigo.jpg", X(2, 380), 560, 700, 2))
E.append(p(2, "O site antigo explicava, mas não mostrava a loja nem os produtos.", 1080, INK, 600, 400))

# 3 · o catálogo: grade de produtos reais
E.append(h(3, f"O catálogo<br>{L('inteiro.', BRAND)}", 160, 140, INK))
E.append(sub(3, "Com foto, preço e filtro por marca.", 440, BRAND, 44))
prods = [("notebook", "Dell", "Notebook i5"), ("impressora", "Brother", "Impressora laser"), ("camera", "Intelbras", "Câmera Wi-Fi"),
         ("roteador", "Huawei", "Roteador mesh"), ("nobreak", "SMS", "Nobreak 1500VA"), ("cadeira", "ThunderX3", "Cadeira gamer")]
for i, (f, marca, nome) in enumerate(prods):
    x, y = 104 + (i % 3) * 296, 560 + (i // 3) * 380
    E.append(f'''<div class="a card" style="left:{X(3,x)}px;top:{y}px;width:280px;height:360px"><div class="ft"><img src="{C}produtos/{f}.png"></div>
      <p style="font-size:18px;font-weight:700;color:#5B6785;letter-spacing:.06em;text-transform:uppercase;margin-top:6px">{marca}</p>
      <p style="font-size:28px;font-weight:700;color:{INK};letter-spacing:-.02em;margin-top:6px">{nome}</p></div>''')

# 4 · para empresa: o orçamento num computador grande, cortado pela borda
E.append(h(4, f"Orçamento<br>{L('para empresa.')}", 160, 140, "#fff"))
E.append(p(4, "Cotação com nota no CNPJ e um vendedor que acompanha o pedido do começo ao fim.", 470, "rgba(255,255,255,.82)", 820))
E.append(jan("d-empresas.jpg", X(4, 70), 700, 1000, -2))

# 5 · para casa: o produto no celular e o WhatsApp
E.append(h(5, f"Viu o<br>preço,<br>{L('chamou.', BRAND)}", 160, 124, INK, 104, 500))
E.append(p(5, "Cada produto com preço e o botão de comprar pelo WhatsApp.", 560, INK, 460))
E.append(cel("m-produto.jpg", X(5, 590), 330, 440, 4))
E.append(f'<div class="a" style="left:{X(5,104)}px;top:800px;z-index:5;background:{ZAP};color:#fff;font-size:38px;font-weight:700;letter-spacing:-.02em;padding:30px 44px;border-radius:12px;box-shadow:0 30px 50px -20px rgba(37,211,102,.5)">Comprar pelo WhatsApp</div>')
E.append(f'''<div class="a" style="left:{X(5,104)}px;top:960px;width:440px;z-index:5;background:#fff;border-radius:16px;padding:30px 34px;font-size:30px;line-height:1.4;color:{INK};box-shadow:0 30px 60px -30px rgba(28,47,92,.35)">
  Olá! Tenho interesse no produto: Notebook i5 <span style="color:#5B6785">(cód. 0014409)</span></div>''')

# 6 · não achou: a busca vazia vira encomenda
E.append(h(6, f"Não achou?<br>{L('Dá pra<br>conseguir.', BRAND)}", 160, 124, INK, 104, 900))
E.append(p(6, "Busca sem resultado vira pedido por encomenda, com um atendente no WhatsApp.", 560, INK, 820))
E.append(cel("m-naoachou.jpg", X(6, 300), 760, 480, -3))
E.append(f'<div class="a" style="left:{X(6,640)}px;top:830px;z-index:5;background:#fff;border:2px solid {LINE};border-radius:12px;padding:20px 28px;font-size:30px;font-weight:600;color:{INK};rotate:4deg;box-shadow:0 30px 50px -25px rgba(28,47,92,.35)">🔍 geladeira</div>')

# 7 · assistência: a bancada de fundo e os 4 passos
E.append(h(7, f"Parou?<br>{L('A Total Tech<br>resolve.')}", 200, 116, "#fff", 104, 900))
passos = [("Fale com a gente", "Conte o problema pelo site ou pelo WhatsApp."), ("Avaliação em 24h", "O técnico avalia o equipamento."),
          ("Você aprova", "O conserto só começa com o seu ok."), ("Entrega com garantia", "90 dias de garantia no serviço.")]
E.append(f'<div class="a" style="left:{X(7,104)}px;top:700px;width:860px;border-bottom:2px solid rgba(255,255,255,.18);z-index:5">'
         + "".join(f'<div class="passo"><b>{i+1}</b><span>{a}<small>{s}</small></span></div>' for i, (a, s) in enumerate(passos)) + '</div>')

# 8 · chamada
E.append(f'<div class="a" style="left:{X(8,104)}px;top:180px;width:150px;height:150px;border-radius:50%;overflow:hidden;z-index:5"><img src="../../elementos/senerine/leonardo-ponto.webp" style="width:100%;height:100%"></div>')
E.append(f'<p class="a" style="left:{X(8,280)}px;top:214px;font-size:34px;font-weight:700;color:#fff;z-index:5">Leonardo Senerine</p><p class="a" style="left:{X(8,280)}px;top:262px;font-size:26px;color:#fff;opacity:.75;z-index:5">senerine.dev · sites e aplicações</p>')
E.append(h(8, f"O seu negócio<br>também merece<br>{L('um site assim.')}", 680, 112, "#fff"))
E.append(p(8, "Me chama no direct. Quem responde sou eu.", 1120, "#fff", 760))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(E)}<script>document.fonts.ready.then(() => document.body.dataset.ok = 1)</script></body></html>'''
open("multsystems-grande.html", "w").write(html)
