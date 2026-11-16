"""Carrossel "ainda vale a pena ter um site em 2026?" no estilo das referências de 2026-11-16 (pôster
"CREATE" + texturas de pincel, parede, ruído e grunge): fundo com textura em cinza, uma palavra gigante
em serifa na vertical, o ponto azul grande saindo da borda (no lugar da forma roxa), a imagem em tinta
clara por cima e o texto em blocos pequenos com traço. Fundos: `elementos/texturas/*.jpg`.
8 slides 1080x1440. Gerar: python3 site-2026-create.py && node ../render.mjs site-2026-create.html saida 1080 1440 8"""

CSS = r'''
:root { --cream:#ece8de; --ink:#121112; --blue:#0a63b2; --claro:#4aa3ea; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; color:var(--cream); background:var(--ink) center/cover no-repeat; }
.s.claro { color:var(--ink); }
.s > * { position:absolute; }
.vert { left:0; top:0; width:1440px; height:330px; transform-origin:0 0; transform:translate(0,1440px) rotate(-90deg);
  display:flex; align-items:center; justify-content:center; z-index:2; }
.vert p { font-family:"Bodoni Moda",serif; font-weight:700; text-transform:uppercase; line-height:.8; letter-spacing:.01em; color:var(--blue); white-space:nowrap; }
.s:not(.claro) .vert p { color:var(--claro); }
.forma { border-radius:50%; background:var(--blue); z-index:1; }
.img { z-index:3; }
.s:not(.claro) .img { filter:invert(1) contrast(1.1); mix-blend-mode:screen; }
.s.claro .img { mix-blend-mode:multiply; }
.bloco { z-index:5; font-family:"JetBrains Mono",monospace; font-size:22px; line-height:1.42; text-transform:uppercase; letter-spacing:.03em; }
.bloco::after { content:""; display:block; width:28px; height:2px; background:currentColor; margin-top:14px; }
.tit { z-index:5; font-family:"Bodoni Moda",serif; font-style:italic; font-weight:800; line-height:1.02; letter-spacing:-.02em; }
.sobre { color:var(--cream) !important; }
.topo { left:330px; right:56px; top:52px; display:flex; align-items:center; gap:22px; z-index:5; font-family:"JetBrains Mono",monospace; font-size:20px; text-transform:uppercase; letter-spacing:.06em; }
.topo i { flex:1; height:2px; background:currentColor; opacity:.7; }
.estrela { z-index:5; width:46px; height:46px; }
.cel { z-index:4; border:8px solid var(--ink); border-radius:40px; overflow:hidden; background:var(--ink); }
.cel img { display:block; width:100%; }
'''

FIT = '''<script>
document.fonts.ready.then(() => {
  for (const p of document.querySelectorAll(".vert p")) {
    const box = p.parentElement; let fs = 460; p.style.fontSize = fs + "px";
    while ((p.scrollWidth > box.clientWidth - 60 || p.offsetHeight > box.clientHeight) && fs > 60) { fs -= 4; p.style.fontSize = fs + "px"; }
  }
});
</script>'''

T = "../../elementos/tinta/"
F = "../../elementos/texturas/"
ESTRELA = ('<svg class="estrela" style="{p}" viewBox="0 0 46 46"><path d="M23 0 C24 18 28 22 46 23 C28 24 24 28 23 46 '
           'C22 28 18 24 0 23 C18 22 22 18 23 0Z" fill="currentColor"/></svg>')


def slide(n, fundo, claro, vert, forma, img, tit, blocos, extra=""):
    """forma: (cx, cy, r) do ponto grande; img: (arquivo, left, top, width); tit: (texto, left, top, width, tamanho);
    blocos: [(texto, left, top, width, sobre_o_ponto)]"""
    cx, cy, r = forma
    arq, x, y, w = img
    t, tx, ty, tw, ts = tit
    bl = "".join(f'<p class="bloco{" sobre" if s else ""}" style="left:{bx}px;top:{by}px;width:{bw}px">{b}</p>'
                 for b, bx, by, bw, s in blocos)
    return f'''<section class="s {"claro" if claro else ""}" id="s{n}" style="background-image:url({F}{fundo}.jpg)">
  <div class="topo"><span>senerine.dev</span><i></i><span>site em 2026</span></div>
  <div class="vert"><p>{vert}</p></div>
  <div class="forma" style="left:{cx - r}px;top:{cy - r}px;width:{2 * r}px;height:{2 * r}px"></div>
  <img class="img" src="{T}{arq}" style="left:{x}px;top:{y}px;width:{w}px">
  <p class="tit" style="left:{tx}px;top:{ty}px;width:{tw}px;font-size:{ts}px">{t}</p>
  {bl}
  {extra}
</section>'''


