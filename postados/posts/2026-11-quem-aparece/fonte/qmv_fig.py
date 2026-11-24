import numpy as np, scipy.ndimage as nd, sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
a = np.asarray(Image.open(src).convert('RGB')).astype(float)
H, W, _ = a.shape
strict = (a[..., 2] < 26) & (a[..., 0] < 20)
strict[:1050] = False
lab, n = nd.label(strict)
k = np.argmax(nd.sum(strict, lab, range(1, n + 1))) + 1
core = nd.binary_fill_holes(lab == k)
core = nd.binary_closing(core, iterations=4)
loose = (a[..., 2] < 62) & (a[..., 0] < 20)
m = nd.binary_fill_holes(loose & nd.binary_dilation(core, iterations=7) | core)
m = nd.binary_opening(m, iterations=2)
m = nd.binary_closing(m, iterations=3)
m = nd.binary_fill_holes(m)
ys, xs = np.where(m)
y0, y1, x0, x1 = ys.min(), H, xs.min(), xs.max() + 1
m = m[y0 - 10:y1, x0 - 10:x1 + 10].astype(float)
# alisa o contorno e amplia 1.3x (2x da arte final)
S = 1.30
f = nd.gaussian_filter(m, 2.2)
f = nd.zoom(f, S, order=3)
alpha = np.clip((f - 0.5) * 3.2 + 0.5, 0, 1)
h, w = alpha.shape
# figura: quase preta, com luz azul na borda (mais forte dos lados) e tecido sutil
inner = nd.gaussian_filter(alpha, 9)
rim = np.clip(alpha - inner, 0, 1) * 2.4
yy = np.linspace(0, 1, h)[:, None]
rng = np.random.default_rng(3)
tex = nd.gaussian_filter(rng.normal(0, 1, (h, w)), 0.8) * 2.2
r = 3 + tex + rim * 30
g = 5 + tex + rim * 70 + yy * 2
b = 12 + tex * 1.6 + rim * 230 + yy * 4
rgba = np.dstack([np.clip(r, 0, 255), np.clip(g, 0, 255), np.clip(b, 0, 255), alpha * 255]).astype('uint8')
Image.fromarray(rgba).save(out + '/figura.png')
# sombras: a mesma silhueta em azul, com linhas de varredura e deslocamento horizontal (interferência)
gs = nd.zoom(alpha, 0.86, order=1)
gh, gw = gs.shape
pad = 60
ga = np.zeros((gh, gw + 2 * pad))
shift = nd.gaussian_filter1d(rng.normal(0, 1, gh), 3) * 9 + (rng.random(gh) < .05) * rng.normal(0, 14, gh)
for y in range(gh):
    s = int(round(shift[y])); ga[y, pad + s:pad + s + gw] = gs[y]
ga = nd.gaussian_filter(ga, (0.6, 2.2))
scan = 0.62 + 0.38 * ((np.arange(gh) % 6) < 3)
ga *= scan[:, None]
noise = nd.gaussian_filter(rng.random(ga.shape), (0.5, 3))
ga *= 0.75 + 0.5 * noise
gr = np.dstack([np.full(ga.shape, 24), np.full(ga.shape, 62), np.full(ga.shape, 210), np.clip(ga, 0, 1) * 200]).astype('uint8')
Image.fromarray(gr).save(out + '/sombra.png')
print('figura', w, h, 'sombra', gr.shape[1], gr.shape[0], 'crop', x0, y0)
