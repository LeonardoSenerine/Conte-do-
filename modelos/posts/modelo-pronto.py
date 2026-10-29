"""Carrossel "por que site de modelo pronto passa batido", versão zine (nº 03) com as mesmas
colagens do "ninguém lê" (a seleção que ele aprovou), notas com linha e o ponto azul.
9 slides 1080x1440. Gerar: python3 modelo-pronto.py && node ../render.mjs modelo-pronto.html saida 1080 1440 9"""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; --off:#f2efea; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; background:var(--paper); color:var(--ink); font-family:"Inter Tight",sans-serif; }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.04em; text-transform:uppercase; }
.top { left:64px; right:64px; top:56px; display:flex; justify-content:space-between; padding-bottom:16px; border-bottom:3px solid var(--ink); z-index:7; }
.bot { left:64px; right:64px; top:1352px; display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:3px solid var(--ink); z-index:7; }
.bot b { font-weight:700; }
.h { font-family:"Anton",sans-serif; font-weight:400; text-transform:uppercase; line-height:1.08; letter-spacing:-.005em; z-index:3; }
.h .b { color:var(--blue); mix-blend-mode:multiply; }
.it { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; letter-spacing:-.02em; line-height:1; z-index:3; }
.it .b { color:var(--blue); mix-blend-mode:multiply; }
.lab { background:var(--ink); color:var(--paper); padding:.06em .22em .02em; display:inline-block; }
.dot { border-radius:50%; background:var(--blue); mix-blend-mode:multiply; }
.img { mix-blend-mode:multiply; z-index:2; }
.tx { font-family:"JetBrains Mono",monospace; font-size:27px; line-height:1.45; letter-spacing:-.01em; z-index:3; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.2;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.note { border-top:2px solid var(--ink); padding-top:14px; z-index:5; }
.ln { left:0; top:0; z-index:5; pointer-events:none; }
.stamp { border:4px solid var(--blue); color:var(--blue); padding:10px 18px; font-family:"JetBrains Mono",monospace; font-weight:700; font-size:24px; letter-spacing:.1em; text-transform:uppercase; mix-blend-mode:multiply; z-index:6; }
s { text-decoration:none; position:relative; }
s::after { content:""; position:absolute; left:-4%; right:-4%; top:52%; height:.16em; background:var(--blue); mix-blend-mode:multiply; rotate:-3deg; }
.list { left:64px; right:64px; z-index:3; }
.list div { display:flex; align-items:baseline; gap:28px; padding:20px 0 18px; border-top:3px solid var(--ink); }
.list div:last-child { border-bottom:3px solid var(--ink); }
.list .n { font-family:"Anton",sans-serif; font-size:64px; line-height:1; color:var(--blue); mix-blend-mode:multiply; width:84px; }
.list .t { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; font-size:54px; line-height:1.05; letter-spacing:-.02em; }
.list .t small { display:block; font-family:"JetBrains Mono",monospace; font-style:normal; font-weight:400; font-size:24px; letter-spacing:0; margin-top:8px; }
.crop { overflow:hidden; mix-blend-mode:multiply; z-index:2; }
.crop img { position:absolute; }
.s.azul { background:var(--blue); color:var(--off); }
.s.azul .top, .s.azul .bot { border-color:var(--off); }
.s.azul .grain { opacity:.3; }
.follow { width:560px; height:124px; border-radius:62px; background:var(--off); color:var(--blue); font-family:"Anton",sans-serif; font-size:72px; text-transform:uppercase; line-height:124px; text-align:center; z-index:4; box-shadow:0 18px 40px -16px rgba(0,0,0,.45); }
.list.c .t { font-size:44px; }
'''

T = "../../elementos/tinta/"


def slide(n, inner, nxt="vira a página →", cls=""):
    return f'''<section class="s {cls}" id="s{n}">
  <div class="mono top"><span>senerine.dev · zine nº 03 · modelo pronto</span><span>{n:02d} / 09</span></div>
  {inner}
  <div class="mono bot"><span><b>senerine.dev</b></span><span>{nxt}</span></div>
  <div class="grain"></div>
</section>'''


def nota(x, y, w, ax, ay, texto, ponto=True):
    """Texto solto no papel sobre um fio; uma linha fina liga a ponta do fio ao detalhe da imagem
    (ax, ay), onde fica um ponto azul. ponto=False quando a linha já encosta num ponto do slide."""
    jx = x + w if ax > x + w / 2 else x
    ln = f'<line x1="{ax}" y1="{ay}" x2="{jx}" y2="{y}"'
    dot = f'<circle cx="{ax}" cy="{ay}" r="11" fill="#0a63b2" stroke="#e8e6e0" stroke-width="4"/>' if ponto else ""
    return (f'<p class="tx note" style="left:{x}px;top:{y}px;width:{w}px">{texto}</p>'
            f'<svg class="ln" width="1080" height="1440">{ln} stroke="#e8e6e0" stroke-width="8" stroke-linecap="round"/>'
            f'{ln} stroke="#121112" stroke-width="2"/>{dot}</svg>')

N1 = nota(64, 1250, 760, 840, 1080, 'Por que site de modelo pronto passa batido.', ponto=False)
N2 = nota(64, 1000, 400, 668, 450, 'Foi desenhado pra caber em qualquer negócio. Pizzaria, clínica, loja de roupa. Fica bonito em todos e não é de nenhum.', ponto=False)
N3 = nota(64, 1046, 300, 560, 800, 'Quando a página lembra várias outras, a cabeça acha que já conhece e segue rolando.')
N4 = nota(64, 1040, 400, 430, 860, 'Foto de banco de imagem, frase que serve pra qualquer um. O cliente não vê quem está do outro lado.')
N5 = nota(64, 900, 400, 454, 680, 'Seções que vieram no modelo, efeito que ninguém pediu, e o botão do WhatsApp perdido lá no fim da página.')
N6 = nota(64, 900, 440, 774, 680, 'Sob medida começa pelo seu cliente: suas cores, suas fotos, o que ele procura logo no topo e o caminho mais curto até te chamar.', ponto=False)
N7 = nota(64, 640, 440, 620, 580, 'Pra testar uma ideia ou começar sem verba, resolve bem. O problema é o negócio crescer e o site continuar com cara de qualquer um.')
N8 = nota(64, 900, 400, 716, 740, 'Faço sites e aplicações sob medida, pensados pro seu cliente. Me chama no direct.', ponto=False)

S = []

# 1 · capa: a multidão correndo, todo mundo igual
S.append(slide(1, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:168px">Seu site é<br><span class="b">bonito.</span></h1>
  <p class="it" style="left:64px;top:526px;font-size:84px;width:900px">E igual ao de<br>todo mundo.</p>
  <div class="dot" style="left:800px;top:850px;width:230px;height:230px"></div>
  <img class="img" src="{T}multidao.png" style="left:-120px;top:500px;width:1260px">
  {N1}'''))

