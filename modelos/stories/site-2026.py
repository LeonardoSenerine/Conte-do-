"""Stories do post "ainda vale a pena ter um site em 2026?", na mesma linguagem do carrossel
(`posts/site-2026-create.py`): fundo com textura, palavra gigante em Bodoni 900 na vertical, o ponto azul
saindo da borda, imagem em retícula clara, título em Instrument Serif engrossada e texto em Inter Tight.
4 stories explicativos, sem interação; o 1º tem o espaço da figurinha do post.
1080x1920. Gerar: python3 site-2026.py && node ../render.mjs site-2026.html saida 1080 1920 4"""

CSS = r'''
:root { --cream:#ece8de; --ink:#121112; --blue:#0a63b2; --claro:#4aa3ea; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1920px; overflow:hidden; color:var(--cream); background:var(--ink) center/cover no-repeat; }
.s.claro { color:var(--ink); }
.s.azul { background:var(--blue); }
.s > * { position:absolute; }
.vert { left:0; top:0; width:1920px; height:330px; transform-origin:0 0; transform:translate(0,1920px) rotate(-90deg);
  display:flex; align-items:center; justify-content:center; z-index:2; }
.vert p { font-family:"Bodoni Moda",serif; font-weight:900; text-transform:uppercase; line-height:.8; letter-spacing:.01em; color:var(--claro); white-space:nowrap; }
.s.claro .vert p { color:var(--blue); }
.s.azul .vert p { color:var(--ink); }
.forma { border-radius:50%; background:var(--blue); z-index:1; }
.s.azul .forma { background:var(--cream); }
.img { z-index:3; }
.s:not(.claro) .img { filter:invert(1) contrast(1.1); mix-blend-mode:screen; }
.s.claro .img { mix-blend-mode:multiply; }
.s.azul .img { filter:none; mix-blend-mode:multiply; }
.tit { left:360px; width:656px; top:280px; text-align:center; text-wrap:balance; font-family:"Instrument Serif",serif; font-weight:400;
  font-size:104px; line-height:1; -webkit-text-stroke:4px currentColor; paint-order:stroke fill; z-index:5; }
.tit i { font-style:italic; color:var(--claro); -webkit-text-stroke:4px var(--claro); }
.s.claro .tit i { color:var(--blue); -webkit-text-stroke:4px var(--blue); }
.s.azul .tit i { color:var(--ink); -webkit-text-stroke:4px var(--ink); }
.txt { left:372px; width:632px; bottom:260px; text-align:center; text-wrap:balance; font-family:"Inter Tight",sans-serif; font-weight:500;
  font-size:44px; line-height:1.3; z-index:5; padding-top:24px; border-top:3px solid currentColor; }
.txt b { font-weight:800; color:var(--claro); }
.s.claro .txt b { color:var(--blue); }
.s.azul .txt b { color:var(--cream); }
.cant { z-index:6; }
.cant i { position:absolute; width:56px; height:56px; border:0 solid currentColor; }
.cant p { position:absolute; left:0; right:0; top:50%; transform:translateY(-50%); text-align:center; font-family:"JetBrains Mono",monospace; font-size:24px; letter-spacing:.08em; text-transform:uppercase; opacity:.8; }
'''

FIT = '''<script>
document.fonts.ready.then(() => {
  for (const p of document.querySelectorAll(".vert p")) {
    const box = p.parentElement; let fs = 460; p.style.fontSize = fs + "px";
    while ((p.scrollWidth > box.clientWidth - 80 || p.offsetHeight > box.clientHeight) && fs > 60) { fs -= 4; p.style.fontSize = fs + "px"; }
  }
});
</script>'''

T = "../../elementos/tinta/"
F = "../../elementos/texturas/"


def cantoneiras(x, y, w, h, rot):
    b = "3px"
    return (f'<div class="cant" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<i style="left:0;top:0;border-left-width:{b};border-top-width:{b}"></i>'
            f'<i style="right:0;top:0;border-right-width:{b};border-top-width:{b}"></i>'
            f'<i style="left:0;bottom:0;border-left-width:{b};border-bottom-width:{b}"></i>'
            f'<i style="right:0;bottom:0;border-right-width:{b};border-bottom-width:{b}"></i>'
            f'<p>{rot}</p></div>')


def story(n, fundo, cls, vert, forma, img, tit, txt, extra=""):
    cx, cy, r = forma
    arq, x, y, w = img
    bg = f'background-image:url({F}{fundo}.jpg)' if fundo else ""
    im = f'<img class="img" src="{T}{arq}" style="left:{x}px;top:{y}px;width:{w}px">' if arq else ""
    tx = f'<p class="txt">{txt}</p>' if txt else ""
    return f'''<section class="s {cls}" id="s{n}" style="{bg}">
  <div class="vert"><p>{vert}</p></div>
  <div class="forma" style="left:{cx - r}px;top:{cy - r}px;width:{2 * r}px;height:{2 * r}px"></div>
  {im}
  <h2 class="tit">{tit}</h2>
  {tx}
  {extra}
</section>'''


S = [
    # 1 · post novo, com o espaço da figurinha do post
    story(1, "ruido", "", "novo", (1060, 820, 220), ("lirios-ramo-ret.png", 700, 600, 300),
          "Post novo: vale a pena ter um site <i>em 2026?</i>", "",
          cantoneiras(380, 1100, 620, 600, "post aqui")),
    # 2 · o teste: pergunta pra IA
    story(2, "pincel", "claro", "teste", (1080, 900, 330), ("flores-tinta-ret.png", 520, 560, 520),
          "Faz um teste <i>agora.</i>",
          "Pergunta pra uma IA onde encontrar o que você vende perto de você. <b>Ela te indicou?</b>"),
    # 3 · por que às vezes não indica
    story(3, "parede", "", "ia", (1000, 960, 300), ("estrelas-ret.png", 700, 520, 300),
          "Se não indicou, <i>tem motivo.</i>",
          "A IA responde com o que está escrito na internet. Stories some em 24 horas, e o que está no direct só quem pergunta vê. <b>Site fica lá, todo dia.</b>"),
    # 4 · chamada
    story(4, None, "azul", "direct", (1060, 1000, 320), (None, 0, 0, 0),
          "Quer <i>aparecer?</i>",
          "O post completo está no feed. E se quiser um site que te coloca no mapa, <b>me chama no direct.</b>"),
]

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}{FIT}</body></html>'''
open("site-2026.html", "w").write(html)
