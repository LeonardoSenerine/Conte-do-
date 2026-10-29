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
    # post "modelo pronto passa batido"
    "toile-flores":      (U + "toile-flores.jpg", 40, 210),
    "pele-cobra":        (U + "pele-cobra.jpg", 40, 200),
    "passaros-borrados": (U + "passaros-borrados.jpg", 30, 235),
    "ornamento":         (U + "ornamento.jpg", 60, 200),
    "leoes":             (U + "leoes.jpg", 50, 215),
    "borboletas":        (U + "borboletas.jpg", 50, 215),
    # modelo pronto, versão com a primeira leva (nanquim e faixas)
    "tecido-floral":     (U + "tecido-floral.jpg", 70, 200),
    "lirios-faixa":      (U + "lirios-faixa.jpg", 40, 215),
    "mulher-pombas":     (U + "mulher-pombas.jpg", 40, 215),
    "videira":           (U + "videira.jpg", 40, 220),
    "tigre-faixa":       (U + "tigre-faixa.jpg", 60, 245),
    "peonias-faixa":     (U + "peonias-faixa.jpg", 30, 240),
    "cobra-fumaca":      (U + "cobra-fumaca.jpg", 40, 225),
    "cobra-escura":      (U + "cobra-escura.jpg", 40, 220),
    "caligrafia":        (U + "caligrafia.jpg", 50, 200),
    "flores-fluidas":    (U + "flores-fluidas.jpg", 15, 245),  # fundo inteiro do slide "estampa"
    "vilao":             (U + "vilao.jpg", 60, 200),          # homem de terno em 1-bit, "não é vilão"
}
# cor própria da imagem que não pode sumir no limiar: nome: (teste por pixel, cor nova ou None pra manter a original)
AZUL = (10, 99, 178)
COR = {
    "cabeca-azul": (lambda r, g, b: b - r > 40, None),  # trocar pelo azul do ponto ficou "bem ruim"
    "leitor": (lambda r, g, b: r - g > 80, AZUL),        # vermelho fora da marca
}
# originais pequenos (uns 600 px) que entram grandes no slide: dobra com Lanczos antes do limiar,
# senão a borda da tinta sai serrilhada e mole
DOBRO = {"cabeca-azul", "multidao", "cabeca-aberta", "lampada", "megafone", "botas", "washington", "leitor",
         "reverencia", "toile-flores", "pele-cobra", "passaros-borrados", "ornamento", "leoes", "borboletas",
         "tecido-floral", "lirios-faixa", "mulher-pombas", "videira", "tigre-faixa", "peonias-faixa",
         "cobra-fumaca", "cobra-escura", "caligrafia", "flores-fluidas", "vilao"}
for name, (f, lo, hi) in jobs.items():
    if len(sys.argv) > 1 and name not in sys.argv[1:]:
        continue  # python3 tinta.py nome1 nome2 converte só esses
    src = Image.open(f)
    if src.mode in ("RGBA", "LA"):
        bg = Image.new("RGB", src.size, "white"); bg.paste(src, mask=src.split()[-1]); src = bg
    if name in DOBRO:
        src = src.convert("RGB")
        src = src.resize((src.width * 2, src.height * 2), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2))
    g = src.convert("L")
    if name in ("tvs", "pressa", "fim"):
        g = g.filter(ImageFilter.MedianFilter(3))  # tira o chiado do papel original
    if name in ("leo", "tecido-floral"):
        g = ImageOps.autocontrast(g, cutoff=2)
    a = g.point(lambda v: 255 if v <= lo else 0 if v >= hi else int(255 * (hi - v) / (hi - lo)))
    out = Image.new("RGBA", g.size, (17, 16, 17, 0)); out.putalpha(a)
    if name in COR:
        rgb, px = src.convert("RGB").load(), out.load()
        for y in range(g.size[1]):
            for x in range(g.size[0]):
                teste, cor = COR[name]
                if teste(*rgb[x, y]): px[x, y] = (cor or rgb[x, y]) + (255,)
    out.save(f"../elementos/tinta/{name}.png"); print(name, g.size)
