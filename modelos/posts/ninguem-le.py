"""Carrossel "ninguém lê o seu site", versão zine: papel de fotocópia, colagens em tinta preta,
o azul do ponto como única cor (a cabeça e a folha do leitor já vêm azuis do tinta.py).
9 slides 1080x1440. Gerar: python3 ninguem-le.py && node ../render.mjs ninguem-le.html saida 1080 1440 9"""

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
.h { font-family:"Anton",sans-serif; font-weight:400; text-transform:uppercase; line-height:1; letter-spacing:-.005em; z-index:3; }
.h .b { color:var(--blue); mix-blend-mode:multiply; }
.it { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; letter-spacing:-.02em; line-height:1; z-index:3; }
.it .b { color:var(--blue); mix-blend-mode:multiply; }
.lab { background:var(--ink); color:var(--paper); padding:.06em .22em .02em; display:inline-block; }
.dot { border-radius:50%; background:var(--blue); mix-blend-mode:multiply; }
.img { mix-blend-mode:multiply; z-index:2; }
.tx { font-family:"JetBrains Mono",monospace; font-size:27px; line-height:1.45; letter-spacing:-.01em; z-index:3; }
.strip { background:#f6f5f1; padding:22px 26px; box-shadow:0 2px 0 rgba(0,0,0,.08), 0 18px 30px -18px rgba(0,0,0,.35); z-index:4; }
.tape { width:150px; height:44px; background:rgba(230,226,214,.75); box-shadow:0 1px 2px rgba(0,0,0,.12); z-index:5; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.28;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.stamp { border:4px solid var(--blue); color:var(--blue); padding:10px 18px; font-family:"JetBrains Mono",monospace; font-weight:700; font-size:24px; letter-spacing:.1em; text-transform:uppercase; mix-blend-mode:multiply; z-index:6; }
s { text-decoration:none; position:relative; }
s::after { content:""; position:absolute; left:-4%; right:-4%; top:52%; height:.16em; background:var(--blue); mix-blend-mode:multiply; rotate:-3deg; }
.list { left:64px; right:64px; z-index:3; }
.list div { display:flex; align-items:baseline; gap:28px; padding:20px 0 18px; border-top:3px solid var(--ink); }
.list div:last-child { border-bottom:3px solid var(--ink); }
.list .n { font-family:"Anton",sans-serif; font-size:64px; line-height:1; color:var(--blue); mix-blend-mode:multiply; width:84px; }
.list .t { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; font-size:54px; line-height:1.05; letter-spacing:-.02em; }
.list .t small { display:block; font-family:"JetBrains Mono",monospace; font-style:normal; font-weight:400; font-size:24px; letter-spacing:0; margin-top:8px; }
.leo { border-radius:50%; object-fit:cover; z-index:4; }
'''

T = "../../elementos/tinta/"


def slide(n, inner, nxt="vira a página →"):
    return f'''<section class="s" id="s{n}">
  <div class="mono top"><span>senerine.dev · zine nº 02 · ninguém lê</span><span>{n:02d} / 09</span></div>
  {inner}
  <div class="mono bot"><span><b>senerine.dev</b></span><span>{nxt}</span></div>
  <div class="grain"></div>
</section>'''


S = []

# 1 · capa: a cabeça azul com a faixa do olho
S.append(slide(1, f'''
  <img class="img" src="{T}cabeca-azul.png" style="left:300px;top:420px;height:932px">
  <h1 class="h" style="left:64px;top:128px;font-size:184px">Ninguém lê<br>o seu site.</h1>
  <p class="it" style="left:64px;top:520px;font-size:96px">Todo<br>mundo<br><span class="b">olha.</span></p>
  <div class="strip tx" style="left:64px;top:1040px;width:380px;rotate:-2deg">Antes da primeira palavra, quem chega já bateu o olho em tudo.</div>
  <div class="tape" style="left:200px;top:1018px;rotate:4deg"></div>'''))

# 2 · a multidão passa correndo
S.append(slide(2, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:168px">Todo mundo<br>passa<br><span class="b">correndo.</span></h1>
  <div class="dot" style="left:790px;top:770px;width:250px;height:250px"></div>
  <img class="img" src="{T}multidao.png" style="left:-120px;top:420px;width:1260px">
  <p class="tx" style="left:64px;top:1180px;width:820px">Rolando o feed, entre uma mensagem e outra. Ninguém abre o seu site pra ler. Abre pra ver se vale a pena ficar.</p>'''))

