"""Case Scarpetta Cucina, versão "grande" (inspirada no carrossel do site do Teacher Leal): poucos elementos por slide
e todos grandes, título enorme na fonte da casa (Fraunces) com legenda em italiano (Pinyon Script), foto sangrando,
celular gigante cortado pela borda e atravessando pro slide seguinte, grade de pratos com nome, cartão de preço do
menu executivo (dados do executivo.ts) e a linha de margem que corre o carrossel inteiro.
8 slides 1080x1440 em panorama. Gerar: python3 scarpetta-grande.py && node ../render.mjs scarpetta-grande.html saida 1080 1440 8 panorama"""

N, W, H = 8, 1080, 1440
X = lambda n, x=0: (n - 1) * W + x
C = "../../elementos/clientes/scarpetta/"
F = C + "fotos/"
VERDE, NOITE, PAPEL, CREME, MANJ, POMO = "#0f3d2c", "#0a2b1f", "#f6f0df", "#efe5c8", "#a9c99a", "#c4362b"
FUNDO = {1: "foto", 2: PAPEL, 3: VERDE, 4: PAPEL, 5: NOITE, 6: PAPEL, 7: "foto", 8: "foto"}

CSS = r'''
* { box-sizing:border-box; margin:0; padding:0; }
body { width:8640px; height:1440px; overflow:hidden; position:relative; font-family:"Inter Tight",sans-serif; }
.a { position:absolute; }
.bg { top:0; width:1080px; height:1440px; }
.bg img { width:100%; height:100%; object-fit:cover; display:block; }
.linhas { top:0; width:1080px; height:1440px; background:repeating-linear-gradient(180deg, transparent 0 63px, rgba(15,61,44,.08) 63px 64px); }
.top, .pe { font-size:26px; font-weight:500; letter-spacing:-.01em; z-index:6; }
.h { font-family:"Fraunces",serif; font-weight:600; line-height:.9; letter-spacing:-.035em; z-index:5; }
.h i { font-weight:400; }
.it { font-family:"Pinyon Script",cursive; line-height:1; z-index:5; }
.p { font-size:34px; line-height:1.35; letter-spacing:-.015em; z-index:5; }
.cel { border-radius:64px; padding:14px; background:#0b0b0b; z-index:4; box-shadow:0 60px 90px -30px rgba(0,0,0,.55); }
.cel img { display:block; width:100%; border-radius:50px; }
.item { display:flex; align-items:baseline; gap:26px; padding:20px 0; border-top:2px solid rgba(15,61,44,.16); font-size:44px; font-weight:500; letter-spacing:-.03em; }
.item b { font-family:"Fraunces",serif; font-style:italic; font-weight:400; color:#c4362b; font-size:34px; width:44px; }
.ft { overflow:hidden; border-radius:10px; z-index:3; }
.ft img { width:100%; height:100%; object-fit:cover; display:block; }
.ft p { position:absolute; left:20px; right:20px; bottom:18px; color:#fff; font-family:"Fraunces",serif; font-size:32px; line-height:1.05; text-shadow:0 2px 14px rgba(0,0,0,.6); }
.ft::after { content:""; position:absolute; inset:50% 0 0 0; background:linear-gradient(transparent, rgba(0,0,0,.55)); }
.ft p { z-index:2; }
.bolha { background:#fff; color:#111; border-radius:30px 30px 30px 8px; padding:34px 40px; font-size:36px; line-height:1.4; z-index:5; box-shadow:0 40px 60px -30px rgba(0,0,0,.5); }
'''

E = []
# fundos
fotos_fundo = {1: ("forno", "center 35%"), 7: ("interior", "center"), 8: ("pizza-mesa", "center")}
for n, f in FUNDO.items():
    if f == "foto":
        img, pos = fotos_fundo[n]
        src = C + "fotos/" + img + ".webp"
        E.append(f'<div class="a bg" style="left:{X(n)}px"><img src="{src}" style="object-position:{pos}"></div>')
        E.append(f'<div class="a bg" style="left:{X(n)}px;background:linear-gradient(180deg, rgba(10,43,31,.55) 0%, rgba(10,43,31,.25) 35%, rgba(10,43,31,.85) 72%, {NOITE} 100%)"></div>')
    else:
        E.append(f'<div class="a bg" style="left:{X(n)}px;background:{f}"></div>')
        if f == PAPEL:
            E.append(f'<div class="a linhas" style="left:{X(n)}px"></div>')
