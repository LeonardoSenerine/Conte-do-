"""Carrossel "seu cliente perdeu o foco" (zine nº 04): só imagens do banco (foco, pressa, queda, megafone,
andorinhas, cavalo, lírios em ramo), notas com linha e o ponto azul. Sem cabeçalho nem rodapé.
8 slides 1080x1440. Gerar: python3 foco.py && node ../render.mjs foco.html saida 1080 1440 8"""

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
.s.fundo .top span, .s.fundo .bot span { background:var(--paper); padding:2px 8px; margin:0 -8px; }
.s.fundo .note { text-shadow:0 0 4px var(--paper), 0 0 8px var(--paper), 0 0 14px var(--paper), 0 0 20px var(--paper); }
.list.c .t { font-size:44px; }
'''

T = "../../elementos/tinta/"


def slide(n, inner, nxt="vira a página →", cls=""):
    return f'''<section class="s {cls}" id="s{n}">
  {inner}
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


S = []

# 1 · capa: o "focus" tremido; o ponto azul fica no "o" nítido
S.append(slide(1, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:170px">Seu cliente<br>perdeu o<br><span class="b">foco.</span></h1>
  <p class="it" style="left:64px;top:672px;font-size:70px">E você nem viu.</p>
  <img class="img" src="{T}foco.png" style="left:40px;top:720px;width:1000px">
  <div class="dot" style="left:292px;top:1036px;width:136px;height:136px"></div>
  {nota(64, 1316, 760, 360, 1104, 'Por que um site lento ou confuso perde quem já estava interessado.', ponto=False)}"""))

# 2 · com pressa: abriu o site no meio de outra coisa
S.append(slide(2, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:160px">Ele está<br>com <span class="b">pressa.</span></h1>
  <p class="it" style="left:64px;top:470px;font-size:70px">Sempre.</p>
  <div class="dot" style="left:700px;top:600px;width:260px;height:260px"></div>
  <img class="img" src="{T}pressa.png" style="left:250px;top:560px;width:800px">
  {nota(64, 1250, 560, 640, 900, 'Ele abriu o seu site no celular, no meio de outra coisa. Se a página demora, ele volta pro que estava fazendo.')}"""))

# 3 · tela em branco: ele cai fora
S.append(slide(3, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:150px">Tela em<br>branco,<br>cliente <span class="b">fora.</span></h1>
  <img class="img" src="{T}queda.png" style="left:230px;top:600px;width:900px">
  {nota(64, 1260, 560, 690, 820, 'Imagem pesada, carregamento que não termina. Enquanto a página não aparece, ele já está indo embora.')}"""))

# 4 · megafone: quando tudo grita
S.append(slide(4, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:140px">Quando tudo<br><span class="b">grita,</span><br>ninguém escuta.</h1>
  <img class="img" src="{T}megafone.png" style="left:420px;top:600px;width:700px">
  {nota(64, 1080, 380, 560, 980, 'Pop-up, vídeo, banner e animação ao mesmo tempo. Quando tudo chama atenção, nada chama.')}"""))

# 5 · andorinhas: uma coisa leva à outra
S.append(slide(5, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:160px">Um caminho<br><span class="b">só.</span></h1>
  <p class="it" style="left:64px;top:470px;width:520px;font-size:56px">Do que ele procura até te chamar.</p>
  <img class="img" src="{T}andorinhas.png" style="left:470px;top:430px;height:1000px">
  {nota(64, 1000, 400, 700, 900, 'O que ele procura logo no topo, um botão claro e nada no meio do caminho. Uma coisa leva à outra.')}"""))

# 6 · cavalo: rápido no celular
S.append(slide(6, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:160px">Rápido no<br><span class="b">celular.</span></h1>
  <p class="tx note" style="left:64px;top:470px;width:600px">Imagem leve, página que abre na hora e nada que trave no celular, que é onde o seu cliente está.</p>
  <div class="dot" style="left:720px;top:640px;width:220px;height:220px"></div>
  <img class="img" src="{T}cavalo.png" style="left:40px;top:560px;width:1000px">"""))

# 7 · ser justo: foco não é site sem graça
S.append(slide(7, f"""
  <p class="it" style="left:64px;top:110px;font-size:84px">Foco não é</p>
  <h1 class="h" style="left:64px;top:214px;font-size:150px">site sem<br><span class="b">graça.</span></h1>
  <img class="img" src="{T}lirios-ramo.png" style="left:500px;top:520px;height:920px">
  {nota(64, 900, 420, 700, 760, 'Bonito também vende. Foco é a beleza trabalhando a favor da mensagem, não competindo com ela.')}"""))

# 8 · chamada: o "focus" volta, com o ponto
S.append(slide(8, f"""
  <h1 class="h" style="left:64px;top:96px;font-size:140px">Quer um site<br>que segura<br>o <span class="b">olhar?</span></h1>
  <img class="img" src="{T}foco.png" style="left:40px;top:640px;width:1000px">
  <div class="dot" style="left:292px;top:956px;width:136px;height:136px"></div>
  {nota(64, 1240, 640, 360, 1024, 'Faço sites e aplicações rápidos e diretos, pensados pro seu cliente. Me chama no direct.', ponto=False)}"""))

html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>"""
open("foco.html", "w").write(html)