S = [
    slide(1, "ruido", False, "2026?", (1010, 330, 400), ("lirios-faixa-ret.png", 300, 300, 640),
          ("Ainda vale a pena ter um site em 2026?", 360, 120, 640, 76),
          [("resposta curta:<br>vale. mas não do<br>jeito que todo<br>mundo fazia.", 760, 1120, 280, False),
           ("arrasta →", 760, 1330, 280, False)],
          ESTRELA.format(p="left:960px;top:980px;color:var(--cream)")),
    slide(2, "pincel", True, "antes", (1060, 1150, 380), ("foco-ret.png", 330, 520, 720),
          ("Antigamente, site era feito por fazer.", 360, 120, 640, 76),
          [("item de lista:<br>ter pra dizer<br>que tinha.", 360, 1000, 300, False),
           ("logo, “quem somos”<br>e um telefone.<br>ninguém pensava<br>em quem ia entrar.", 720, 1050, 300, True)]),
    slide(3, "parede", False, "ruim", (980, 1250, 360), ("queda-ret.png", 280, 330, 900),
          ("Hoje, sobra site ruim.", 360, 120, 640, 88),
          [("abre devagar no<br>celular. não mostra<br>o preço. esconde<br>o whatsapp.", 360, 1080, 320, False),
           ("o cliente não acha<br>o que veio buscar<br>e volta pro google.", 730, 1150, 300, True)]),
    slide(4, "rabisco-cinza", True, "capta", (1110, 180, 300), ("cisnes-ret.png", 330, 720, 470),
          ("Vitrine só mostra. Site único capta.", 360, 120, 420, 70),
          [("um site feito pro<br>seu cliente tira a<br>dúvida e leva ao<br>próximo passo.", 360, 1170, 320, False),
           ("no senerine.dev:<br>o que eu faço, quem<br>faz e o whatsapp,<br>na primeira tela.", 730, 1170, 300, False)],
          '<div class="cel" style="left:740px;top:400px;width:280px;rotate:5deg"><img src="../../elementos/senerine/m-hero.png"></div>'),
    slide(5, "grunge", False, "rua", (1000, 1000, 420), ("cavalo-ret.png", 300, 480, 760),
          ("A internet é a rua mais movimentada.", 360, 120, 640, 76),
          [("todo mundo passa<br>por ela: pesquisa,<br>compara, pergunta.", 360, 1150, 320, False),
           ("o perfil é uma banca<br>na calçada. o site<br>é o seu endereço,<br>aberto de madrugada.", 720, 1150, 320, True)]),
    slide(6, "pincel-escuro", False, "ia", (1060, 400, 360), ("andorinhas-ret.png", 620, 560, 430),
          ("Seu cliente não pesquisa só no Google. Pergunta pra IA.", 360, 120, 580, 64),
          [("“onde tem uma<br>barbearia boa<br>aqui perto?”", 360, 640, 300, False),
           ("a ia responde com<br>o que encontra<br>escrito na internet.<br>se você só existe<br>no stories, fica<br>difícil te achar.", 360, 1000, 300, False)]),
    slide(7, "pincel", True, "apareça", (980, 1180, 380), ("camera-ret.png", 420, 460, 620),
          ("Não basta existir. Você precisa aparecer.", 360, 120, 640, 76),
          [("01 ser achado<br>quando alguém<br>pesquisa.", 360, 1150, 280, False),
           ("02 ser lido pelo<br>google e pela ia.<br>03 convencer<br>quem chega.", 700, 1150, 320, True)]),
    slide(8, "ruido", False, "trabalho", (1000, 360, 420), ("leoes-ret.png", 290, 100, 800),
          ("Esse é o meu trabalho.", 360, 120, 560, 88),
          [("senerine.dev é um<br>estúdio digital<br>autoral. sites e<br>aplicações pra serem<br>encontrados.", 360, 1060, 320, False),
           ("me chama no direct.<br>e manda pra quem<br>acha que site<br>já era.", 730, 1060, 300, False)],
          ESTRELA.format(p="left:960px;top:1330px;color:var(--cream)")),
]

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}{FIT}</body></html>'''
open("site-2026-create.html", "w").write(html)
