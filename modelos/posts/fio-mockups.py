"""Carrossel panorâmico "link na bio": 7 slides 1080x1350 lado a lado num canvas só (7560 px).
O fio do rodapé é um traço azul contínuo que atravessa todos os slides (o "link"), com o ponto
andando por ele como indicador de progresso, e termina no ponto grande com a foto do contato."""

N, W, H = 7, 1080, 1350
X = lambda n, x=0: (n - 1) * W + x

CSS = r'''
:root { --bg:#1e1d1e; --ink:#f2efea; --muted:rgba(242,239,234,.66); --line:rgba(242,239,234,.16); --blue:#0a63b2; --sky:#4aa3ea; --warm:#d99278; --paper:#f2efea; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:7560px; height:1350px; background:var(--bg); font-family:"Inter Tight",sans-serif; color:var(--ink); position:relative; overflow:hidden; }
.a { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.02em; }
.kick { top:66px; display:flex; align-items:center; gap:14px; font-size:26px; font-weight:500; }
.kick i { width:12px; height:12px; border-radius:50%; background:currentColor; }
.folio { top:70px; color:var(--muted); width:300px; text-align:right; }
.rule { height:1px; width:936px; top:120px; background:var(--line); }
.logo { top:1268px; font-size:30px; font-weight:700; letter-spacing:-.05em; }
.logo span { color:#5aa3e8; }
.logo i { display:inline-block; width:8px; height:8px; border-radius:50%; background:#5aa3e8; margin:0 1px 0 2px; }
.swipe { top:1274px; color:var(--muted); width:300px; text-align:right; }
.card { top:156px; width:936px; height:640px; border-radius:28px; overflow:hidden; background:var(--paper); color:#1e1d1e; }
.card > * { position:absolute; }
.t { top:846px; width:936px; font-size:88px; font-weight:700; line-height:.98; letter-spacing:-.055em; }
.t em { font-style:normal; color:var(--warm); }
.dot { display:inline-block; width:.15em; height:.15em; border-radius:50%; background:#3d8fe0; margin-left:.04em; }
.p { top:1052px; width:820px; font-size:31px; line-height:1.4; color:var(--muted); letter-spacing:-.015em; }
/* página de links genérica (cinza, igual pra todo mundo) */
.lp { background:#e9e7e3; border-radius:30px; overflow:hidden; box-shadow:0 30px 60px -30px rgba(30,29,30,.5), 0 0 0 1px rgba(30,29,30,.08); display:flex; flex-direction:column; align-items:center; }
.lp .av { border-radius:50%; background:#c9c6c0; flex:none; }
.lp .hd { font-weight:600; color:#4a4848; letter-spacing:-.02em; }
.lp .pl { width:84%; border-radius:999px; background:#fff; color:#5b5958; font-weight:500; display:grid; place-items:center; letter-spacing:-.01em; box-shadow:0 1px 0 rgba(0,0,0,.06); flex:none; }
.lp .ft { margin-top:auto; color:#9a9894; font-family:"JetBrains Mono",monospace; letter-spacing:.04em; }
.node { height:76px; border-radius:18px; display:flex; align-items:center; padding:0 26px; font-size:28px; font-weight:600; letter-spacing:-.03em; white-space:nowrap; }
'''


def lp(handle, w, h, links=("Cardápio", "WhatsApp", "Instagram", "Localização", "Avaliações"), s=1.0):
    pl = ''.join(f'<div class="pl" style="height:{58*s:.0f}px;font-size:{21*s:.0f}px;margin-top:{14*s:.0f}px">{l}</div>' for l in links)
    return f'''<div class="lp" style="width:{w}px;height:{h}px;padding:{38*s:.0f}px 0 {20*s:.0f}px">
      <div class="av" style="width:{84*s:.0f}px;height:{84*s:.0f}px"></div>
      <p class="hd" style="font-size:{22*s:.0f}px;margin:{14*s:.0f}px 0 {10*s:.0f}px">{handle}</p>{pl}
      <p class="ft" style="font-size:{14*s:.0f}px">linktr.ee</p></div>'''


