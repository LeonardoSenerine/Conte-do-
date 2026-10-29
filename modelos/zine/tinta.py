"""Converte cada imagem em tinta preta com alfa (fundo de papel some), pra colar sobre o papel do zine."""
from PIL import Image, ImageFilter, ImageOps
import sys
U = "../../elementos/originais/"
jobs = {  # nome: (arquivo, preto, branco)
    "menino": (U + "menino.jpg", 40, 200),
    "pressa": (U + "pressa.jpg", 60, 190),
    "tvs":    (U + "tvs.jpg", 70, 195),
    "flor":   (U + "flor.jpg", 40, 200),
    "fim":    (U + "fim.jpg", 40, 205),
    "mundo":  (U + "mundo.jpg", 40, 200),
    "leo":    (U + "leonardo-recorte.png", 50, 170),
}
for name, (f, lo, hi) in jobs.items():
    src = Image.open(f)
    if src.mode in ("RGBA", "LA"):
        bg = Image.new("RGB", src.size, "white"); bg.paste(src, mask=src.split()[-1]); src = bg
    g = src.convert("L")
    if name in ("tvs", "pressa", "fim"):
        g = g.filter(ImageFilter.MedianFilter(3))  # tira o chiado do papel original
    if name == "leo":
        g = ImageOps.autocontrast(g, cutoff=2)
    a = g.point(lambda v: 255 if v <= lo else 0 if v >= hi else int(255 * (hi - v) / (hi - lo)))
    out = Image.new("RGBA", g.size, (17, 16, 17, 0)); out.putalpha(a)
    out.save(f"../../elementos/tinta/{name}.png"); print(name, g.size)
