"""Recorta a foto do Leonardo (elementos/senerine/leo-cut.png, fundo branco com círculo azul) e gera a versão
preto e branco de alto contraste com grão, sem fundo: elementos/senerine/leo-pb.png (e o olho em leo-olho.png).
Rodar da raiz do repositório: python3 modelos/recorte-leo.py"""
import numpy as np, scipy.ndimage as nd
from PIL import Image, ImageOps

im = Image.open('elementos/senerine/leo-cut.png').convert('RGB')
a = np.asarray(im).astype(int)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
cand = ((r > 200) & (g > 205) & (b > 205) & (abs(r - b) < 45)) | ((b > 120) & (b - r > 70))
lab, n = nd.label(cand)
edge = set(lab[0, :]) | set(lab[:1150, 0]) | set(lab[:1150, -1])
edge.discard(0)
fg = nd.binary_fill_holes(~nd.binary_opening(np.isin(lab, list(edge)), iterations=1))
lab2, n2 = nd.label(fg)
fg = lab2 == (np.argmax(nd.sum(fg, lab2, range(1, n2 + 1))) + 1)
alpha = np.clip((nd.gaussian_filter(fg.astype(float), 1.0) - .5) * 2.2 + .5, 0, 1)
gray = np.asarray(ImageOps.grayscale(im)).astype(float)
gray = np.clip((gray - 128) * 1.35 + 122, 0, 255)
gray = np.clip(gray + np.random.default_rng(1).normal(0, 9, gray.shape), 0, 255)
Image.fromarray(np.dstack([gray, gray, gray, alpha * 255]).astype('uint8')).save('elementos/senerine/leo-pb.png')
Image.fromarray(gray.astype('uint8')).crop((400, 615, 670, 765)).save('elementos/senerine/leo-olho.png')