def frame(n, kick, folio, swipe="arrasta →"):
    return f'''<p class="a kick" style="left:{X(n,72)}px"><i></i>{kick}</p><p class="a folio mono" style="left:{X(n,708)}px">{folio}</p>
<div class="a rule" style="left:{X(n,72)}px"></div>
<p class="a logo" style="left:{X(n,72)}px">senerine<i></i><span>dev</span></p>
<p class="a swipe mono" style="left:{X(n,708)}px">{swipe}</p>'''


def text(n, title, p, top=846, ptop=1052):
    return f'''<h2 class="a t" style="left:{X(n,72)}px;top:{top}px">{title}{'' if title.endswith('?</em>') else '<span class="dot"></span>'}</h2>
<p class="a p" style="left:{X(n,72)}px;top:{ptop}px">{p}</p>'''


def card(n, inner, bg="var(--paper)", color="#1e1d1e"):
    return f'<div class="a card" style="left:{X(n,72)}px;background:{bg};color:{color}">{inner}</div>'


out = []

# 1 · capa: a bio com o link e a página de links que ele abre
out.append(frame(1, "Link na bio", "01 / 07"))
out.append(card(1, f'''
  <div style="left:56px;top:62px;width:120px;height:120px;border-radius:50%;background:#d4d1cb"></div>
  <p style="left:56px;top:212px;font-size:44px;font-weight:700;letter-spacing:-.045em">Seu Negócio</p>
  <p style="left:56px;top:270px;width:420px;font-size:28px;line-height:1.35;color:#5b5958;letter-spacing:-.015em">Comida feita com calma.<br>Delivery de terça a domingo.</p>
  <p id="biolink" style="left:56px;top:372px;font-size:30px;font-weight:600;color:#0a63b2;letter-spacing:-.02em;padding:4px 10px;margin-left:-10px;border-radius:8px;background:rgba(217,146,120,.28)">linktr.ee/seunegocio</p>
  <div style="left:540px;top:52px;rotate:4deg">{lp("@seunegocio", 330, 600)}</div>'''))
out.append(text(1, "Seu link na bio leva<br>pra uma página<br><em>que não é sua</em>",
                "Ajuda no começo. Mas tem coisa nele que passa batido.", ptop=1132))

# 2 · o endereço
out.append(frame(2, "O endereço", "02 / 07"))
out.append(card(2, '''
  <p class="mono" style="left:56px;top:62px;font-size:20px;color:#8a8783;text-transform:uppercase;letter-spacing:.08em">O link que você divulga</p>
  <div style="left:56px;top:116px;width:824px;height:120px;border-radius:24px;background:#fff;box-shadow:0 1px 0 rgba(0,0,0,.06);display:flex;align-items:center;padding:0 34px;gap:2px;font-size:54px;font-weight:600;letter-spacing:-.04em">
    <span style="background:rgba(217,146,120,.35);border-radius:10px;padding:0 6px">linktr.ee/</span><span style="color:#8a8783">seunegocio</span></div>
  <p class="mono" style="left:96px;top:252px;font-size:20px;color:#b0674d;text-transform:uppercase;letter-spacing:.08em">↑ o nome que aparece é o deles</p>
  <p class="mono" style="left:56px;top:362px;font-size:20px;color:#8a8783;text-transform:uppercase;letter-spacing:.08em">O link que poderia ser</p>
  <div style="left:56px;top:416px;width:824px;height:120px;border-radius:24px;background:#0a63b2;color:#fff;display:flex;align-items:center;padding:0 34px;font-size:54px;font-weight:600;letter-spacing:-.04em">seunegocio.com.br</div>
  <p class="mono" style="left:96px;top:552px;font-size:20px;color:#0a63b2;text-transform:uppercase;letter-spacing:.08em">↑ o nome que aparece é o seu</p>'''))
out.append(text(2, "O endereço<br>é <em>deles</em>",
                "Cada vez que alguém salva ou compartilha o link, divulga a plataforma. E no plano grátis, a marca dela aparece no rodapé da sua página."))

