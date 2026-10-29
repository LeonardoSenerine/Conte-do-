"""Destaque "Processo": capa + 7 stories (abertura, 5 etapas, fecho) no estilo zine.
Textos das etapas tirados do site (dictionaries.ts, seção process e "como funciona"), sem o exemplo da SURAMU."""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1920px; overflow:hidden; background:var(--paper); color:var(--ink); }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:24px; letter-spacing:.06em; text-transform:uppercase; }
.anton { font-family:"Anton",sans-serif; text-transform:uppercase; line-height:.86; }
.bod { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:700; line-height:.9; letter-spacing:-.035em; }
.ins { font-family:"Instrument Serif",serif; line-height:1.02; letter-spacing:-.015em; }
.ins i { font-style:italic; }
.tx { font-family:"JetBrains Mono",monospace; font-size:30px; line-height:1.5; letter-spacing:-.01em; }
.tags { display:flex; gap:14px; }
.tags span { background:var(--ink); color:var(--paper); font-family:"JetBrains Mono",monospace; font-size:24px; letter-spacing:.06em; text-transform:uppercase; padding:10px 16px 8px; }
.rule { left:72px; right:72px; height:3px; background:var(--ink); }
.img { mix-blend-mode:multiply; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.28;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
'''

STEPS = [
    ("Entender", ["marca", "objetivo", "usuário"], "Quem é essa marca, o que ela quer e <i>quem ela precisa alcançar?</i>",
     "A personalidade e o objetivo vêm antes da paleta. Começa com uma conversa, por vídeo ou WhatsApp, e termina numa proposta por escrito com valor fechado."),
    ("Conceber", ["conteúdo", "roteiro", "design"], "O que a pessoa <i>sente a cada rolagem?</i>",
     "O roteiro e o sistema visual existem antes da tela. Primeiro o que dizer e em que ordem, depois como isso aparece."),
    ("Construir", ["interface", "tecnologia"], "Qual é a ferramenta certa <i>para o tamanho do problema?</i>",
     "Só agora o código entra. Você acompanha o site sendo feito por um link e pede ajustes no caminho."),
    ("Refinar", ["detalhe", "performance", "acessibilidade"], "O que ainda sobra e <i>o que ainda falta?</i>",
     "Cada tela é revisada no celular, com imagens leves e contraste de verdade. É aqui que nenhum detalhe passa batido."),
    ("Publicar", ["domínio", "SEO", "acompanhamento"], "Como o site chega <i>a quem precisa dele?</i>",
     "Domínio, Google, prévia de link e acompanhamento depois do ar. Trocar um preço, uma foto ou um horário é só me mandar uma mensagem."),
]


def path(cur, y=1640, labels=True):
    """O caminho das 5 etapas: linha azul com os pontos; o da etapa atual aceso e maior."""
    x0, x1 = 100, 980
    xs = [x0 + i * (x1 - x0) / 4 for i in range(5)]
    h = f'<div style="left:{x0}px;top:{y - 2}px;width:{x1 - x0}px;height:4px;background:var(--blue)"></div>'
    for i, x in enumerate(xs, 1):
        on = i == cur
        r = 26 if on else 13
        st = "background:var(--blue);box-shadow:0 0 0 10px rgba(10,99,178,.18)" if on else ("background:var(--blue)" if cur and i < cur else "background:var(--paper);border:4px solid var(--blue)")
        h += f'<div style="left:{x - r}px;top:{y - r}px;width:{2*r}px;height:{2*r}px;border-radius:50%;{st}"></div>'
        if labels:
            h += f'<p class="mono" style="left:{x - 100}px;width:200px;top:{y + 44}px;text-align:center;font-size:19px;opacity:{1 if on else .55};font-weight:{700 if on else 400}">{STEPS[i-1][0]}</p>'
    return h


def frame(n, inner, right):
    return f'''<section class="s" id="s{n}">
  <p class="mono" style="left:72px;top:250px">processo · senerine.dev</p><p class="mono" style="right:72px;top:250px">{right}</p>
  <div class="rule" style="top:300px"></div>
  {inner}
  <div class="grain"></div>
</section>'''


S = []

# capa do destaque (o Instagram recorta o centro em círculo): o caminho com o último ponto grande
S.append('''<section class="s" id="s0">
  <div style="left:170px;top:958px;width:620px;height:5px;background:var(--blue)"></div>
  ''' + ''.join(f'<div style="left:{170 + i*155 - 16}px;top:944px;width:32px;height:32px;border-radius:50%;background:var(--blue)"></div>' for i in range(4)) + '''
  <div style="left:750px;top:880px;width:160px;height:160px;border-radius:50%;background:var(--blue);box-shadow:0 0 0 18px rgba(10,99,178,.18)"></div>
  <div class="grain"></div>
</section>''')

# abertura
S.append(frame(1, f'''
  <p class="anton" style="left:66px;top:340px;font-size:200px;line-height:.98">Código<br>é a <span style="color:var(--blue)">última</span><br>etapa.</p>
  <p class="ins" style="left:72px;top:1170px;width:900px;font-size:66px">Antes de abrir o editor, <i>todo projeto passa por cinco etapas.</i></p>
  <p class="tx" style="left:72px;top:1390px;width:900px;font-size:28px">Do primeiro rabisco ao site no ar, você fala direto comigo. Quem ouve o pedido é quem desenha e escreve o código.</p>
  {path(0)}
  <p class="mono" style="right:72px;top:1760px;opacity:.6">toca pra seguir →</p>''', "00 / 05"))

# etapas
for i, (t, tags, q, tx) in enumerate(STEPS, 1):
    extra = ""
    if i == 1:
        extra = '<img class="img" src="../../elementos/tinta/dobermans.png" style="left:600px;top:320px;width:470px;clip-path:inset(0 0 33% 0)">'
    if i == 5:
        extra = '<img class="img" src="../../elementos/tinta/mundo.png" style="left:560px;top:180px;width:520px;clip-path:inset(18% 0 25% 0)">'
    S.append(frame(i + 1, f'''{extra}
  <p class="anton" style="left:58px;top:330px;font-size:470px;color:var(--blue);mix-blend-mode:multiply">{i:02d}</p>
  <p class="bod" style="left:66px;top:770px;font-size:150px">{t}</p>
  <div class="tags" style="left:72px;top:960px">{''.join(f'<span>{g}</span>' for g in tags)}</div>
  <p class="ins" style="left:72px;top:1060px;width:920px;font-size:74px">{q}</p>
  <p class="tx" style="left:72px;top:1290px;width:920px;font-size:29px">{tx}</p>
  {path(i)}''', f"{i:02d} / 05"))

# fecho
S.append(frame(7, f'''
  <p class="ins" style="left:72px;top:370px;width:940px;font-size:96px">Valor fechado, prévia ao vivo e <i>alguém por perto depois.</i></p>
  <p class="anton" style="left:66px;top:800px;font-size:200px;line-height:1.08">Começa<br>pela <span style="color:var(--blue)">01.</span></p>
  <p class="tx" style="left:72px;top:1240px;width:900px">Me conta da sua marca e do que ela precisa. Quem responde sou eu, no direct ou pelo link da bio.</p>
  {path(5, labels=False)}
  <p class="mono" style="left:72px;top:1720px;font-weight:700">senerine.dev</p>''', "fim"))

open("processo.html", "w").write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>''')
