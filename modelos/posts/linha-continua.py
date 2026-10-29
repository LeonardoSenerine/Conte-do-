"""Carrossel "caro e barato ao mesmo tempo" (referência: texto curto em fundo liso, uma linha que
atravessa os slides e encosta no texto). Aqui no papel do zine, com a linha azul do ponto.
8 slides 1080x1350 num canvas só; a linha é desenhada no navegador a partir da posição real dos textos."""

N, W, H, Y = 8, 1080, 1350, 675
X = lambda n, x=0: (n - 1) * W + x

CSS = r'''
:root { --paper:#e8e6e0; --ink:#121112; --blue:#0a63b2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:8640px; height:1350px; background:var(--paper); color:var(--ink); position:relative; overflow:hidden; font-family:"Inter Tight",sans-serif; }
.a { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:20px; letter-spacing:.08em; text-transform:uppercase; color:rgba(18,17,18,.55); }
.tx { top:675px; transform:translateY(-50%); font-size:64px; font-weight:500; line-height:1.08; letter-spacing:-.035em; z-index:3; }
.tx c, .tx b { font-family:"Instrument Serif",serif; font-style:italic; font-weight:400; font-size:1.2em; letter-spacing:-.01em; line-height:.9; }
.tx b { color:var(--blue); }
.tx small { position:absolute; top:100%; left:0; right:0; margin-top:26px; font-family:"JetBrains Mono",monospace; font-size:23px; line-height:1.45; letter-spacing:0; color:rgba(18,17,18,.62); font-weight:400; }
.img { mix-blend-mode:multiply; z-index:2; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.28;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
'''

slides = [
    # (alinhamento, texto, imagens [(arquivo, left, top, width)])
    ("l", "Meu site é <c>caro</c><br>e <b>barato</b> ao<br>mesmo tempo.", [("tulipa.png", 300, 790, 820)]),
    ("r", "<c>Caro</c> pra quem só<br>quer um site pra<br>dizer que tem.", [("porsche.png", 60, -10, 680)]),
    ("l", "<b>Barato</b> pra quem<br>quer que o site<br>traga cliente.", [("lirios.png", 470, 790, 560)]),
    ("r", "<c>Caro</c> pra quem acha<br>que qualquer site<br>serve.<small>Site genérico deixa o<br>seu negócio sem cara.</small>", [("terno.png", 40, -20, 540)]),
    ("l", "<b>Barato</b> pra quem<br>cansou de ver cliente<br>chegar e ir embora.", [("mao-mao.png", 405, 150, 675), ("mao-homem.png", 520, 860, 420)]),
    ("r", "<c>Caro</c> mesmo é o<br>barato que sai caro.<small>O site que trava, ninguém<br>acha e precisa ser refeito.</small>", [("batida.png", 60, -70, 820)]),
    ("l", "Site não é gasto.<br>É a vitrine que<br><b>nunca fecha.</b>", [("faixa.png", 520, 140, 760)]),
    ("r", "Quer vender mais?<br><b>Vamos conversar.</b><small>senerine.dev · link na bio</small>", []),
]

out = []
for i, (al, t, imgs) in enumerate(slides, 1):
    out.append(f'<p class="a mono" style="left:{X(i,72)}px;top:64px">senerine.dev</p><p class="a mono" style="left:{X(i,808)}px;width:200px;text-align:right;top:64px">{i:02d} / {N:02d}</p>')
    pos = f"left:{X(i,72)}px" if al == "l" else f"right:{(N - i) * W + 72}px;text-align:right"
    out.append(f'<div class="a tx" data-al="{al}" style="{pos}">{t}</div>')
    for f, l, tp, w in imgs:
        out.append(f'<img class="a img" src="../../elementos/tinta/{f}" style="left:{X(i,l)}px;top:{tp}px;width:{w}px">')

JS = f'''
const Y = {Y}, PAD = 34, ns = "http://www.w3.org/2000/svg";
const svg = document.querySelector("svg");
const box = [...document.querySelectorAll(".tx")].map(e => {{
  // mede só a linha do meio do bloco (onde a linha encosta), pela largura real do texto
  const r = document.createRange(); r.selectNodeContents(e);
  const rs = [...r.getClientRects()].filter(q => q.height > 30);
  return {{ x0: Math.min(...rs.map(q => q.left)), x1: Math.max(...rs.map(q => q.right)) }};
}});
let d = "";
for (let i = 0; i < box.length - 1; i++) d += ` M ${{box[i].x1 + PAD}} ${{Y}} L ${{box[i + 1].x0 - PAD}} ${{Y}}`;
const p = document.createElementNS(ns, "path"); p.setAttribute("d", d); svg.appendChild(p);
const c = document.createElementNS(ns, "circle"); c.setAttribute("cx", box.at(-1).x0 - PAD); c.setAttribute("cy", Y); c.setAttribute("r", 16); svg.appendChild(c);
'''

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}
svg path {{ fill:none; stroke:var(--blue); stroke-width:4; }} svg circle {{ fill:var(--blue); filter:drop-shadow(0 0 10px rgba(74,163,234,.8)); }}</style></head>
<body>{"".join(out)}
<svg class="a" style="left:0;top:0;z-index:4" width="{N*W}" height="{H}"></svg>
<div class="a grain"></div>
<script>document.fonts.ready.then(() => {{ {JS} document.body.dataset.ok = 1; }});</script>
</body></html>'''
open("caro.html", "w").write(html)