# 3 · todo mundo igual
names = ["@pizzaria.vila", "@barbearia.jr", "@seunegocio", "@loja.flor", "@doceria.mel"]
fan = ''.join(f'<div style="left:{30 + i*172}px;top:{78 + abs(i-2)*22}px;rotate:{(i-2)*4}deg;z-index:{5-abs(i-2)}">{lp(h, 240, 470, s=.72)}</div>'
              for i, h in enumerate(names))
out.append(frame(3, "A cara", "03 / 07"))
out.append(card(3, fan, bg="#dcd9d3"))
out.append(text(3, "Igual a<br><em>todo mundo</em>",
                "Pizzaria, barbearia e loja de roupa com o mesmo layout e os mesmos botões. Quem clica não sente a sua marca."))

# 4 · o caminho
def row(y, label, nodes, color):
    sep = f'<i style="width:34px;height:2px;background:{color};flex:none"></i>'
    return (f'<p class="mono" style="left:56px;top:{y}px;font-size:20px;color:{color};text-transform:uppercase;letter-spacing:.08em">{label}</p>'
            f'<div style="left:56px;top:{y + 44}px;display:flex;align-items:center;gap:10px">'
            + sep.join(f'<div class="node" style="{st}">{t}</div>' for t, st in nodes) + '</div>')
grey = "background:#fff;color:#5b5958;box-shadow:0 1px 0 rgba(0,0,0,.06)"
blue = "background:#0a63b2;color:#fff"
out.append(frame(4, "O caminho", "04 / 07"))
out.append(card(4, row(70, "Com Linktree · 4 telas", [("Bio", grey), ("Lista de links", grey), ("Cardápio", grey), ("WhatsApp", grey)], "#8a8783")
           + row(250, "Com página própria · 3 telas", [("Bio", grey), ("Cardápio com botão", blue), ("WhatsApp", grey)], "#0a63b2")
           + '<div style="left:56px;right:56px;top:470px;height:1px;background:rgba(30,29,30,.14)"></div>'
           + '<p style="left:56px;top:504px;width:800px;font-size:34px;line-height:1.3;font-weight:600;letter-spacing:-.035em">Tirar uma tela do meio é tirar<br>um motivo pra desistir.</p>'))
out.append(text(4, "Uma tela<br><em>a mais</em>",
                "A pessoa sai da bio, cai numa lista, escolhe um botão e só então chega no que queria. Cada tela no caminho é uma chance de ela ir embora."))

# 5 · sendo justo
pros = [("01", "É grátis."), ("02", "Fica pronto em minutos."), ("03", "Resolve bem no começo.")]
lines = ''.join(f'''<div style="left:56px;right:56px;top:{70 + i*150}px;height:150px;border-top:1px solid rgba(255,255,255,.22);display:flex;align-items:center;gap:40px">
  <span class="mono" style="font-size:22px;opacity:.7">{a}</span><span style="font-size:58px;font-weight:700;letter-spacing:-.05em">{b}</span></div>''' for i, (a, b) in enumerate(pros))
out.append(frame(5, "Sendo justo", "05 / 07"))
out.append(card(5, lines + '<div style="left:56px;right:56px;top:520px;height:1px;background:rgba(255,255,255,.22)"></div>', bg="#0a63b2", color="#fff"))
out.append(text(5, "Linktree não<br>é <em>vilão</em>",
                "O problema é continuar nele quando o negócio já tem cara própria e o link da bio virou a porta de entrada principal."))