# a linha de margem corre o carrossel inteiro
E.append(f'<div class="a" style="left:56px;right:0;top:0;bottom:0;width:2px;height:1440px;background:{POMO};opacity:.55;z-index:2"></div>')
for n in range(1, N + 1):
    if n > 1:
        E.append(f'<div class="a" style="left:{X(n,56)}px;top:0;width:2px;height:1440px;background:{POMO};opacity:.55;z-index:2"></div>')
    claro = FUNDO[n] in ("foto", VERDE, NOITE)
    cor = CREME if claro else VERDE
    seta = " · arrasta →" if n < N else ""
    E.append(f'<p class="a top" style="left:{X(n,104)}px;top:56px;color:{cor};opacity:.8">@senerine.dev</p>')
    E.append(f'<p class="a top" style="left:{X(n,604)}px;width:400px;text-align:right;top:56px;color:{cor};opacity:.8">{n:02d} / {N:02d}{seta}</p>')
    E.append(f'<p class="a pe" style="left:{X(n,400 if n == 2 else 104)}px;top:1350px;color:{cor};font-weight:600">Scarpetta Cucina · case</p>')


def cel(src, x, y, w, rot=0):
    return f'<div class="a cel" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg"><img src="{C}{src}"></div>'


def h(n, txt, top, size, cor, left=104, extra=""):
    return f'<h2 class="a h" style="left:{X(n,left)}px;top:{top}px;font-size:{size}px;color:{cor};{extra}">{txt}</h2>'


def it(n, txt, top, cor, size=78, left=104):
    return f'<p class="a it" style="left:{X(n,left)}px;top:{top}px;font-size:{size}px;color:{cor}">{txt}</p>'


def p(n, txt, top, cor, w=840, left=104):
    return f'<p class="a p" style="left:{X(n,left)}px;top:{top}px;width:{w}px;color:{cor}">{txt}</p>'


# 1 · capa: o forno de fundo, título enorme, o celular gigante cortado na borda e entrando no slide 2
E.append(h(1, "Site novo<br><i>no ar.</i>", 860, 168, CREME))
E.append(it(1, "Benvenuti a casa.", 1180, MANJ, 84))
E.append(p(1, "Do Linktree ao site da Scarpetta Cucina.", 1272, CREME, 700))
E.append(cel("site.webp", X(1, 690), 220, 680, 4))

# 2 · tudo num lugar só (o celular termina aqui, à esquerda)
E.append(h(2, "Tudo num<br><i>lugar só.</i>", 170, 150, VERDE, 400))
E.append(it(2, "Tutto in un posto.", 470, POMO, 70, 404))
itens = ["Reserve sua mesa", "O cardápio", "Menu executivo", "Scarpetta em casa", "Eventos", "O salão"]
E.append(f'<div class="a" style="left:{X(2,400)}px;top:590px;width:610px;border-bottom:2px solid rgba(15,61,44,.16);color:{VERDE};z-index:5">'
         + "".join(f'<div class="item"><b>{i+1}</b>{t}</div>' for i, t in enumerate(itens)) + '</div>')
E.append(p(2, 'Antes: um Linktree com<br><s style="text-decoration-color:#c4362b;text-decoration-thickness:4px">sete botões cinza.</s>', 1200, VERDE, 620, 400))

# 3 · reserva: a mensagem que chega no WhatsApp, enorme
E.append(h(3, "A reserva<br><i>chega pronta.</i>", 170, 140, CREME))
E.append(it(3, "Prenota il tuo tavolo.", 460, MANJ, 70))
E.append(cel("reserva.webp", X(3, 620), 640, 420, -4))
E.append(f'''<div class="a bolha" style="left:{X(3,104)}px;top:700px;width:560px;rotate:2deg">Olá! Gostaria de reservar uma mesa no Scarpetta.<br><br>
  <span style="opacity:.75">Dia: sábado<br>Horário: 20h<br>Pessoas: 4<br>Ocasião: Aniversário</span></div>''')
E.append(p(3, "O cliente escolhe e o WhatsApp da casa recebe tudo.", 1150, CREME, 470))

# 4 · cardápio: grade de pratos com nome, como a grade de viagens do Leal
E.append(h(4, "O cardápio<br><i>com foto.</i>", 170, 150, VERDE))
E.append(it(4, "Il menù della casa.", 470, POMO, 70))
pratos = [("fettuccine-garfo", "Fettuccine Alfredo"), ("pizza-parma", "Pizza Parma"), ("risotto-gamberi", "Risotto ai gamberi"),
          ("medaglioni-quadrado", "Medaglioni di filetto"), ("lasagna-detalhe", "Lasagna alla bolognese"), ("budino", "Budino al pistacchio")]
