"""Carrossel "link na bio", versão zine: papel de fotocópia, imagens em tinta preta, um único azul
de risografia (o ponto da senerine.dev) e manchetes em Anton. 7 slides 1080x1350."""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1350px; overflow:hidden; background:var(--paper); color:var(--ink); font-family:"Inter Tight",sans-serif; }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.04em; text-transform:uppercase; }
.top { left:64px; right:64px; top:56px; display:flex; justify-content:space-between; padding-bottom:16px; border-bottom:3px solid var(--ink); }
.bot { left:64px; right:64px; top:1262px; display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:3px solid var(--ink); }
.bot b { font-weight:700; }
.h { font-family:"Anton",sans-serif; font-weight:400; text-transform:uppercase; line-height:.9; letter-spacing:-.005em; z-index:3; }
.h .b { color:var(--blue); mix-blend-mode:multiply; }
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
'''


def slide(n, inner, nxt="vira a página →"):
    return f'''<section class="s" id="s{n}">
  <div class="mono top"><span>senerine.dev · zine nº 01 · link na bio</span><span>{n:02d} / 07</span></div>
  {inner}
  <div class="mono bot"><span><b>senerine.dev</b></span><span>{nxt}</span></div>
  <div class="grain"></div>
</section>'''


S = []

# 1 · capa: o menino que veio correndo pela bio
S.append(slide(1, '''
  <div class="dot" style="left:430px;top:470px;width:600px;height:600px"></div>
  <img class="img" src="../../elementos/tinta/menino.png" style="left:380px;top:330px;height:940px">
  <h1 class="h" style="left:64px;top:132px;font-size:178px">Ele veio<br>correndo<br>pelo seu<br><span class="b">link.</span></h1>
  <div class="strip tx" style="left:64px;top:1010px;width:560px;rotate:-2deg">E chegou numa página igual à de todo mundo, com o nome de outra empresa.</div>
  <div class="tape" style="left:300px;top:990px;rotate:4deg"></div>'''))

# 2 · o endereço roda o mundo com o nome deles
S.append(slide(2, '''
  <div class="dot" style="left:388px;top:494px;width:356px;height:356px"></div>
  <img class="img" src="../../elementos/tinta/mundo.png" style="left:230px;top:220px;height:1000px">
  <h1 class="h" style="left:64px;top:132px;font-size:150px">Seu link<br>roda o <span class="b">mundo</span></h1>
  <p class="h" style="left:64px;top:1046px;font-size:86px"><span class="lab">linktr.ee/</span><span style="opacity:.35">seunegocio</span></p>
  <p class="tx" style="left:600px;top:150px;width:416px;font-size:24px;text-align:right">Com o nome de outra empresa. Cada vez que alguém salva ou compartilha, divulga a plataforma.</p>
  <div class="stamp" style="left:690px;top:930px;rotate:-8deg">no plano grátis,<br>a marca deles<br>vai no rodapé</div>'''))

# 3 · todo mundo vê a mesma página
S.append(slide(3, '''
  <img class="img" src="../../elementos/tinta/tvs.png" style="left:250px;top:300px;height:940px">
  <div class="dot" style="left:610px;top:575px;width:118px;height:118px"></div>
  <h1 class="h" style="left:64px;top:132px;font-size:150px">Todo mundo<br>vê a <span class="b">mesma</span><br>página.</h1>
  <div class="strip tx" style="left:64px;top:900px;width:430px;rotate:1.5deg">Pizzaria, barbearia, loja de roupa. Mesmo layout, mesmos botões. Quem clica não sente a sua marca.</div>
  <div class="tape" style="left:200px;top:880px;rotate:-5deg"></div>'''))

# 4 · quem tem pressa
S.append(slide(4, '''
  <div class="dot" style="left:640px;top:190px;width:340px;height:340px"></div>
  <img class="img" src="../../elementos/tinta/pressa.png" style="left:400px;top:160px;width:620px">
  <h1 class="h" style="left:64px;top:770px;font-size:126px">Quem tem<br>pressa não<br><span class="b">escolhe</span> botão.</h1>
  <p class="tx" style="left:64px;top:150px;width:380px;font-size:26px">bio<br>→ <s>lista de links</s><br>→ cardápio<br>→ whatsapp</p>
  <p class="tx" style="left:64px;top:1196px;width:952px;font-size:24px">Cada tela no meio do caminho é uma chance de ir embora.</p>'''))

# 5 · calma, não é o fim do mundo
S.append(slide(5, '''
  <div class="dot" style="left:130px;top:700px;width:500px;height:500px"></div>
  <img class="img" src="../../elementos/tinta/fim.png" style="left:-110px;top:180px;width:1000px">
  <h1 class="h" style="left:64px;top:132px;font-size:168px">Calma.<br>Não é o fim<br>do <span class="b">mundo.</span></h1>
  <div class="strip tx" style="left:640px;top:760px;width:376px;font-size:25px;rotate:2deg">O Linktree é grátis, fica pronto em minutos e resolve no começo. O problema é ficar nele quando o negócio já tem cara própria.</div>
  <div class="tape" style="left:760px;top:740px;rotate:-5deg"></div>'''))

# 6 · uma página com a sua cara
S.append(slide(6, '''
  <div class="dot" style="left:480px;top:440px;width:520px;height:520px"></div>
  <img class="img" src="../../elementos/tinta/flor.png" style="left:390px;top:350px;width:700px">
  <h1 class="h" style="left:64px;top:132px;font-size:150px">Seu link pode<br>ter a <span class="b">sua cara.</span></h1>
  <p class="tx" style="left:64px;top:520px;width:380px;font-size:26px;line-height:1.7">01 seu domínio<br>02 suas cores<br>03 o botão que<br>&nbsp;&nbsp;&nbsp;importa primeiro<br>04 os cliques no<br>&nbsp;&nbsp;&nbsp;seu painel</p>
  <p class="h" style="left:64px;top:1080px;font-size:86px"><span class="lab">seunegocio.com.br</span></p>'''))

# 7 · chamada com o Leonardo no ponto
S.append(slide(7, '''
  <div class="dot" style="left:560px;top:430px;width:480px;height:480px"></div>
  <img class="img" src="../../elementos/tinta/leo.png" style="left:500px;top:330px;height:930px">
  <h1 class="h" style="left:64px;top:132px;font-size:150px">Quer<br>trocar o<br>link da<br>sua <span class="b">bio?</span></h1>
  <div class="strip tx" style="left:64px;top:900px;width:470px;rotate:-2deg">Faço a sua página de links ou o site completo, no seu domínio. Me chama no direct.</div>
  <div class="tape" style="left:230px;top:880px;rotate:-4deg"></div>
  <div class="stamp" style="left:64px;top:1130px;rotate:-3deg">senerine.dev</div>''', nxt="salva pra depois"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>'''
open("zine.html", "w").write(html)
