"""Carrossel "ainda vale a pena ter um site em 2026?" no estilo da referência "Halftone Poster Design"
(2026-11-16): cada slide é um pôster. Manchete condensada na largura toda, faixa fina com texto miúdo
em duas colunas e o ponto no meio, e um quadro grande com a imagem em retícula. O azul do ponto é a
única cor chapada, por baixo da retícula (como os óculos vermelhos da referência).
Imagens em retícula: `python3 ../reticula.py nome --passo N` gera `<nome>-ret.png`.
8 slides 1080x1440. Gerar: python3 site-2026-poster.py && node ../render.mjs site-2026-poster.html saida 1080 1440 8"""

CSS = r'''
:root { --cream:#ebe7dc; --ink:#121112; --blue:#0a63b2; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; }
.s { position:relative; width:1080px; height:1440px; overflow:hidden; background:var(--cream); color:var(--ink); }
.s > * { position:absolute; }
.s.preto { background:var(--ink); color:var(--cream); }
.h { left:48px; right:48px; top:52px; height:330px; display:flex; align-items:flex-end; }
.h p { font-family:"Anton",sans-serif; text-transform:uppercase; line-height:1.02; letter-spacing:-.01em; color:var(--blue); white-space:nowrap; }
.s.preto .h p { color:var(--cream); }
.faixa { left:48px; right:48px; top:404px; height:172px; border-top:3px solid currentColor; border-bottom:3px solid currentColor;
  display:grid; grid-template-columns:1fr 92px 1fr; gap:28px; align-items:center; padding:0 2px; }
.faixa p { font-family:"JetBrains Mono",monospace; font-size:21px; line-height:1.38; text-align:justify; hyphens:auto; }
.faixa p:last-child { text-align:justify; }
.faixa i { width:64px; height:64px; border-radius:50%; background:var(--blue); justify-self:center; }
.quadro { left:48px; top:600px; width:984px; height:792px; overflow:hidden; border:3px solid currentColor; }
.quadro > * { position:absolute; }
.quadro .img { mix-blend-mode:multiply; z-index:2; }
.s.preto .quadro .img { filter:invert(1); mix-blend-mode:screen; }
.quadro .dot { border-radius:50%; background:var(--blue); z-index:1; }
.cel { z-index:3; border:8px solid var(--ink); border-radius:40px; overflow:hidden; background:var(--ink); }
.cel img { display:block; width:100%; }
.grain { inset:0; z-index:9; pointer-events:none; mix-blend-mode:multiply; opacity:.16;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"); }
.s.preto .grain { mix-blend-mode:screen; opacity:.1; }
'''

# encaixa cada manchete na largura e na altura da caixa (como a referência: a palavra ocupa o pôster)
FIT = '''<script>
document.fonts.ready.then(() => {
  for (const p of document.querySelectorAll(".h p")) {
    const box = p.parentElement; let fs = 420;
    p.style.fontSize = fs + "px";
    while ((p.scrollWidth > box.clientWidth || p.offsetHeight > box.clientHeight) && fs > 40) { fs -= 2; p.style.fontSize = fs + "px"; }
  }
});
</script>'''

T = "../../elementos/tinta/"
U = "../../elementos/senerine/"


def poster(n, cls, linhas, esq, dir, img, dot, extra=""):
    """img: (arquivo, left, top, width) dentro do quadro; dot: (cx, cy, r) do ponto azul por baixo."""
    arq, x, y, w = img
    cx, cy, r = dot
    return f'''<section class="s {cls}" id="s{n}">
  <div class="h"><p>{"<br>".join(linhas)}</p></div>
  <div class="faixa"><p>{esq}</p><i></i><p>{dir}</p></div>
  <div class="quadro">
    <div class="dot" style="left:{cx - r}px;top:{cy - r}px;width:{2 * r}px;height:{2 * r}px"></div>
    <img class="img" src="{T}{arq}" style="left:{x}px;top:{y}px;width:{w}px">
    {extra}
  </div>
  <div class="grain"></div>
</section>'''


S = [
    poster(1, "", ["ainda vale a pena", "ter um site", "em 2026?"],
           "Resposta curta: vale. Todo mundo já tem perfil, link na bio e WhatsApp. Então pra que site?",
           "Porque o jeito de procurar mudou, e o site de antes não acompanhou. Arrasta.",
           ("lirios-faixa-ret.png", -309, -895, 1550), (368, 313, 170)),
    poster(2, "preto", ["antigamente,", "site era", "por fazer."],
           "Site era item de lista: ter pra dizer que tinha. Uma página com logo, “quem somos” e um telefone.",
           "Ninguém pensava em quem ia entrar, nem no que essa pessoa queria fazer ali. Faltava foco.",
           ("foco-ret.png", -109, -61, 1222), (295, 402, 100)),
    poster(3, "", ["hoje, sobra", "site ruim."],
           "Abre devagar no celular. Não mostra o preço. Esconde o WhatsApp lá embaixo. Não diz o que faz logo de cara.",
           "A pessoa não acha o que veio buscar e volta pro Google. O site existe, mas não trabalha.",
           ("queda-ret.png", -313, -370, 1717), (520, 420, 230)),
    poster(4, "preto", ["vitrine mostra.", "site único capta."],
           "Vitrine mostra e espera alguém entrar. Um site feito pro seu cliente tira a dúvida antes da pergunta e leva ao próximo passo.",
           "Foi o que eu fiz no senerine.dev: na primeira tela, você sabe o que eu faço, vê quem faz e chama no WhatsApp com um toque.",
           ("cisnes-ret.png", 0, 40, 736), (373, 420, 60),
           f'<div class="cel" style="left:630px;top:60px;width:300px;rotate:4deg"><img src="{U}m-hero.png"></div>'),
    poster(5, "", ["a internet é a rua", "mais movimentada."],
           "Todo mundo passa por ela: pesquisando, comparando, perguntando. O perfil é uma banca na calçada, com as regras de outro.",
           "O site é o seu endereço: seu domínio, do seu jeito, aberto de madrugada, no feriado, no domingo.",
           ("cavalo-ret.png", -46, -159, 1074), (519, 378, 170)),
    poster(6, "preto", ["seu cliente", "pergunta pra ia."],
           "Ele não pesquisa só no Google. Pergunta pro ChatGPT, pro Claude: “onde tem uma barbearia boa aqui perto?”",
           "A IA responde com o que encontra escrito na internet. Se o que você faz só existe no stories e no direct, fica difícil ela te achar.",
           ("andorinhas-ret.png", 168, -84, 665), (489, 470, 130)),
    poster(7, "", ["não basta existir.", "precisa aparecer."],
           "Aparecer, hoje, é: 01 ser achado quando alguém pesquisa; 02 estar escrito de um jeito que o Google e a IA conseguem ler.",
           "03 convencer em segundos quem chega. Não é ter mais post. É ter um lugar que trabalha por você.",
           ("camera-ret.png", -48, -127, 1079), (258, 632, 150)),
    poster(8, "preto", ["esse é o meu", "trabalho."],
           "Senerine.dev é um estúdio digital autoral. Faço sites e aplicações pensados pra serem encontrados, entendidos e usados.",
           "Me chama no direct. E manda pra quem acha que site já era.",
           ("leoes-ret.png", -55, -566, 1101), (835, 406, 110)),
]

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}{FIT}</body></html>'''
open("site-2026-poster.html", "w").write(html)
