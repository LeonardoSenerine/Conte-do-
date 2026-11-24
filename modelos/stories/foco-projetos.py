"""Story "menos post, mais projeto" no estilo tipografia expressiva (referência Pinterest de 2026-11-24, só no azul):
letras gigantes atrás da pessoa, papel rasgado em camadas, foto do Leonardo em P&B recortada (modelos/recorte-leo.py),
o olho num pedaço de papel, código de barras, faixa xadrez e o ponto azul fechando a frase.
1 story 1080x1920. Gerar: python3 foco-projetos.py && node ../render.mjs foco-projetos.html saida 1080 1920 1 panorama"""
import random

random.seed(7)
E_ = "../../elementos/"


def rasgado(w, h, amp=14, passo=26):
    """clip-path com as quatro bordas rasgadas"""
    pts = []
    for x in range(0, w + 1, passo):
        pts.append((x, random.uniform(0, amp)))
    for y in range(0, h + 1, passo):
        pts.append((w - random.uniform(0, amp), y))
    for x in range(w, -1, -passo):
        pts.append((x, h - random.uniform(0, amp)))
    for y in range(h, -1, -passo):
        pts.append((random.uniform(0, amp), y))
    return "polygon(" + ",".join(f"{x:.0f}px {y:.0f}px" for x, y in pts) + ")"


def barras(w, h):
    x, out = 0, []
    while x < w:
        bw = random.choice([2, 2, 3, 5, 7])
        if random.random() < .62:
            out.append(f'<rect x="{x}" y="0" width="{bw}" height="{h}"/>')
        x += bw + random.choice([2, 3, 4])
    return f'<svg width="{w}" height="{h}" fill="#121112">{"".join(out)}</svg>'


CSS = r'''
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; height:1920px; overflow:hidden; position:relative; background:#ebe7dd; font-family:"Inter Tight",sans-serif; }
.a { position:absolute; }
.tex { inset:0; width:1080px; height:1920px; object-fit:cover; mix-blend-mode:multiply; opacity:.55; z-index:9; pointer-events:none; }
.azul { background:#0a63b2; }
.foco { font-family:"Anton",sans-serif; color:#f2efea; font-size:560px; line-height:.8; letter-spacing:-.02em; transform:scaleY(1.32); transform-origin:top left; z-index:2; filter:url(#onda); }
.h { font-family:"Anton",sans-serif; line-height:.86; letter-spacing:-.01em; text-transform:uppercase; z-index:6; }
.papel { background:#f4f1ea; z-index:6; box-shadow:0 18px 30px -18px rgba(0,0,0,.45); }
.ponto { display:inline-block; width:.26em; height:.26em; border-radius:50%; background:radial-gradient(circle at 40% 38%, #8fd0ff, #3a9bf0 45%, #0a63b2); box-shadow:0 0 30px rgba(58,155,240,.9); margin-left:.05em; vertical-align:.04em; }
.nota { font-size:35px; line-height:1.36; letter-spacing:-.015em; color:#121112; font-weight:500; }
.nota b { font-weight:700; color:#0a63b2; }
.xadrez { background:conic-gradient(#121112 25%, #f2efea 0 50%, #121112 0 75%, #f2efea 0) 0 0/36px 36px; z-index:5; }
'''

E = []
# filtro de onda leve para as letras gigantes
E.append('<svg width="0" height="0" style="position:absolute"><filter id="onda"><feTurbulence type="fractalNoise" baseFrequency=".006 .02" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="26"/></filter></svg>')
# papel azul rasgado atrás de tudo, com as letras de FOCO
E.append(f'<div class="a azul" style="left:-30px;top:560px;width:1140px;height:1020px;rotate:-3deg;clip-path:{rasgado(1140, 1020, 22, 30)};z-index:1"></div>')
E.append('<p class="a foco" style="left:-14px;top:540px">FOCO</p>')
# faixa xadrez e código de barras
E.append(f'<div class="a xadrez" style="left:0;top:1190px;width:72px;height:300px;clip-path:{rasgado(72, 300, 8, 18)}"></div>')
E.append(f'<div class="a papel" style="left:930px;top:640px;width:110px;height:330px;rotate:2deg;padding:16px 14px;clip-path:{rasgado(110, 330, 7, 16)}"><div style="rotate:90deg;transform-origin:center;width:300px;margin:120px 0 0 -96px">{barras(300, 70)}</div></div>')
# a foto
E.append(f'<img class="a" src="{E_}senerine/leo-pb.png" style="left:90px;top:250px;width:1000px;z-index:4">')
# o olho num pedaço de papel rasgado, no alto à direita
E.append(f'<div class="a papel" style="left:640px;top:300px;width:380px;height:220px;rotate:4deg;padding:14px;clip-path:{rasgado(380, 220, 10, 20)}"><img src="{E_}senerine/leo-olho.png" style="width:100%;height:100%;object-fit:cover;filter:contrast(1.25)"></div>')
# manchete
E.append('<h1 class="a h" style="left:60px;top:270px;font-size:250px;color:#121112;rotate:-3deg">Menos<br><span style="font-size:.78em">post,</span></h1>')
# tira branca com MAIS PROJETO e o ponto
E.append(f'<div class="a papel" style="left:40px;top:1320px;width:1000px;height:190px;rotate:2.5deg;clip-path:{rasgado(1000, 190, 12, 24)}"></div>')
E.append('<p class="a h" style="left:84px;top:1342px;font-size:150px;color:#0a63b2;rotate:2.5deg">mais projeto<span class="ponto"></span></p>')
# nota
E.append(f'<div class="a papel" style="left:60px;top:1515px;width:960px;height:180px;rotate:-1deg;padding:26px 36px;clip-path:{rasgado(960, 180, 9, 22)}"><p class="nota">Tô postando menos, e é de propósito. O tempo agora vai pra <b>qualidade e pros projetos</b>, que não param de chegar. Logo eles aparecem por aqui.</p></div>')
E.append(f'<img class="a tex" src="{E_}texturas/papel.png">')

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(E)}<script>document.fonts.ready.then(() => document.body.dataset.ok = 1)</script></body></html>'''
open("foco-projetos.html", "w").write(html)
