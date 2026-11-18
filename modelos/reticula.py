"""Passa uma imagem em tinta (PNG com alfa) para retícula de pontos (meio-tom), como impressão barata.
Cada célula da grade vira um ponto cujo tamanho segue a quantidade de tinta ali. Grade girada 45°.
Uso, dentro de modelos/: python3 reticula.py nome [nome...] [--passo 9]  ->  ../elementos/tinta/<nome>-ret.png
"""
import math
import sys
from PIL import Image, ImageDraw, ImageFilter

args = [a for a in sys.argv[1:] if not a.startswith("--")]
passo = 9
if "--passo" in sys.argv:
    passo = int(sys.argv[sys.argv.index("--passo") + 1])
    args.remove(str(passo))

ESCALA = 4  # desenha os pontos 4x maior e reduz no fim, pra borda sair lisa
ANG = math.radians(45)

for nome in args:
    src = Image.open(f"../elementos/tinta/{nome}.png").convert("RGBA")
    a = src.split()[-1].filter(ImageFilter.GaussianBlur(passo / 3))
    w, h = src.size
    out = Image.new("L", (w * ESCALA, h * ESCALA), 0)
    d = ImageDraw.Draw(out)
    c, s = math.cos(ANG), math.sin(ANG)
    diag = int(math.hypot(w, h) / passo) + 2
    for i in range(-diag, diag):
        for j in range(-diag, diag):
            # centro da célula na grade girada
            x = (i * c - j * s) * passo + w / 2
            y = (i * s + j * c) * passo + h / 2
            if not (0 <= x < w and 0 <= y < h):
                continue
            v = a.getpixel((int(x), int(y))) / 255
            if v < .04:
                continue
            r = passo * .72 * math.sqrt(v) * ESCALA
            X, Y = x * ESCALA, y * ESCALA
            d.ellipse((X - r, Y - r, X + r, Y + r), fill=255)
    alpha = out.resize((w, h), Image.LANCZOS)
    res = Image.new("RGBA", (w, h), (17, 16, 17, 0))
    res.putalpha(alpha)
    res.save(f"../elementos/tinta/{nome}-ret.png")
    print(nome, (w, h))
