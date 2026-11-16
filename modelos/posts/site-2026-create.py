"""Carrossel "ainda vale a pena ter um site em 2026?" no estilo das referências de 2026-11-16 (pôster
"CREATE" + texturas de pincel, parede, ruído e grunge): fundo com textura em cinza, uma palavra gigante
em serifa na vertical, o ponto azul grande saindo da borda (no lugar da forma roxa), a imagem em tinta
clara por cima; título no alto e texto embaixo, em Inter Tight (legível), sem cabeçalho. Fundos: `elementos/texturas/*.jpg`.
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
.tit { left:360px; width:656px; top:110px; text-align:center; text-wrap:balance; font-family:"Inter Tight",sans-serif; font-weight:800; font-size:68px; line-height:1.04; letter-spacing:-.03em; z-index:5; }
.txt { left:400px; width:576px; bottom:100px; text-align:center; text-wrap:balance; font-family:"Inter Tight",sans-serif; font-weight:500; font-size:34px; line-height:1.36; letter-spacing:-.01em; z-index:5; padding-top:22px; border-top:3px solid currentColor; }
.txt b { font-weight:800; color:var(--blue); margin-right:8px; }
.s:not(.claro) .txt b { color:var(--claro); }
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


def slide(n, fundo, claro, vert, forma, img, tit, texto, extra=""):
    """Grade fixa em todos os slides: título no alto da coluna da direita, imagem no meio, texto embaixo.
    forma: (cx, cy, r) do ponto grande; img: (arquivo, left, top, width)."""
    cx, cy, r = forma
    arq, x, y, w = img
    return f'''<section class="s {"claro" if claro else ""}" id="s{n}" style="background-image:url({F}{fundo}.jpg)">
  <div class="vert"><p>{vert}</p></div>
  <div class="forma" style="left:{cx - r}px;top:{cy - r}px;width:{2 * r}px;height:{2 * r}px"></div>
  <img class="img" src="{T}{arq}" style="left:{x}px;top:{y}px;width:{w}px">
  <h2 class="tit">{tit}</h2>
  <p class="txt">{texto}</p>
  {extra}
</section>'''


S = [
    slide(1, "ruido", False, "2026?", (1010, 600, 330), ("lirios-faixa-ret.png", 420, 330, 520),
          "Ainda vale a pena ter um site em 2026?",
          "Resposta curta: vale. Mas não do jeito que todo mundo fazia. Arrasta →",
          ESTRELA.format(p="left:980px;top:1040px;color:var(--cream)")),
    slide(2, "pincel", True, "antes", (1080, 640, 300), ("foco-ret.png", 380, 480, 640),
          "Antigamente, site era feito por fazer.",
          "Era item de lista: ter pra dizer que tinha. Uma página com logo, “quem somos” e um telefone. Ninguém pensava em quem ia entrar."),
    slide(3, "parede", False, "ruim", (1000, 700, 300), ("queda-ret.png", 380, 300, 720),
          "Hoje, sobra site ruim.",
          "Abre devagar no celular, não mostra o preço, esconde o WhatsApp. O cliente não acha o que veio buscar e volta pro Google."),
    slide(4, "rabisco-cinza", True, "capta", (1110, 600, 250), ("cisnes-ret.png", 340, 640, 440),
          "Vitrine só mostra. Site único capta.",
          "Um site feito pro seu cliente tira a dúvida e leva ao próximo passo. No senerine.dev, a primeira tela já mostra o que eu faço, quem faz e o botão do WhatsApp.",
          '<div class="cel" style="left:760px;top:330px;width:260px;rotate:5deg"><img src="../../elementos/senerine/m-hero.png"></div>'),
    slide(5, "grunge", False, "rua", (980, 700, 300), ("cavalo-ret.png", 330, 420, 720),
          "A internet é a rua mais movimentada.",
          "Todo mundo passa por ela: pesquisa, compara, pergunta. O perfil é uma banca na calçada. O site é o seu endereço, aberto de madrugada."),
    slide(6, "pincel-escuro", False, "ia", (1060, 740, 300), ("andorinhas-ret.png", 560, 440, 440),
          "Seu cliente não pesquisa só no Google. Pergunta pra IA.",
          "“Onde tem uma barbearia boa aqui perto?” A IA responde com o que encontra escrito na internet. Se você só existe no stories, fica difícil te achar."),
    slide(7, "pincel", True, "apareça", (1040, 700, 280), ("camera-ret.png", 420, 440, 560),
          "Não basta existir. Você precisa aparecer.",
          "<b>01</b> Ser encontrado na busca.<br><b>02</b> Ser lido pelo Google e pela IA.<br><b>03</b> Convencer quem chega."),
    slide(8, "ruido", False, "trabalho", (1000, 560, 330), ("leoes-ret.png", 330, -40, 720),
          "Esse é o meu trabalho.",
          "Senerine.dev é um estúdio digital autoral: sites e aplicações pra serem encontrados, entendidos e usados. Me chama no direct. E manda pra quem acha que site já era.",
          ESTRELA.format(p="left:980px;top:1040px;color:var(--cream)")),
]

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}{FIT}</body></html>'''
open("site-2026-create.html", "w").write(html)
