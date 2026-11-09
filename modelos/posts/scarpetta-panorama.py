"""Case Scarpetta Cucina em panorama: 9 slides 1080x1440 num canvas só, fundo verde da casa contínuo,
e o computador, os celulares e os pratos atravessando de um slide pro outro. O site aparece em ângulos diferentes
(computador inclinado, janelas giradas, celular encostado na emenda). Estrutura do portfólio: rótulo e fólio,
título com o ponto, régua e rodapé, só que as réguas correm o carrossel inteiro.
Gerar: python3 scarpetta-panorama.py && node ../render.mjs scarpetta-panorama.html saida 1080 1440 9 panorama"""

N, W, H = 9, 1080, 1440
X = lambda n, x=0: (n - 1) * W + x
C = "../../elementos/clientes/scarpetta/"

CSS = r'''
:root { --verde:#0f3d2c; --noite:#0a2b1f; --creme:#efe5c8; --manj:#a9c99a; --warm:#d99278; --muted:rgba(239,229,200,.7); --line:rgba(239,229,200,.18); }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:9720px; height:1440px; overflow:hidden; position:relative; font-family:"Inter Tight",sans-serif; color:var(--creme);
  background:radial-gradient(1400px 900px at 1000px 300px, #14513a, transparent 70%), radial-gradient(1600px 1000px at 4800px 1100px, #134a35, transparent 70%),
             radial-gradient(1400px 900px at 8200px 400px, #14513a, transparent 70%), linear-gradient(90deg, #0f3d2c, #0a2b1f 50%, #0f3d2c); }
.a { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.02em; }
.kick { top:66px; display:flex; align-items:center; gap:14px; font-size:26px; font-weight:500; }
.kick i { width:12px; height:12px; border-radius:50%; background:currentColor; }
.folio { top:70px; width:400px; text-align:right; color:var(--muted); }
.logo { top:1358px; font-size:30px; font-weight:700; letter-spacing:-.05em; }
.logo span { color:#7cbcf2; } .logo i { display:inline-block; width:8px; height:8px; border-radius:50%; background:#7cbcf2; margin:0 1px 0 2px; }
.swipe { top:1364px; width:300px; text-align:right; color:var(--muted); }
.t { font-size:92px; font-weight:700; line-height:.98; letter-spacing:-.055em; z-index:4; }
.t em { font-style:normal; color:var(--warm); }
.t .sc { font-family:"Pinyon Script",cursive; font-weight:400; letter-spacing:0; font-size:1.25em; color:var(--creme); }
.dot { display:inline-block; width:.15em; height:.15em; border-radius:50%; background:#3d8fe0; margin-left:.04em; }
.p { width:560px; font-size:30px; line-height:1.4; color:var(--muted); letter-spacing:-.015em; z-index:4; }
.cena { perspective:1800px; z-index:3; }
.laptop .tela { background:#0b0b0b; border-radius:22px 22px 6px 6px; padding:16px 16px 20px; outline:2px solid rgba(255,255,255,.08); }
.laptop .tela img { display:block; width:100%; border-radius:6px; }
.laptop .base { height:30px; margin:0 -56px; border-radius:2px 2px 20px 20px; background:linear-gradient(#d3d6da,#8b8f95); position:relative; }
.laptop .base::before { content:""; position:absolute; left:50%; top:0; width:170px; height:10px; margin-left:-85px; border-radius:0 0 10px 10px; background:#7a7e84; }
.jan { border-radius:16px; overflow:hidden; background:#0b0b0b; outline:2px solid rgba(255,255,255,.08); }
.jan .barra { height:44px; background:#161616; display:flex; align-items:center; gap:10px; padding:0 18px; }
.jan .barra i { width:12px; height:12px; border-radius:50%; background:#3a3a3a; }
.jan img { display:block; width:100%; }
.cel { border-radius:46px; padding:10px; background:#0b0b0b; outline:2px solid rgba(255,255,255,.1); z-index:5; }
.cel img { display:block; width:100%; border-radius:37px; }
.prato { border-radius:50%; overflow:hidden; z-index:2; }
.prato img { width:100%; height:100%; object-fit:cover; display:block; }
.sombra { filter:drop-shadow(0 50px 60px rgba(0,0,0,.45)); }
.etq { font-family:"JetBrains Mono",monospace; font-size:20px; letter-spacing:.06em; text-transform:uppercase; padding:12px 18px; border-radius:10px; background:#0a63b2; color:#fff; z-index:6; }
.etq b { font-weight:400; opacity:.7; margin-right:12px; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:screen; filter:invert(1); opacity:.06;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
'''