# 2 · o homem lâmpada: o modelo é o mesmo corpo, só troca a cabeça
S.append(slide(2, f'''
  <div class="dot" style="left:648px;top:222px;width:280px;height:280px"></div>
  <img class="img" src="{T}lampada.png" style="left:420px;top:150px;height:1190px">
  <h1 class="h" style="left:64px;top:128px;font-size:132px">Modelo<br>pronto é<br><span class="b">estampa.</span></h1>
  {N2}'''))

# 3 · a cabeça azul com o olho: o olho já viu e passa batido
S.append(slide(3, f'''
  <img class="img" src="{T}cabeca-azul.png" style="left:300px;top:420px;height:932px">
  <h1 class="h" style="left:64px;top:128px;font-size:150px">O olho<br>já viu<br>isso.</h1>
  <p class="it" style="left:64px;top:650px;font-size:64px">e passa<br><span class="b">batido.</span></p>
  {N3}'''))

# 4 · o leitor com a folha azul no rosto: o negócio fica sem cara
S.append(slide(4, f'''
  <img class="img" src="{T}leitor.png" style="left:300px;top:500px;width:820px">
  <h1 class="h" style="left:64px;top:128px;font-size:130px">O negócio<br>fica sem<br><span class="b">cara.</span></h1>
  {N4}'''))

# 5 · o megafone: enfeite e barulho no lugar do que importa
S.append(slide(5, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:120px">Enfeite no<br>lugar do que<br><span class="b">importa.</span></h1>
  <img class="img" src="{T}megafone.png" style="left:370px;top:520px;width:700px">
  {N5}'''))

# 6 · a cabeça aberta: sob medida começa pela cabeça do cliente
S.append(slide(6, f'''
  <img class="img" src="{T}cabeca-aberta.png" style="left:460px;top:390px;height:960px">
  <div class="dot" style="left:772px;top:598px;width:140px;height:140px"></div>
  <h1 class="h" style="left:64px;top:128px;font-size:120px">No meio de<br>todo mundo,</h1>
  <p class="it" style="left:64px;top:410px;font-size:64px">quem é <span class="b">diferente</span><br>fica.</p>
  {N6}'''))

# 7 · a reverência: ser justo, pra começar sem verba o modelo pronto resolve
S.append(slide(7, f'''
  <img class="img" src="{T}reverencia.png" style="left:360px;top:540px;width:740px">
  <p class="it" style="left:64px;top:140px;font-size:84px">Modelo pronto</p>
  <h1 class="h" style="left:64px;top:240px;font-size:150px">Não é <span class="b">vilão.</span></h1>
  {N7}'''))

# 8 · chamada: as botas, alguém com a própria cara
S.append(slide(8, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:140px">Quer um<br>site com a<br>sua <span class="b">cara?</span></h1>
  <div class="dot" style="left:713px;top:640px;width:190px;height:190px"></div>
  <img class="img" src="{T}botas.png" style="left:420px;top:640px;width:690px">
  {N8}'''))

# 9 · o ponto cresceu e cobriu a página: segue pra ver os próximos projetos, com o Washington apontando pro botão
S.append(slide(9, f'''
  <p class="mono" style="left:64px;top:132px;z-index:3">próximos projetos</p>
  <h1 class="h" style="left:64px;top:170px;font-size:200px;color:var(--off)">Tem mais<br>vindo.</h1>
  <p class="it" style="left:64px;top:600px;font-size:58px;width:760px;color:var(--off)">Sites e aplicações novos saindo do estúdio.</p>
  <img class="img" src="{T}washington.png" style="left:150px;top:640px;width:860px">
  <div class="follow" style="left:300px;top:1170px">+ seguir</div>
  <p class="mono" style="left:64px;top:1300px;z-index:3;width:952px;text-align:center">@senerine.dev · ativa o sininho</p>''', nxt="salva pra depois", cls="azul"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>'''
open("modelo-pronto.html", "w").write(html)
