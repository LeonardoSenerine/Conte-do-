"""Gera a textura de papel impresso (1080x1440) usada por cima dos slides: grão, fibras, uma dobra,
pontinhos de tinta e borda mais escura. Cinza sobre branco, pra usar com mix-blend-mode:multiply
(no fundo escuro, com soft-light). Uso, dentro de modelos/: python3 textura.py"""
import random
from PIL import Image, ImageDraw, ImageFilter, ImageChops

random.seed(7)
W, H = 1080, 1440
base = Image.effect_noise((W, H), 38).point(lambda v: 236 + (v - 128) * .28)  # grão
base = base.filter(ImageFilter.GaussianBlur(.6))

fib = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(fib)
for _ in range(900):  # fibras curtas do papel
    x, y = random.uniform(0, W), random.uniform(0, H)
    dx, dy = random.uniform(-18, 18), random.uniform(-6, 6)
    d.line((x, y, x + dx, y + dy), fill=random.randint(205, 232), width=1)
for _ in range(260):  # pontinhos de tinta perdidos, como xerox
    x, y, r = random.uniform(0, W), random.uniform(0, H), random.uniform(.6, 2.2)
    d.ellipse((x - r, y - r, x + r, y + r), fill=random.randint(40, 120))
fib = fib.filter(ImageFilter.GaussianBlur(.4))

dobra = Image.new("L", (W, H), 255)  # dobra horizontal: sombra de um lado, luz do outro
d = ImageDraw.Draw(dobra)
y0 = int(H * .47)
for k in range(40):
    d.line((0, y0 + k, W, y0 + k - 6), fill=int(255 - 22 * (1 - k / 40) ** 2))
d.line((0, y0 - 1, W, y0 - 7), fill=200, width=1)
dobra = dobra.filter(ImageFilter.GaussianBlur(1.2))

borda = Image.new("L", (W, H), 0)  # borda mais escura
ImageDraw.Draw(borda).rectangle((60, 60, W - 60, H - 60), fill=255)
borda = borda.filter(ImageFilter.GaussianBlur(120)).point(lambda v: 228 + v * 27 // 255)

tex = ImageChops.multiply(ImageChops.multiply(ImageChops.multiply(base, fib), dobra), borda)
tex.point(lambda v: min(255, int(v * 1.04))).save("../elementos/texturas/papel.png", optimize=True)
print("papel.png", tex.size)
