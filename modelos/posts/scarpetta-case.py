"""Case Scarpetta Cucina no padrão dos primeiros posts (o mesmo do portfólio): fundo escuro da senerine, cartão com
a captura real na cor da casa (a "sala" do cliente), faixa azul com o rótulo, título com o ponto, cabeçalho e rodapé.
Textos da página de proposta do repositório Scarpetta e decisões tiradas do código. A cidade foi apagada do Linktree.
10 slides 1080x1440. Gerar: python3 scarpetta-case.py && node ../render.mjs scarpetta-case.html saida 1080 1440 10"""

M = 72
HEAD = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>
:root { --bg:#1e1d1e; --ink:#f2efea; --muted:rgba(242,239,234,.66); --line:rgba(242,239,234,.16); --blue:#0a63b2; --warm:#d99278; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; font-family:"Inter Tight",sans-serif; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; background:var(--bg); color:var(--ink); }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.02em; }
.kick { left:72px; top:66px; display:flex; align-items:center; gap:14px; font-size:26px; font-weight:500; }
.kick i { width:12px; height:12px; border-radius:50%; background:currentColor; }
.folio { right:72px; top:70px; color:var(--muted); }
.rule { left:72px; right:72px; height:1px; background:var(--line); }
.logo { left:72px; top:1358px; font-size:30px; font-weight:700; letter-spacing:-.05em; }
.logo span { color:#5aa3e8; }
.logo i { display:inline-block; width:8px; height:8px; border-radius:50%; background:#5aa3e8; margin:0 1px 0 2px; }
.swipe { right:72px; top:1364px; color:var(--muted); }
.card { left:72px; right:72px; top:156px; height:720px; border-radius:28px; overflow:hidden; background:#f2efea; color:#1e1d1e; }
.card > * { position:absolute; }
.band { left:20px; right:20px; bottom:20px; height:88px; border-radius:16px; background:var(--blue); color:#fff; display:flex; align-items:center; gap:22px; padding:0 30px; font-size:27px; font-weight:500; letter-spacing:-.02em; z-index:10; }
.band .mono { font-size:18px; letter-spacing:.06em; text-transform:uppercase; opacity:.7; flex:none; }
.t { left:72px; right:72px; top:926px; font-size:88px; font-weight:700; line-height:.98; letter-spacing:-.055em; }
.t em { font-style:normal; color:var(--warm); }
.dot { display:inline-block; width:.15em; height:.15em; border-radius:50%; background:#3d8fe0; margin-left:.04em; }
.p { left:72px; width:820px; top:1140px; font-size:31px; line-height:1.4; color:var(--muted); letter-spacing:-.015em; }
.scr { border-radius:30px; overflow:hidden; box-shadow:0 30px 60px -30px rgba(30,29,30,.55); }
.scr img { position:absolute; left:0; display:block; }
.ui { font-family:"Inter Tight",sans-serif; }
.scr img { width:100%; top:0; }
.cap { font-family:"JetBrains Mono",monospace; font-size:18px; letter-spacing:.06em; text-transform:uppercase; color:#efe5c8; opacity:.75; }
</style></head><body>
'''


def shell(n, kick, folio, inner, swipe="arrasta →"):
    return f'''<section class="s" id="s{n}">
  <p class="kick"><i></i>{kick}</p><p class="folio mono">{folio}</p>
  <div class="rule" style="top:120px"></div>
  {inner}
  <div class="rule" style="top:1326px"></div>
  <p class="logo">senerine<i></i><span>dev</span></p><p class="swipe mono">{swipe}</p>
</section>'''


def detail(n, kick, folio, art, label, bad, title, text, plate="#0f3d2c"):
    return shell(n, kick, folio, f'''<div class="card" style="background:{plate}">{art}
    <div class="band"><span class="mono">{label}</span><span>{bad}</span></div></div>
  <h2 class="t">{title}<span class="dot"></span></h2>
  <p class="p">{text}</p>''')



C = "../../elementos/clientes/scarpetta/"
VERDE, PAPEL, NOITE = "#0f3d2c", "#f6f0df", "#0a2b1f"


def tela(src, left, top=40, w=420, h=600, extra=""):
    """Captura do celular sem moldura, cortada na altura do cartão."""
    return f'<div class="scr" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;{extra}"><img src="{C}{src}"></div>'


def centro(src, w=420, h=600):
    return tela(src, (936 - w) // 2, 40, w, h)


out = [HEAD.replace('href="../../fontes/fontes.css"', 'href="../../fontes/fontes.css"')]

# 1 · capa: o antes e o depois lado a lado no cartão verde
out.append(shell(1, "Case · Scarpetta Cucina", "senerine.dev", f"""<div class="card" style="background:{VERDE}">
    {tela("linktree-sem-cidade.png", 70, 40, 360, 600, "filter:grayscale(1);opacity:.8")}{tela("site.webp", 506, 40, 360, 600)}
    <div class="band"><span class="mono">Cliente real</span><span>Cozinha italiana afetiva.</span></div></div>
  <h2 class="t">Do Linktree ao site<br><em>com a cara da casa</em><span class="dot"></span></h2>
  <p class="p">Como o link da bio da Scarpetta virou um site com cardápio, reserva e o salão.</p>"""))

# 2 · índice: onde cada botão foi morar
items = [("Reservas", "Reserve sua mesa"), ("Menu", "O cardápio"), ("iFood e delivery", "Scarpetta em casa"), ("Eventos", "Eventos com orçamento")]
rows = "".join(f"""<div style="display:grid;grid-template-columns:96px 1fr auto;align-items:baseline;padding:34px 0;border-top:1px solid var(--line)">
  <span class="mono" style="color:#5aa3e8">{i + 1:02d}</span><span style="font-size:44px;font-weight:600;letter-spacing:-.04em">{a}</span><span style="font-size:26px;color:var(--muted)">→ {b}</span></div>""" for i, (a, b) in enumerate(items))
out.append(shell(2, "Índice", "4 trocas", f"""<h2 class="t" style="top:170px">Cada botão do Linktree<br>ganhou <em>um lugar</em><span class="dot"></span></h2>
  <div style="left:72px;right:72px;top:480px;border-bottom:1px solid var(--line)">{rows}</div>
  <p class="p" style="top:1080px">Nada do que o cliente já usava se perdeu. Só mudou de casa.</p>"""))

# 3 · antes
out.append(detail(3, "Antes", "o link da bio", f'<div style="position:absolute;inset:0;background:#e9ebef"></div>' + centro("linktree-sem-cidade.png"), "Antes",
    "Botões cinza, sem prato e sem foto.", "O link da bio<br>era <em>um Linktree</em>",
    "Uma lista igual à de qualquer perfil. Cada toque mandava o cliente pra outro lugar.", PAPEL))

# 4 a 7 · as trocas
trocas = [
    ("Reservas", "reserva.webp", "A reserva<br><em>chega pronta</em>", "O cliente escolhe dia, horário e pessoas, e o WhatsApp da casa recebe a mensagem completa."),
    ("Menu", "cardapio.webp", "O cardápio<br><em>com foto e preço</em>", "Pratos com foto, descrição e preço, separados por categoria, com os destaques da casa no topo."),
    ("Peça pelo iFood · delivery", "delivery.webp", "Os pedidos<br><em>num lugar só</em>", "O iFood e o delivery próprio lado a lado, com as mesmas massas e pizzas."),
    ("Eventos", "eventos.webp", "Eventos<br><em>com orçamento</em>", "As ocasiões, como o menu é servido e o pedido de orçamento por WhatsApp ou e-mail."),
]
for i, (de, img, t, p) in enumerate(trocas):
    arte = (tela(img, 118, 120, 700, 538) if img == "delivery.webp" else centro(img))
    out.append(detail(4 + i, "Depois", f"{i + 1:02d} / 04", arte, "No Linktree", f"o botão “{de}”", t, p))

# 8 · o que o linktree não mostrava
out.append(detail(8, "Depois", "bônus", tela("executivo.webp", 70, 40, 380, 600) + tela("salao.webp", 486, 40, 380, 600), "Antes",
    "Nenhum prato, nenhuma foto do salão.", "O prato, o preço<br><em>e o salão</em>",
    "O menu executivo da semana e o salão no meio da mata, antes do primeiro contato.", NOITE))

# 9 · ficha técnica e decisões, como nos cases do portfólio
dec = ["A reserva monta a mensagem pronta pro WhatsApp da casa.", "Aviso de aberto ou fechado agora, turno por turno.",
       "Fotos em três tamanhos, leves no celular.", "Capa de link própria pra quando o site é compartilhado."]
rows = "".join(f"""<div style="display:grid;grid-template-columns:96px 1fr;align-items:baseline;padding:30px 0;border-top:1px solid rgba(239,229,200,.22)">
  <span class="mono" style="color:#a9c99a">{i + 1:02d}</span><span style="font-size:34px;font-weight:600;letter-spacing:-.03em;line-height:1.2">{t}</span></div>""" for i, t in enumerate(dec))
out.append(shell(9, "Ficha técnica", "Scarpetta", f"""<div style="left:72px;right:72px;top:156px;height:1130px;border-radius:28px;background:{VERDE};color:#efe5c8;padding:60px 56px">
    <p class="mono" style="color:#a9c99a;letter-spacing:.06em;text-transform:uppercase">React · TypeScript · Vite · Motion</p>
    <h2 style="margin-top:26px;font-size:80px;font-weight:700;line-height:.98;letter-spacing:-.055em">Decisões<br>do projeto<span class="dot"></span></h2>
    <div style="margin-top:50px;border-bottom:1px solid rgba(239,229,200,.22)">{rows}</div></div>"""))

# 10 · contato, como o bloco do site
out.append(shell(10, "Contato", "senerine.dev", """<img src="../../elementos/senerine/leonardo-ponto.webp" style="left:72px;top:250px;width:168px;height:168px;border-radius:50%">
  <p style="left:268px;top:300px;font-size:30px;font-weight:600;letter-spacing:-.03em">Leonardo Senerine</p><p class="mono" style="left:268px;top:344px;color:var(--muted)">quem faz o senerine.dev</p>
  <h2 class="t" style="top:500px;font-size:96px">O seu link da bio<br>também pode<br><em>virar site</em><span class="dot"></span></h2>
  <p class="p" style="top:860px">Me conta da marca e do que ela precisa.<br>Quem responde sou eu.</p>""", swipe="salva esse"))

out.append("</body></html>")
open("scarpetta-case.html", "w").write("".join(out))
print(len(out) - 2, "slides")
