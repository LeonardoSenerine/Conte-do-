"""Carrossel "por que site de modelo pronto passa batido", versão zine (nº 03): estampas e
colagens em tinta, a faixa vertical das referências de 2026-10-29 e o ponto azul.
8 slides 1080x1440. Gerar: python3 modelo-pronto.py && node ../render.mjs modelo-pronto.html saida 1080 1440 8"""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; }
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
'''

T = "../../elementos/tinta/"


def slide(n, inner, nxt="vira a página →"):
    return f'''<section class="s" id="s{n}">
  <div class="mono top"><span>senerine.dev · zine nº 03 · modelo pronto</span><span>{n:02d} / 08</span></div>
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

N1 = nota(64, 770, 760, 790, 990, 'Por que site de modelo pronto passa batido.', ponto=False)
N2 = nota(64, 800, 560, 812, 1130, 'Foi desenhado pra caber em qualquer negócio. Pizzaria, clínica, loja de roupa. Fica bonito em todos e não é de nenhum.', ponto=False)
N3 = nota(64, 1080, 420, 660, 900, 'Quando a página lembra várias outras, a cabeça acha que já conhece e segue rolando.', ponto=False)
N4 = nota(64, 920, 420, 580, 580, 'Foto de banco de imagem, frase que serve pra qualquer um. O cliente não vê quem está do outro lado.', ponto=False)
N5 = nota(64, 860, 400, 500, 840, 'Seções que vieram no modelo, efeito que ninguém pediu, e o botão do WhatsApp lá no fim da página.')
N6 = nota(64, 1040, 480, 600, 1000, 'Pra testar uma ideia ou começar sem verba, resolve bem. O problema é o negócio crescer e o site continuar com cara de qualquer um.')
N7 = nota(64, 780, 440, 566, 700, 'Faço sites e aplicações sob medida, pensados pro seu cliente. Me chama no direct.', ponto=False)

S = []

# 1 · capa: o site bonito que é estampa repetida (a toile), com um ponto no meio das flores
S.append(slide(1, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:168px">Seu site é<br><span class="b">bonito.</span></h1>
  <p class="it" style="left:64px;top:526px;font-size:84px;width:900px">E igual ao de<br>todo mundo.</p>
  <div class="crop" style="left:0;top:860px;width:1080px;height:492px"><img src="{T}toile-flores.png" style="left:0;top:-300px;width:1080px"></div>
  <div class="dot" style="left:690px;top:990px;width:200px;height:200px;z-index:3"></div>
  {N1}'''))

# 2 · modelo pronto é estampa: a pele de cobra numa faixa vertical (referência das faixas)
S.append(slide(2, f'''
  <div class="crop" style="left:720px;top:96px;width:296px;height:1256px"><img src="{T}pele-cobra.png" style="left:-200px;top:0;height:1256px"></div>
  <div class="dot" style="left:808px;top:1080px;width:120px;height:120px;z-index:3"></div>
  <h1 class="h" style="left:64px;top:128px;font-size:132px">Modelo<br>pronto é<br><span class="b">estampa.</span></h1>
  {N2}'''))

# 3 · os pássaros borrados: o olho já viu e passa batido
S.append(slide(3, f'''
  <div class="dot" style="left:640px;top:740px;width:260px;height:260px"></div>
  <img class="img" src="{T}passaros-borrados.png" style="left:470px;top:110px;height:1240px">
  <h1 class="h" style="left:64px;top:128px;font-size:150px">O olho<br>já viu<br>isso.</h1>
  <p class="it" style="left:64px;top:650px;font-size:72px">e passa<br><span class="b">batido.</span></p>
  {N3}'''))

# 4 · o terno sem cabeça: foto de banco e texto de exemplo deixam o negócio sem cara
S.append(slide(4, f'''
  <img class="img" src="{T}terno.png" style="left:420px;top:420px;height:920px">
  <div class="stamp" style="left:566px;top:462px;width:150px;height:150px;border-radius:50%;border-style:dashed;padding:0"></div>
  <h1 class="h" style="left:64px;top:128px;font-size:130px">O negócio<br>fica sem<br><span class="b">cara.</span></h1>
  {N4}'''))

# 5 · o ornamento: enfeite no lugar do que importa, e o botão perdido lá embaixo
S.append(slide(5, f'''
  <img class="img" src="{T}ornamento.png" style="left:450px;top:290px;height:920px;clip-path:inset(1.6%)">
  <h1 class="h" style="left:64px;top:128px;font-size:120px">Enfeite no<br>lugar do que<br><span class="b">importa.</span></h1>
  {N5}
  <div class="dot" style="left:944px;top:1252px;width:56px;height:56px;z-index:3"></div>
  <p class="mono" style="left:680px;top:1266px;z-index:3;color:var(--blue)">o que importa →</p>'''))

# 6 · os leões e a figura de preto: no meio de todo mundo, o diferente fica
S.append(slide(6, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:120px">No meio de<br>todo mundo,</h1>
  <p class="it" style="left:64px;top:410px;font-size:64px">quem é <span class="b">diferente</span> fica.</p>
  <div class="dot" style="left:764px;top:523px;width:200px;height:200px"></div>
  <img class="img" src="{T}leoes.png" style="left:0;top:-327px;width:1080px">
  <p class="mono" style="left:64px;top:900px;z-index:3">sob medida começa pelo seu cliente:</p>
  <div class="list" style="top:950px">
    <div><span class="n">01</span><span class="t">suas cores, suas fotos</span></div>
    <div><span class="n">02</span><span class="t">o que ele procura, no topo</span></div>
    <div><span class="n">03</span><span class="t">o caminho curto até te chamar</span></div>
  </div>'''))

# 7 · as borboletas: ser justo, modelo pronto serve pra começar
S.append(slide(7, f'''
  <div class="dot" style="left:560px;top:600px;width:300px;height:300px"></div>
  <img class="img" src="{T}borboletas.png" style="left:300px;top:450px;width:760px">
  <p class="it" style="left:64px;top:140px;font-size:84px">Modelo pronto</p>
  <h1 class="h" style="left:64px;top:240px;font-size:150px">Não é <span class="b">vilão.</span></h1>
  {N6}'''))

# 8 · chamada com o Leonardo no ponto
S.append(slide(8, f'''
  <div class="dot" style="left:560px;top:500px;width:480px;height:480px"></div>
  <img class="img" src="{T}leo.png" style="left:510px;top:400px;height:952px">
  <h1 class="h" style="left:64px;top:128px;font-size:150px">Quer um<br>site com a<br>sua <span class="b">cara?</span></h1>
  {N7}''', nxt="salva pra depois"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>'''
open("modelo-pronto.html", "w").write(html)
