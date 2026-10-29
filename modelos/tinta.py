"""Converte cada imagem em tinta preta com alfa (fundo de papel some), pra colar sobre o papel do zine."""
from PIL import Image, ImageFilter, ImageOps
import sys
U = "../elementos/originais/"
jobs = {  # nome: (arquivo, preto, branco)
    "menino": (U + "menino.jpg", 40, 200),
    "pressa": (U + "pressa.jpg", 60, 190),
    "tvs":    (U + "tvs.jpg", 70, 195),
    "flor":   (U + "flor.jpg", 40, 200),
    "fim":    (U + "fim.jpg", 40, 205),
    "mundo":  (U + "mundo.jpg", 40, 200),
    "leo":    (U + "leonardo-recorte.png", 50, 170),
    # post "ninguém lê o seu site"
    "cabeca-azul":   (U + "cabeca-azul.jpg", 40, 190),
    "multidao":      (U + "multidao.jpg", 50, 215),
    "cabeca-aberta": (U + "cabeca-aberta.jpg", 40, 215),
    "lampada":       (U + "lampada.jpg", 40, 225),
    "megafone":      (U + "megafone.jpg", 40, 200),
    "botas":         (U + "botas.jpg", 40, 215),
    "washington":    (U + "washington.jpg", 70, 225),
    "leitor":        (U + "leitor.jpg", 40, 200),
    "reverencia":    (U + "reverencia.jpg", 40, 215),
}
# cor própria da imagem que vira o azul do ponto (em vez de sumir no limiar): nome: teste por pixel
COR = {
    "cabeca-azul": lambda r, g, b: b - r > 40,
    "leitor": lambda r, g, b: r - g > 80,
}
AZUL = (10, 99, 178)
for name, (f, lo, hi) in jobs.items():
    if len(sys.argv) > 1 and name not in sys.argv[1:]:
        continue  # python3 tinta.py nome1 nome2 converte só esses
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
    if name in COR:
        rgb, px = src.convert("RGB").load(), out.load()
        for y in range(g.size[1]):
            for x in range(g.size[0]):
                if COR[name](*rgb[x, y]): px[x, y] = AZUL + (255,)
    out.save(f"../elementos/tinta/{name}.png"); print(name, g.size)
