"""Carrossel "palavras que o seu site usa e não dizem nada", no estilo anti design / acid graphics
(referências de 2026-11-16): frase gigante distorcida e cortada pela borda, risco azul à mão, texto
miúdo nos cantos, etiqueta preta torta e grão de xerox. Só tipografia, um azul só.
7 slides 1080x1440. Gerar: python3 nada.py && node ../render.mjs nada.html saida 1080 1440 7"""

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; --off:#f2efea; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; background:var(--paper); color:var(--ink); }
.s.preto { background:var(--ink); color:var(--off); }
.s.azul { background:var(--blue); color:var(--off); }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.06em; text-transform:uppercase; line-height:1.4; z-index:5; }
.giga { font-family:"Anton",sans-serif; text-transform:uppercase; line-height:1.04; letter-spacing:-.02em; white-space:nowrap; z-index:2; transform-origin:0 0; }
.w1 { filter:url(#onda); }
.w2 { filter:url(#derrete); }
.risco { left:0; top:0; z-index:3; pointer-events:none; }
.troca { font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; letter-spacing:-.02em; line-height:1.08; z-index:5; }
.tag { font-family:"Anton",sans-serif; text-transform:uppercase; font-size:52px; line-height:1; padding:14px 22px 10px; background:var(--ink); color:var(--off); z-index:6; }
.s.preto .tag { background:var(--off); color:var(--ink); }
.dot { border-radius:50%; background:var(--blue); z-index:4; }
.s.azul .dot { background:var(--off); }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.32;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.s.preto .grain, .s.azul .grain { mix-blend-mode:screen; opacity:.16;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
'''

# filtros de distorção (acid): onda horizontal e "derretido" vertical
SVG_DEFS = '''<svg width="0" height="0" style="position:absolute"><defs>
  <filter id="onda" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.0025 0.006" numOctaves="1" seed="4"/><feDisplacementMap in="SourceGraphic" scale="55" xChannelSelector="R" yChannelSelector="G"/></filter>
  <filter id="derrete" x="-10%" y="-10%" width="120%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.006 0.0012" numOctaves="1" seed="9"/><feDisplacementMap in="SourceGraphic" scale="90" xChannelSelector="B" yChannelSelector="R"/></filter>
</defs></svg>'''


def risco(pts, cor="#0a63b2", w=34):
    """Risco azul feito à mão por cima da frase: uma linha que treme um pouco."""
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    return (f'<svg class="risco" width="1080" height="1440"><path d="{d}" fill="none" stroke="{cor}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def slide(n, inner, cls="", canto="senerine.dev"):
    return f'''<section class="s {cls}" id="s{n}">
  {inner}
  <p class="mono" style="right:64px;bottom:56px;text-align:right">{canto}</p>
  <div class="grain"></div>
</section>'''


def cliche(n, cls, num, linhas, tam, top, estica, filtro, porque, troca, exemplo, cor_risco="#0a63b2", lh=1.04):
    giga = "<br>".join(linhas)
    meio = top + tam * 1.04 * estica * .55  # o risco atravessa a primeira linha, longe dos acentos de baixo
    riscos = [(20, meio + 10), (300, meio - 12), (620, meio + 18), (1060, meio - 8)]
    return slide(n, f'''
  <p class="mono" style="left:64px;top:56px">frase que não diz nada<br>nº {num:02d} / 05</p>
  <p class="mono" style="right:64px;top:56px;text-align:right;width:360px">{porque}</p>
  <h1 class="giga {filtro}" style="left:40px;top:{top}px;font-size:{tam}px;line-height:{lh};transform:scaleY({estica})">{giga}</h1>
  {risco(riscos, cor_risco)}
  <p class="tag" style="left:64px;top:1004px;rotate:-3deg">troca por</p>
  <p class="troca" style="left:64px;top:1090px;width:900px;font-size:60px">{troca}</p>
  <p class="mono" style="left:64px;bottom:56px;width:640px;text-transform:none;letter-spacing:0;font-size:24px">{exemplo}</p>''', cls)


S = []

# 1 · capa: "NADA." gigante, derretido, cortado pelas bordas; o ponto é o ponto final
S.append(slide(1, '''
  <p class="troca" style="left:64px;top:110px;font-size:76px;width:900px">Seu site fala muito<br>e não diz</p>
  <h1 class="giga w2" style="left:-30px;top:420px;font-size:620px;transform:scaleY(1.5)">nada</h1>
  <div class="dot" style="left:930px;top:1170px;width:120px;height:120px"></div>
  <p class="tag" style="left:64px;top:300px;rotate:-4deg">5 frases pra trocar hoje</p>
  <p class="mono" style="left:64px;bottom:56px">arrasta →</p>'''))

S.append(cliche(2, "", 1, ["qualidade", "e excelên-", "cia"], 205, 190, 1.12, "w1",
                "todo mundo diz.<br>ninguém acredita.",
                "o que você faz, de verdade.",
                "ex.: “Corte, barba e sobrancelha. Marca o horário pelo site.”"))

S.append(cliche(3, "preto", 2, ["bem-vindo", "ao nosso", "site"], 215, 190, 1.1, "w1",
                "a primeira frase<br>é a mais lida.",
                "o que você faz e pra quem, logo de cara.",
                "ex.: “Bolos de festa sob encomenda, entregues na sua casa.”"))

S.append(cliche(4, "", 3, ["solu-", "ções"], 310, 140, 1.06, "w2",
                "solução de quê?",
                "o problema que você resolve.",
                "ex.: “O cliente marca sozinho, sem esperar resposta no WhatsApp.”", lh=1.2))

S.append(cliche(5, "azul", 4, ["saiba", "mais"], 345, 180, 1.12, "w1",
                "o botão que<br>não diz pra onde vai.",
                "o que acontece quando clica.",
                "ex.: “Ver o cardápio”, “Marcar horário”, “Chamar no WhatsApp”.", cor_risco="#121112"))

S.append(cliche(6, "preto", 5, ["preço", "justo"], 345, 180, 1.12, "w2",
                "justo pra quem?<br>quanto é?",
                "o preço, ou pelo menos “a partir de”.",
                "Quem não acha o preço pergunta no direct. Ou vai embora."))

# 7 · chamada: falar menos, dizer mais; o ponto fecha
S.append(slide(7, '''
  <p class="mono" style="left:64px;top:56px">agora é com você</p>
  <h1 class="giga" style="left:64px;top:150px;font-size:230px;transform:scaleY(1.05)">fala<br>menos.</h1>
  <h1 class="giga w2" style="left:64px;top:690px;font-size:230px;transform:scaleY(1.1);color:var(--blue)">diz mais</h1>
  <div class="dot" style="left:790px;top:860px;width:90px;height:90px"></div>
  <p class="troca" style="left:64px;top:1030px;font-size:46px;width:900px">Abre o seu site e procura essas 5 frases. Achou alguma? Me chama no direct que eu te ajudo a trocar.</p>
  <p class="tag" style="left:64px;top:1250px;rotate:-2deg">salva e manda pra quem precisa</p>''', canto="senerine.dev"))

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{SVG_DEFS}{"".join(S)}</body></html>'''
open("nada.html", "w").write(html)