def frame(n, kick, folio, swipe="arrasta →"):
    return (f'<p class="a kick" style="left:{X(n,72)}px"><i></i>{kick}</p><p class="a folio mono" style="left:{X(n,608)}px">{folio}</p>'
            f'<p class="a logo" style="left:{X(n,72)}px">senerine<i></i><span>dev</span></p><p class="a swipe mono" style="left:{X(n,708)}px">{swipe}</p>')


def texto(n, t, p=None, top=170, ptop=None, left=72):
    h = f'<h2 class="a t" style="left:{X(n,left)}px;top:{top}px">{t}<span class="dot"></span></h2>'
    if p:
        h += f'<p class="a p" style="left:{X(n,left)}px;top:{ptop}px">{p}</p>'
    return h


def laptop(img, x, y, w, rot=0, tilt=0):
    return (f'<div class="a cena sombra" style="left:{x}px;top:{y}px;width:{w}px"><div class="laptop" style="transform:rotateY({rot}deg) rotateX({tilt}deg)">'
            f'<div class="tela"><img src="{C}desktop-{img}.jpg"></div><div class="base"></div></div></div>')


def janela(img, x, y, w, rot=0, crop=None):
    st = f"height:{crop}px;object-fit:cover;object-position:top" if crop else ""
    return (f'<div class="a cena sombra" style="left:{x}px;top:{y}px;width:{w}px"><div class="jan" style="transform:rotateY({rot}deg)">'
            f'<div class="barra"><i></i><i></i><i></i></div><img src="{C}desktop-{img}.jpg" style="{st}"></div></div>')


def cel(src, x, y, w, rot=0, extra=""):
    return f'<div class="a cel sombra" style="left:{x}px;top:{y}px;width:{w}px;rotate:{rot}deg;{extra}"><img src="{C}{src}"></div>'


def prato(foto, x, y, d):
    return f'<div class="a prato sombra" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px"><img src="{C}fotos/{foto}.webp"></div>'


def etq(x, y, a, b):
    return f'<p class="a etq" style="left:{x}px;top:{y}px"><b>{a}</b>{b}</p>'


E = []
# réguas que correm o carrossel inteiro
E.append(f'<div class="a" style="left:72px;right:72px;top:120px;height:1px;background:var(--line)"></div>')
E.append(f'<div class="a" style="left:72px;right:72px;top:1326px;height:1px;background:var(--line)"></div>')

# 1 · capa: o computador inclinado atravessa pro slide 2; a pizza entra pela borda
E.append(frame(1, "Case · Scarpetta Cucina", "senerine.dev"))
E.append(texto(1, 'Do Linktree<br>ao site da<br><span class="sc">Scarpetta</span>', "Como o link da bio virou um site com cardápio, reserva e o salão.", 170, 470))
E.append(prato("pizza-mesa", X(1, -230), 700, 500))
E.append(laptop("topo", X(1, 560), 520, 1180, -14, 4))
E.append(etq(X(1, 640), 470, "Depois", "o site no ar"))

# 2 · antes: o linktree cinza, do lado do fim do computador
E.append(frame(2, "Antes", "o link da bio"))
E.append(texto(2, 'O link da bio<br>era <em>um Linktree</em>', "Botões cinza, sem prato e sem foto. Cada toque mandava o cliente pra outro lugar.", 170, 400, 380))
E.append(cel("linktree-sem-cidade.png", X(2, 760), 640, 260, 6, "filter:grayscale(1)"))
E.append(etq(X(2, 700), 1180, "Antes", "linktr.ee"))

# 3 · reserva: janela girada pra direita; o celular da reserva fica na emenda 3|4
E.append(frame(3, "Depois", "01 / 04"))
E.append(texto(3, 'A reserva<br><em>chega pronta</em>', "Dia, horário e pessoas. O WhatsApp da casa recebe a mensagem completa.", 170, 400))
E.append(janela("reserva", X(3, 60), 620, 900, 10))
E.append(cel("reserva.webp", X(4, -150), 520, 300, -4))
E.append(etq(X(3, 72), 1240, "No Linktree", "“Reservas”"))