# 6 · no lugar: página própria (uma marca inventada, só pra mostrar a diferença)
own = '''<div style="left:300px;top:44px;width:336px;height:640px;border-radius:30px;overflow:hidden;background:#24302a;color:#efe6d6;box-shadow:0 30px 60px -30px rgba(30,29,30,.6)">
  <div style="position:absolute;left:14px;right:14px;top:14px;height:44px;border-radius:12px;background:rgba(239,230,214,.12);display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-size:15px;letter-spacing:.02em">seunegocio.com.br/links</div>
  <p style="position:absolute;left:28px;top:96px;font-family:Georgia,serif;font-size:50px;line-height:.95;letter-spacing:-.03em">Seu<br>Negócio<span style="color:#d99278">.</span></p>
  <p style="position:absolute;left:28px;top:212px;width:280px;font-size:18px;line-height:1.4;opacity:.75">Comida feita com calma. Delivery de terça a domingo.</p>
  <div style="position:absolute;left:28px;right:28px;top:290px;height:72px;border-radius:14px;background:#d99278;color:#24302a;display:flex;align-items:center;justify-content:space-between;padding:0 22px;font-size:21px;font-weight:700;letter-spacing:-.02em">Pedir pelo WhatsApp <span>→</span></div>
  ''' + ''.join(f'''<div style="position:absolute;left:28px;right:28px;top:{392 + i*58}px;height:58px;border-top:1px solid rgba(239,230,214,.18);display:flex;align-items:center;justify-content:space-between;font-size:19px;font-weight:500">{t}<span style="opacity:.6">↗</span></div>''' for i, t in enumerate(["Cardápio", "Como chegar", "Horários"])) + '''
</div>'''
notes = [(56, 66, "01", "Seu domínio"), (56, 306, "02", "O botão que<br>importa primeiro"), (676, 120, "03", "Suas cores<br>e sua letra"), (676, 470, "04", "Os cliques no<br>seu painel")]
nt = ''.join(f'''<div style="left:{x}px;top:{y}px;width:210px"><p class="mono" style="font-size:20px;color:#0a63b2">{a}</p>
  <p style="margin-top:8px;font-size:28px;font-weight:600;line-height:1.1;letter-spacing:-.035em">{b}</p></div>''' for x, y, a, b in notes)
out.append(frame(6, "No lugar", "06 / 07"))
out.append(card(6, own + nt))
out.append(text(6, "Uma página<br>com a <em>sua cara</em>",
                "No seu domínio, com as suas cores, o botão que mais importa em primeiro e os cliques medidos no seu próprio painel."))

# 7 · chamada: o fio termina no ponto com a foto
out.append(frame(7, "Senerine.dev", "07 / 07", swipe="salva pra depois"))
out.append(f'''<div class="a" style="left:{X(7,330)}px;top:170px;width:620px;height:620px;border-radius:50%;overflow:hidden;background:#0a63b2;box-shadow:0 0 0 14px rgba(74,163,234,.14),0 0 120px rgba(74,163,234,.35)">
  <img src="../../elementos/tinta/leonardo-ponto.webp" style="width:100%;height:100%;display:block"></div>''')
out.append(text(7, "Quer trocar o<br>link da sua <em>bio?</em>",
                "Faço a sua página de links ou o site completo, no seu domínio. Me chama no direct ou em senerine.dev."))

# o fio: sai do link da bio (slide 1), desce pela margem direita, corre no rodapé por todos os slides
# e sobe no último até o ponto grande
y = 1236
path = (f"M {X(1,440)} 550 C {X(1,500)} 550, {X(1,500)} 590, {X(1,500)} 640 L {X(1,500)} 781 Q {X(1,500)} 821, {X(1,540)} 821 "
        f"L {X(1,1000)} 821 Q {X(1,1040)} 821, {X(1,1040)} 861 L {X(1,1040)} {y-40} Q {X(1,1040)} {y}, {X(1,1080)} {y} "
        f"L {X(7,1000)} {y} Q {X(7,1040)} {y}, {X(7,1040)} {y-40} L {X(7,1040)} 520 Q {X(7,1040)} 480, {X(7,1000)} 480 L {X(7,950)} 480")
dots = ''.join(f'<circle cx="{X(n, 72 + (n-1) * 150)}" cy="{y}" r="11" fill="#4aa3ea" filter="url(#g)"/>' for n in range(2, 7))
out.append(f'''<svg class="a" style="left:0;top:0;z-index:2;pointer-events:none" width="{N*W}" height="{H}" viewBox="0 0 {N*W} {H}">
  <defs><filter id="g" x="-2" y="-2" width="5" height="5"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
  <path d="{path}" fill="none" stroke="#0a63b2" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  {dots}</svg>''')

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{''.join(out)}</body></html>'''
open("lk.html", "w").write(html)