# 3 · a cabeça aberta: a impressão vem antes do pensamento
S.append(slide(3, f'''
  <img class="img" src="{T}cabeca-aberta.png" style="left:420px;top:330px;height:1020px">
  <div class="dot" style="left:752px;top:552px;width:150px;height:150px"></div>
  <h1 class="h" style="left:64px;top:128px;font-size:150px">Ele decide<br>antes de<br><span class="b">pensar.</span></h1>
  <div class="strip tx" style="left:64px;top:780px;width:440px;rotate:1.5deg">Parece sério? Parece de verdade? Parece caro? A impressão vem primeiro. A leitura, se vier, vem depois.</div>
  <div class="tape" style="left:190px;top:760px;rotate:-5deg"></div>'''))

# 4 · o homem lâmpada na poltrona: julga sem pressa e com outras abas abertas
S.append(slide(4, f'''
  <div class="dot" style="left:648px;top:222px;width:280px;height:280px"></div>
  <img class="img" src="{T}lampada.png" style="left:420px;top:150px;height:1190px">
  <h1 class="h" style="left:64px;top:128px;font-size:150px">E julga<br>do <span class="b">sofá,</span></h1>
  <p class="it" style="left:64px;top:450px;font-size:66px;width:420px">com outras abas abertas.</p>
  <div class="strip tx" style="left:64px;top:1010px;width:420px;rotate:-1.5deg">O concorrente está a um toque. Ele fica com quem parece mais confiável logo de cara.</div>
  <div class="tape" style="left:220px;top:990px;rotate:3deg"></div>'''))

# 5 · o megafone: gritar não adianta
S.append(slide(5, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:150px">Gritar<br><span class="b">não</span><br>adianta.</h1>
  <img class="img" src="{T}megafone.png" style="left:370px;top:520px;width:700px">
  <div class="strip tx" style="left:64px;top:880px;width:400px;rotate:-2deg">Tudo em caixa alta, um monte de cores, banner piscando. Quando tudo chama atenção, <b style="color:var(--blue)">nada chama.</b></div>
  <div class="tape" style="left:180px;top:858px;rotate:-4deg"></div>'''))

# 6 · as botas de baixo: o ângulo que você não olha (o celular)
S.append(slide(6, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:124px;line-height:1.1">Ele vê de<br>um ângulo<br>que você<br>nem <span class="b">olha.</span></h1>
  <div class="dot" style="left:713px;top:640px;width:190px;height:190px"></div>
  <img class="img" src="{T}botas.png" style="left:420px;top:640px;width:690px">
  <div class="strip tx" style="left:64px;top:900px;width:370px;rotate:1.5deg">Você aprova o site no computador. Ele abre no celular, com uma mão só, no meio de outra coisa.</div>
  <div class="tape" style="left:170px;top:880px;rotate:-3deg"></div>'''))

# 7 · Washington apontando pra lista: o que precisa aparecer primeiro
S.append(slide(7, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:120px">O que ele<br>precisa ver<br><span class="b">primeiro:</span></h1>
  <img class="img" src="{T}washington.png" style="left:150px;top:400px;width:860px">
  <div class="list" style="top:858px">
    <div><span class="n">01</span><span class="t">o que você faz<small>em uma frase, sem adivinhar</small></span></div>
    <div><span class="n">02</span><span class="t">que é de verdade<small>foto sua, não de banco de imagem</small></span></div>
    <div><span class="n">03</span><span class="t">como te chamar<small>num toque, sem procurar</small></span></div>
  </div>'''))

# 8 · o leitor: ser justo, texto importa
S.append(slide(8, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:150px">Texto<br>importa,<br><span class="b">sim.</span></h1>
  <img class="img" src="{T}leitor.png" style="left:300px;top:500px;width:820px">
  <div class="strip tx" style="left:64px;top:1030px;width:400px;rotate:-1.5deg">Quem gostou do que viu, lê. Texto bom tira a dúvida e fecha a venda. Mas só lê quem o olho deixou ficar.</div>
  <div class="tape" style="left:200px;top:1010px;rotate:4deg"></div>'''))

# 9 · chamada: a reverência abre a porta, o Leonardo no ponto
S.append(slide(9, f'''
  <h1 class="h" style="left:64px;top:128px;font-size:128px">Quer um site<br>que não passa<br><span class="b">batido?</span></h1>
  <img class="img" src="{T}reverencia.png" style="left:360px;top:540px;width:740px">
  <div class="strip tx" style="left:64px;top:620px;width:440px;rotate:-2deg">Faço sites e aplicações pensados pra quem bate o olho. Me chama no direct.</div>
  <div class="tape" style="left:210px;top:600px;rotate:-4deg"></div>
  <img class="leo" src="{T}leonardo-ponto.webp" style="left:64px;top:960px;width:250px;height:250px">
  <div class="stamp" style="left:300px;top:1160px;rotate:-4deg">senerine.dev</div>''', nxt="salva pra depois"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>'''
open("ninguem-le.html", "w").write(html)