# 4 · cardápio: janela girada pro outro lado, recorte do topo; o fettuccine na emenda 4|5
E.append(frame(4, "Depois", "02 / 04"))
E.append(texto(4, 'O cardápio<br><em>com foto e preço</em>', "Pratos com foto, descrição e preço, separados por categoria.", 170, 400, 260))
E.append(janela("cardapio", X(4, 200), 640, 820, -10, 520))
E.append(cel("cardapio.webp", X(5, -130), 600, 260, 5))
E.append(etq(X(4, 260), 1240, "No Linktree", "“Menu”"))

# 5 · pedidos: o computador de frente, a pizza de pepperoni cortada na emenda 5|6
E.append(frame(5, "Depois", "03 / 04"))
E.append(texto(5, 'Os pedidos<br><em>num lugar só</em>', "O iFood e o delivery próprio lado a lado.", 170, 400, 200))
E.append(laptop("delivery", X(5, 200), 560, 760, 0, 0))
E.append(prato("pizza-peperoni-detalhe", X(6, -260), 820, 520))
E.append(etq(X(5, 200), 1240, "No Linktree", "“Peça pelo iFood”"))

# 6 · eventos: janela girada; o celular dos eventos na emenda 6|7
E.append(frame(6, "Depois", "04 / 04"))
E.append(texto(6, 'Eventos<br><em>com orçamento</em>', "As ocasiões, como o menu é servido e o pedido de orçamento.", 170, 400, 300))
E.append(janela("eventos", X(6, 280), 620, 760, 10))
E.append(cel("eventos.webp", X(7, -140), 560, 280, -5))
E.append(etq(X(6, 300), 1240, "No Linktree", "“Eventos”"))

# 7 · o salão: computador inclinado pro outro lado, o forno de fundo
E.append(frame(7, "Bônus", "o que o Linktree não mostrava"))
E.append(texto(7, 'O salão<br><em>no meio da mata</em>', "As fotos do lugar, o menu da semana e os pratos, antes do primeiro contato.", 170, 400, 220))
E.append(f'<div class="a" style="left:{X(7,380)}px;top:560px;width:700px;height:740px;border-radius:28px;overflow:hidden;z-index:1"><img src="{C}fotos/forno.webp" style="width:100%;height:100%;object-fit:cover;opacity:.85"></div>')
E.append(laptop("salao", X(7, 120), 700, 860, 12, 4))

# 8 · ficha técnica; o risoto atravessa pro contato
dec = ["A reserva monta a mensagem pronta pro WhatsApp da casa.", "Aviso de aberto ou fechado agora, turno por turno.",
       "Fotos em três tamanhos, leves no celular.", "Capa de link própria pra quando o site é compartilhado."]
rows = "".join(f'<div style="display:grid;grid-template-columns:80px 1fr;align-items:baseline;padding:26px 0;border-top:1px solid var(--line)"><span class="mono" style="color:var(--manj)">{i+1:02d}</span><span style="font-size:32px;font-weight:600;letter-spacing:-.03em;line-height:1.2">{t}</span></div>' for i, t in enumerate(dec))
E.append(frame(8, "Ficha técnica", "Scarpetta"))
E.append(texto(8, 'Decisões<br><em>do projeto</em>', None, 170))
E.append(f'<p class="a mono" style="left:{X(8,72)}px;top:420px;color:var(--manj);text-transform:uppercase;letter-spacing:.06em">React · TypeScript · Vite · Motion</p>')
E.append(f'<div class="a" style="left:{X(8,72)}px;top:480px;width:760px;border-bottom:1px solid var(--line);z-index:4">{rows}</div>')
E.append(prato("risotto-gamberi", X(9, -230), 860, 460))

# 9 · contato
E.append(frame(9, "Contato", "senerine.dev", swipe="salva esse"))
E.append(f'<img class="a" src="../../elementos/senerine/leonardo-ponto.webp" style="left:{X(9,320)}px;top:230px;width:150px;height:150px;border-radius:50%;z-index:4">')
E.append(f'<p class="a" style="left:{X(9,500)}px;top:270px;font-size:30px;font-weight:600;letter-spacing:-.03em">Leonardo Senerine</p><p class="a mono" style="left:{X(9,500)}px;top:314px;color:var(--muted)">quem faz o senerine.dev</p>')
E.append(texto(9, 'O seu link da bio<br>também pode<br><em>virar site</em>', "Me conta da marca e do que ela precisa. Quem responde sou eu.", 470, 790, 320))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(E)}<div class="a grain"></div><script>document.fonts.ready.then(() => document.body.dataset.ok = 1)</script></body></html>'''
open("scarpetta-panorama.html", "w").write(html)
