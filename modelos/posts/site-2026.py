"""Carrossel "ainda vale a pena ter um site em 2026?", no estilo anti design / acid (como o `nada.py`),
com mais elementos desenhados: janela de navegador antiga, página quebrada, ímã, placa de rua,
balões de conversa, alfinete de mapa, adesivos, fita, retícula e código de barras. Sem cabeçalho
nem rodapé. Nenhuma foto: os elementos são desenhados, então nada se repete de outro post.
8 slides 1080x1440. Gerar: python3 site-2026.py && node ../render.mjs site-2026.html saida 1080 1440 8"""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; --off:#f2efea; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; background:var(--paper); color:var(--ink); }
.s.preto { background:var(--ink); color:var(--off); }
.s.azul { background:var(--blue); color:var(--off); }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:24px; letter-spacing:.04em; text-transform:uppercase; line-height:1.35; z-index:6; }
.giga { font-family:"Anton",sans-serif; text-transform:uppercase; line-height:1.04; letter-spacing:-.02em; white-space:nowrap; z-index:2; transform-origin:0 0; }
.w1 { filter:url(#onda); }
.w2 { filter:url(#derrete); }
.it { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; letter-spacing:-.02em; line-height:1.06; z-index:6; }
.b { color:var(--blue); }
.s.azul .b { color:var(--ink); }
.tx { font-family:"JetBrains Mono",monospace; font-size:27px; line-height:1.45; letter-spacing:-.01em; z-index:6; border-top:3px solid currentColor; padding-top:16px; }
.tag { font-family:"Anton",sans-serif; text-transform:uppercase; font-size:50px; line-height:1; padding:14px 22px 10px; background:var(--ink); color:var(--off); z-index:7; }
.s.preto .tag { background:var(--off); color:var(--ink); }
.dot { border-radius:50%; background:var(--blue); z-index:4; }
.s.azul .dot { background:var(--off); }
.svg { left:0; top:0; z-index:5; pointer-events:none; overflow:visible; }
.tape { width:170px; height:48px; background:rgba(236,232,220,.82); z-index:8; }
.half { z-index:1; background-image:radial-gradient(currentColor 34%, transparent 36%); background-size:20px 20px;
  -webkit-mask-image:radial-gradient(circle, #000 30%, transparent 70%); mask-image:radial-gradient(circle, #000 30%, transparent 70%); }
.barcode { height:90px; z-index:6; background:repeating-linear-gradient(90deg, currentColor 0 4px, transparent 4px 7px, currentColor 7px 9px, transparent 9px 15px, currentColor 15px 21px, transparent 21px 24px); }
/* janela de navegador antiga */
.win { border:4px solid var(--ink); background:var(--off); color:var(--ink); z-index:4; }
.win .bar { height:54px; border-bottom:4px solid var(--ink); display:flex; align-items:center; gap:12px; padding:0 16px; font-family:"JetBrains Mono",monospace; font-size:22px; }
.win .bar i { width:22px; height:22px; border:3px solid var(--ink); display:block; }
.win .bar span { margin-left:12px; border:3px solid var(--ink); padding:2px 14px; flex:1; }
.obras { height:70px; background:repeating-linear-gradient(-45deg, var(--ink) 0 26px, var(--blue) 26px 52px); }
.cont { font-family:"JetBrains Mono",monospace; font-size:24px; display:inline-flex; gap:4px; }
.cont b { background:var(--ink); color:var(--off); padding:4px 8px; font-weight:700; }
/* balões e busca */
.bal { border:4px solid currentColor; padding:20px 26px; font-family:"Inter Tight",sans-serif; font-weight:600; font-size:36px; line-height:1.2; letter-spacing:-.02em; z-index:6; }
.bal small { display:block; font-family:"JetBrains Mono",monospace; font-weight:400; font-size:22px; letter-spacing:.04em; text-transform:uppercase; margin-bottom:8px; opacity:.75; }
.busca { border:4px solid currentColor; height:96px; display:flex; align-items:center; gap:20px; padding:0 28px; font-family:"Inter Tight",sans-serif; font-weight:600; font-size:38px; letter-spacing:-.02em; z-index:6; }
/* placa de rua */
.placa { background:var(--blue); color:var(--off); border:6px solid var(--blue); outline:5px solid var(--off); outline-offset:-18px; padding:34px 44px 30px; z-index:6; font-family:"Inter Tight",sans-serif; font-weight:800; letter-spacing:-.03em; text-transform:uppercase; line-height:1; }
.placa small { display:block; font-weight:600; font-size:30px; letter-spacing:0; margin-top:14px; text-transform:none; }
.zebra { height:150px; z-index:1; background:repeating-linear-gradient(90deg, currentColor 0 70px, transparent 70px 130px); }
.aberto { border:4px solid var(--ink); background:var(--off); color:var(--ink); font-family:"Anton",sans-serif; text-transform:uppercase; font-size:56px; padding:16px 30px 10px; z-index:6; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.32;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.s.preto .grain, .s.azul .grain { mix-blend-mode:screen; opacity:.16;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
'''

SVG_DEFS = '''<svg width="0" height="0" style="position:absolute"><defs>
  <filter id="onda" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.0025 0.006" numOctaves="1" seed="4"/><feDisplacementMap in="SourceGraphic" scale="55" xChannelSelector="R" yChannelSelector="G"/></filter>
  <filter id="derrete" x="-10%" y="-10%" width="120%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.006 0.0012" numOctaves="1" seed="9"/><feDisplacementMap in="SourceGraphic" scale="90" xChannelSelector="B" yChannelSelector="R"/></filter>
</defs></svg>'''

AZUL, TINTA, OFF = "#0a63b2", "#121112", "#f2efea"


def svg(*partes):
    return f'<svg class="svg" width="1080" height="1440">{"".join(partes)}</svg>'


def burst(cx, cy, r, texto, rot=-12, fundo=AZUL, cor=OFF, pontas=14, fs=34):
    """Adesivo em estrela com texto (o "NOVO!" das páginas antigas)."""
    import math
    pts = []
    for i in range(pontas * 2):
        rr = r if i % 2 == 0 else r * .78
        a = math.pi * i / pontas
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    linhas = texto.split("|")
    tsp = "".join(f'<tspan x="{cx}" dy="{0 if k == 0 else fs * 1.05}">{t}</tspan>' for k, t in enumerate(linhas))
    y0 = cy - (len(linhas) - 1) * fs * .52 + fs * .36
    return (f'<g transform="rotate({rot} {cx} {cy})"><polygon points="{" ".join(pts)}" fill="{fundo}"/>'
            f'<text x="{cx}" y="{y0}" text-anchor="middle" font-family="Anton" font-size="{fs}" fill="{cor}" '
            f'style="text-transform:uppercase">{tsp}</text></g>')


def circulo(cx, cy, rx, ry, cor=AZUL, w=8):
    """Círculo à mão: duas voltas que não fecham no mesmo lugar."""
    return (f'<path d="M{cx - rx},{cy + 6} C{cx - rx},{cy - ry - 10} {cx + rx + 14},{cy - ry} {cx + rx},{cy + 4} '
            f'S{cx - rx + 30},{cy + ry + 12} {cx - rx - 8},{cy - 14}" fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round"/>')


def seta(x1, y1, x2, y2, cor=AZUL, w=8):
    """Seta à mão, levemente curva."""
    import math
    mx, my = (x1 + x2) / 2 + (y2 - y1) * .18, (y1 + y2) / 2 - (x2 - x1) * .18
    a = math.atan2(y2 - my, x2 - mx)
    h1 = (x2 - 40 * math.cos(a - .5), y2 - 40 * math.sin(a - .5))
    h2 = (x2 - 40 * math.cos(a + .5), y2 - 40 * math.sin(a + .5))
    return (f'<path d="M{x1},{y1} Q{mx},{my} {x2},{y2} M{h1[0]:.0f},{h1[1]:.0f} L{x2},{y2} L{h2[0]:.0f},{h2[1]:.0f}" '
            f'fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def xis(cx, cy, r, cor=AZUL, w=10):
    return (f'<path d="M{cx - r},{cy - r + 6} L{cx + r},{cy + r} M{cx + r - 4},{cy - r} L{cx - r + 4},{cy + r - 4}" '
            f'stroke="{cor}" stroke-width="{w}" stroke-linecap="round"/>')


def cursor(x, y, s=1.0, rot=-8):
    p = "0,0 0,64 16,50 28,76 40,70 28,46 48,46"
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><polygon points="{p}" fill="{TINTA}" '
            f'stroke="{OFF}" stroke-width="4" stroke-linejoin="round"/></g>')


def risco(pts, cor=AZUL, w=30):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    return f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def slide(n, inner, cls=""):
    return f'''<section class="s {cls}" id="s{n}">
  {inner}
  <div class="grain"></div>
</section>'''


S = []

# 1 · capa: "SITE" gigante derretido, cursor clicando, adesivo de spoiler
S.append(slide(1, f'''
  <p class="it" style="left:64px;top:96px;font-size:80px">Ainda vale a pena<br>ter um</p>
  <h1 class="giga w2" style="left:30px;top:290px;font-size:560px;transform:scaleY(1.22)">site</h1>
  <h1 class="giga w1 b" style="left:64px;top:1030px;font-size:190px">em 2026?</h1>
  <div class="half" style="left:640px;top:60px;width:420px;height:420px;color:var(--blue)"></div>
  {svg(burst(860, 250, 150, "spoiler:|depende|do site", rot=10, fs=40), cursor(800, 900, 1.6), circulo(450, 1150, 400, 120))}
  <div class="barcode" style="left:760px;top:1310px;width:256px"></div>'''))

# 2 · antigamente: janela velha "em construção", contador de visitas, adesivo "NOVO!"
S.append(slide(2, f'''
  <p class="mono" style="left:64px;top:96px">antigamente</p>
  <h1 class="giga w1" style="left:64px;top:140px;font-size:185px">todo mundo<br>fazia <span class="b">por</span><br><span class="b">fazer.</span></h1>
  <div class="win" style="left:420px;top:790px;width:600px;height:400px;rotate:4deg">
    <div class="bar"><i></i><i></i><span>www.meusite.com.br</span></div>
    <div class="obras" style="position:absolute;left:0;right:0;top:110px"></div>
    <p style="position:absolute;left:30px;top:200px;font-family:'Anton';font-size:64px;text-transform:uppercase">em construção</p>
    <p class="cont" style="position:absolute;left:30px;top:300px">visitas: <b>0</b><b>0</b><b>0</b><b>0</b><b>0</b></p>
  </div>
  <div class="tape" style="left:900px;top:770px;rotate:28deg;width:140px"></div>
  {svg(burst(440, 830, 85, "novo!", rot=-14, fs=42))}
  <p class="tx" style="left:64px;top:1240px;width:560px">Era pra dizer que tinha. Ninguém pensava em quem ia entrar.</p>'''))

# 3 · hoje: sobra site ruim; página quebrada, carregando, aviso, x
S.append(slide(3, f'''
  <p class="mono" style="left:64px;top:96px">hoje</p>
  <h1 class="giga w2" style="left:64px;top:140px;font-size:230px">sobra site<br><span class="b">ruim.</span></h1>
  <div class="win" style="left:64px;top:700px;width:560px;height:360px;rotate:-3deg">
    <div class="bar"><i></i><i></i><span>carregando…</span></div>
    <p style="position:absolute;left:30px;top:90px;font-family:'Anton';font-size:150px;line-height:1">404</p>
    <p class="mono" style="position:absolute;left:34px;top:260px;font-size:22px">página não encontrada</p>
  </div>
  {svg(
      '<circle cx="840" cy="790" r="70" fill="none" stroke="#f2efea" stroke-width="14" stroke-dasharray="60 26"/>',
      '<g transform="rotate(8 860 1010)"><polygon points="860,920 960,1090 760,1090" fill="none" stroke="#0a63b2" stroke-width="12" stroke-linejoin="round"/><text x="860" y="1075" text-anchor="middle" font-family="Anton" font-size="110" fill="#0a63b2">!</text></g>',
      xis(560, 690, 44), cursor(500, 1000, 1.4, 12))}
  <p class="tx" style="left:64px;top:1150px;width:760px">Lento no celular, sem preço, botão que não leva a lugar nenhum. Existe, mas não trabalha.</p>''', "preto"))

# 4 · vitrine x site único: a placa "aberto" só mostra; o ímã capta
S.append(slide(4, f'''
  <h1 class="giga w1" style="left:64px;top:110px;font-size:200px">vitrine</h1>
  <p class="it" style="left:64px;top:330px;font-size:72px">só mostra.</p>
  {svg(risco([(40, 236), (330, 226), (620, 244), (700, 230)], w=16),
       '<path d="M780,40 L840,190 M960,40 L900,190" stroke="#121112" stroke-width="4"/>')}
  <div class="aberto" style="left:780px;top:190px;rotate:5deg">aberto</div>
  <h1 class="giga w2 b" style="left:64px;top:560px;font-size:230px">site único</h1>
  <p class="it" style="left:64px;top:830px;font-size:96px">capta.</p>
  {svg('<g transform="rotate(-20 760 1050)"><path d="M660,960 L660,1080 A100,100 0 0 0 860,1080 L860,960" fill="none" stroke="#121112" stroke-width="64"/><rect x="628" y="930" width="64" height="56" fill="#0a63b2"/><rect x="828" y="930" width="64" height="56" fill="#0a63b2"/></g>',
       '<circle cx="560" cy="1000" r="16" fill="#0a63b2"/><circle cx="470" cy="960" r="12" fill="#0a63b2"/><circle cx="500" cy="1080" r="14" fill="#0a63b2"/><circle cx="390" cy="1030" r="10" fill="#0a63b2"/>',
       '<path d="M590,1000 L620,1000 M500,950 L560,945 M530,1080 L590,1070" stroke="#0a63b2" stroke-width="5" stroke-dasharray="8 8"/>')}
  <p class="tx" style="left:64px;top:1150px;width:620px">Vitrine mostra e espera. Um site pensado pro seu cliente tira a dúvida, mostra o preço e leva até o WhatsApp.</p>'''))

# 5 · a rua mais movimentada: placa azul, faixa de pedestre, setas
S.append(slide(5, f'''
  <p class="it" style="left:64px;top:96px;font-size:72px">A internet é a</p>
  <h1 class="giga w1" style="left:64px;top:200px;font-size:210px">rua mais<br><span class="b">movimen-</span><br><span class="b">tada.</span></h1>
  <div class="placa" style="left:470px;top:880px;rotate:-4deg;font-size:76px">R. da internet<small>aberta 24 horas, todo dia</small></div>
  <div class="zebra" style="left:-40px;top:1110px;width:1160px;color:var(--ink);rotate:-4deg;opacity:.9"></div>
  {svg(seta(120, 1340, 330, 1300, TINTA, 10), seta(760, 1350, 980, 1330, TINTA, 10))}
  <p class="tx" style="left:64px;top:860px;width:380px">E o seu negócio precisa de um endereço nela. Não só de um perfil.</p>'''))

# 6 · o cliente pergunta pra IA: busca + balões
S.append(slide(6, f'''
  <p class="it" style="left:64px;top:96px;font-size:66px">Seu cliente não<br>pesquisa só no</p>
  <h1 class="giga w2" style="left:64px;top:270px;font-size:230px">google<span class="b">.</span></h1>
  <div class="busca" style="left:64px;top:600px;width:760px;rotate:-2deg">
    <svg width="44" height="44"><circle cx="18" cy="18" r="14" fill="none" stroke="#f2efea" stroke-width="5"/><path d="M29,29 L42,42" stroke="#f2efea" stroke-width="6" stroke-linecap="round"/></svg>
    barbearia perto de mim</div>
  <div class="bal" style="left:240px;top:760px;width:760px;rotate:2deg"><small>pro chatgpt</small>Onde tem uma barbearia boa aqui perto?</div>
  <div class="bal" style="left:64px;top:960px;width:700px;rotate:-2deg;background:var(--blue);border-color:var(--blue)"><small>pro claude</small>Quero um bolo de festa pra sábado. Quem faz?</div>
  <p class="tx" style="left:64px;top:1170px;width:860px">Ele também pergunta pra IA. E ela responde com o que consegue ler na internet sobre você.</p>''', "preto"))

# 7 · aparecer: alfinete de mapa com o ponto, retícula, seta
S.append(slide(7, f'''
  <p class="it" style="left:64px;top:96px;font-size:72px">Não basta existir.<br>Você precisa</p>
  <h1 class="giga w1 b" style="left:40px;top:310px;font-size:262px">aparecer.</h1>
  <div class="half" style="left:520px;top:640px;width:560px;height:560px;color:var(--ink)"></div>
  {svg('<path d="M800,1170 C730,1060 660,990 660,900 A140,140 0 0 1 940,900 C940,990 870,1060 800,1170 Z" fill="#121112"/>',
       '<circle cx="800" cy="900" r="62" fill="#0a63b2"/>', seta(420, 780, 640, 870, AZUL, 9))}
  <p class="mono" style="left:64px;top:700px;width:380px">no google<br>na resposta da ia<br>e no celular de quem chega</p>
  <p class="tx" style="left:64px;top:1140px;width:560px">E quando o cliente chega, o site precisa convencer em poucos segundos.</p>'''))

# 8 · esse é o meu trabalho
S.append(slide(8, f'''
  <h1 class="giga w2" style="left:64px;top:110px;font-size:205px">esse é o<br>meu<br>trabalho.</h1>
  <div class="dot" style="left:810px;top:840px;width:170px;height:170px"></div>
  {svg(burst(250, 960, 120, "sites|e aplicações", rot=-10, fundo=TINTA, cor=OFF, fs=36), circulo(895, 925, 125, 125, OFF, 7))}
  <p class="tx" style="left:64px;top:1110px;width:900px">Senerine.dev é um estúdio digital autoral. Faço sites e aplicações pro seu cliente achar, entender e chamar. Me chama no direct.</p>
  <p class="tag" style="left:64px;top:1290px;rotate:-2deg;font-size:46px">manda pra quem acha que site já era</p>''', "azul"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{SVG_DEFS}{"".join(S)}</body></html>'''
open("site-2026.html", "w").write(html)
