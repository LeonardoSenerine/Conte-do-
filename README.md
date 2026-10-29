# senerine-conteudo

Arsenal de conteúdo do [@senerine.dev](https://instagram.com/senerine.dev): referências, elementos, ideias e os modelos que geram os posts.

```
CLAUDE.md      roteador: qual guia ler para cada pedido
COMO-PEDIR.md  como pedir um post, stories, reels...
formatos/      um guia por formato: padrão, especificações, o que funciona e o que não funciona
marca/         regras da marca e sistema visual
ideias/        o arsenal, por formato, e o banco de ganchos
referencias/   referências por formato, com notas
elementos/     imagens prontas para usar (originais/, tinta/, senerine/)
modelos/       geradores por formato (posts/, stories/, reels/) + render.mjs e tinta.py
fontes/        Anton, Bodoni Moda, Instrument Serif, Inter Tight, JetBrains Mono (OFL)
postados/      o que já foi feito, por formato
```

## Gerar um post

```bash
cd modelos/posts
python3 zine.py                                     # gera zine.html
node ../render.mjs zine.html ../../saida/zine 1080 1350 7
```

Carrosséis com uma linha que atravessa os slides usam o modo panorama:

```bash
python3 linha-continua.py
node ../render.mjs caro.html ../../saida/caro 1080 1350 8 panorama
```

Reels: veja `formatos/reels.md`.

Precisa de Python 3 com Pillow, Node com Playwright (Chromium) e ffmpeg para os reels.

## Imagens de terceiros

As imagens em `elementos/originais/` vieram de referências visuais (Pinterest e afins) e pertencem aos seus autores.
Estão aqui como material de estudo; ao publicar, credite o autor quando conhecido.
