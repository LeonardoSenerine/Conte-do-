# senerine-conteudo

Arsenal de conteúdo do [@senerine.dev](https://instagram.com/senerine.dev): referências, elementos, ideias e os modelos que geram os posts.

```
referencias/   posts e peças de outros perfis que inspiram, com notas do porquê
elementos/     imagens prontas para usar (originais/ e tinta/, já sem fundo)
ideias.md      o arsenal: ganchos, temas e formatos, com status
modelos/       geradores dos posts (HTML + Python) e o render.mjs
fontes/        Anton, Bodoni Moda, Instrument Serif, Inter Tight, JetBrains Mono (OFL)
postados/      o que já foi feito, por tema
```

## Gerar um post

```bash
cd modelos/zine
python3 carrossel.py                                   # gera zine.html
node ../render.mjs zine.html ../../saida/zine 1080 1350 7
```

Para os carrosséis com uma linha que atravessa os slides, use o modo panorama:

```bash
cd modelos/linha-continua
python3 carrossel.py
node ../render.mjs caro.html ../../saida/caro 1080 1350 8 panorama
```

Precisa de Python 3 com Pillow e de Node com Playwright (Chromium).

## Imagens de terceiros

As imagens em `elementos/originais/` vieram de referências visuais (Pinterest e afins) e pertencem aos seus autores.
Estão aqui como material de estudo; ao publicar, credite o autor quando conhecido.