for i, (f, nome) in enumerate(pratos):
    x, y = 104 + (i % 3) * 300, 580 + (i // 3) * 370
    E.append(f'<div class="a ft" style="left:{X(4,x)}px;top:{y}px;width:282px;height:352px"><img src="{F}{f}.webp"><p>{nome}</p></div>')

# 5 · menu executivo: o cartão de preço, como o "escolha seu ritmo" do Leal
E.append(h(5, "Menu<br><i>executivo.</i>", 170, 150, CREME))
E.append(it(5, "Ogni settimana.", 470, MANJ, 70))
etapas = [("Entrada", "Arancini ou bruschetta"), ("Principal", "Carbonara, penne alla vodka ou tilápia"), ("Sobremesa", "Budino al pistacchio ou frutas")]
rows = "".join(f'<div style="display:flex;justify-content:space-between;gap:30px;padding:22px 0;border-top:1px solid rgba(15,61,44,.18)"><span style="font-family:Fraunces;font-style:italic;font-size:34px;color:{POMO}">{a}</span><span style="font-size:30px;text-align:right">{b}</span></div>' for a, b in etapas)
E.append(f'''<div class="a" style="left:{X(5,104)}px;top:590px;width:770px;background:{PAPEL};color:{VERDE};padding:50px 56px;z-index:5;box-shadow:0 50px 80px -30px rgba(0,0,0,.6)">
  <p style="font-size:28px;opacity:.7">Quinta e sexta · entrada, principal e sobremesa</p>
  <p style="font-family:Fraunces;font-weight:600;line-height:.85;margin:20px 0 30px"><span style="font-size:56px;vertical-align:top">R$</span><span style="font-size:220px;letter-spacing:-.04em">99</span></p>
  {rows}</div>''')
E.append(f'<div class="a" style="left:{X(6,-190)}px;top:960px;width:340px;height:340px;border-radius:50%;overflow:hidden;z-index:6;box-shadow:0 40px 60px -20px rgba(0,0,0,.5)"><img src="{F}carbonara-penne.webp" style="width:100%;height:100%;object-fit:cover"></div>')

# 6 · eventos e delivery: dois celulares grandes, como os depoimentos do Leal
E.append(h(6, "Eventos e<br><i>delivery.</i>", 170, 150, VERDE, 240))
E.append(it(6, "Festa e cena a casa.", 470, POMO, 70, 244))
E.append(cel("eventos.webp", X(6, 210), 600, 420, -4))
E.append(f'<div class="a" style="left:{X(6,600)}px;top:720px;width:420px;rotate:5deg;z-index:4;box-shadow:0 50px 80px -30px rgba(0,0,0,.5)"><img src="{C}delivery.webp" style="width:100%;display:block;border-radius:18px"></div>')

# 7 · o salão de fundo
E.append(h(7, "Uma casa<br><i>no meio<br>da mata.</i>", 700, 150, CREME))
E.append(it(7, "Il nostro salone.", 1170, MANJ, 72))
E.append(p(7, "O salão em vídeo, antes do primeiro contato.", 1262, CREME, 760))

# 8 · chamada com a pizza de fundo
E.append(h(8, "O seu link<br>da bio também<br><i>pode virar site.</i>", 660, 118, CREME))
E.append(it(8, "Andiamo?", 1050, MANJ, 90))
E.append(p(8, "Me chama no direct. Quem responde sou eu.", 1172, CREME, 760))
E.append(f'<div class="a" style="left:{X(8,104)}px;top:180px;width:150px;height:150px;border-radius:50%;overflow:hidden;z-index:5"><img src="../../elementos/senerine/leonardo-ponto.webp" style="width:100%;height:100%"></div>')
E.append(f'<p class="a" style="left:{X(8,280)}px;top:214px;font-size:34px;font-weight:600;color:{CREME};z-index:5">Leonardo Senerine</p><p class="a" style="left:{X(8,280)}px;top:262px;font-size:26px;color:{CREME};opacity:.75;z-index:5">senerine.dev · sites e aplicações</p>')

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(E)}<script>document.fonts.ready.then(() => document.body.dataset.ok = 1)</script></body></html>'''
open("scarpetta-grande.html", "w").write(html)
