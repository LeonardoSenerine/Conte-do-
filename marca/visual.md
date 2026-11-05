# Sistema visual

## Cores
| Nome | Hex | Uso |
|---|---|---|
| Azul do ponto | `#0a63b2` | assinatura, destaque, linhas, risografia |
| Azul claro | `#4aa3ea` / `#5aa3e8` / `#7cbcf2` | brilho do ponto, texto azul sobre fundo escuro |
| Preto | `#1e1d1e` (fundo) · `#121112` (tinta) | |
| Papel | `#e8e6e0` | fundo do zine |
| Off-white | `#f2efea` | texto sobre escuro, cartões |
| Pele | `#d99278` | ênfase quente (na linguagem Senerine) |

Evitar vermelho.

## O ponto
O ponto azul aceso é a assinatura: fecha títulos (`.dot`), vira indicador de progresso, carrega a foto do Leonardo, termina as linhas que atravessam os slides. Reaproveitar antes de inventar outro recurso.

## Linguagem 1 · Zine (a preferida até agora)
Nomes do estilo: **estética zine / fanzine**, **xerox art** (photocopy aesthetic) com cor de **risografia** (riso print) e imagens em **bitmap / 1-bit** (threshold, alto contraste). Para buscar referência: `xerox art`, `photocopy aesthetic`, `risograph poster`, `zine collage`, `1-bit image`, `threshold art`, `stencil photo`, `brutalist editorial`.
- Papel `#e8e6e0` com grão (SVG feTurbulence em multiply, opacidade ~0.28).
- Imagens em **tinta preta sem fundo** (`elementos/tinta/`, `mix-blend-mode:multiply`).
- Um único azul, como segunda cor de risografia, também em multiply (ponto atrás da imagem, palavra da manchete).
- Manchete em **Anton** maiúscula; contraste com **Bodoni Moda** itálica 700 a 800 ou **Instrument Serif** (itálico na palavra-chave); texto corrido e rótulos em **JetBrains Mono**.
- Recursos: **nota com linha** (texto no papel sobre um fio, linha fina até o detalhe da imagem, ponto azul na ponta; preferida desde o zine nº 02), papelzinho colado com fita (evitar em série: "sem graça"), carimbo azul inclinado, etiqueta preta com texto claro (estilo recorte), palavra riscada em azul.
- Atenção: Anton com `line-height` baixo esconde acentos e cedilha (É, Ó, Ç). Use `line-height:1` nas linhas com acento.

## Linguagem 2 · Senerine (a do site)
Nomes do estilo: **editorial minimalista** com **tipografia suíça** (grade rígida, sem serifa, muito respiro). O carrossel "caro e barato" também é minimalista editorial, só que no papel do zine.
- Fundo `#1e1d1e`, Inter Tight bold com `letter-spacing:-.055em`, JetBrains Mono nos rótulos, ponto azul fechando o título.
- Estrutura de grade rígida: margem 72 px, cabeçalho com rótulo e fólio ("01 / 05"), régua, cartão de imagem, título, texto, rodapé com logo e "arrasta →".
- Imagens: **capturas reais** do site e dos projetos (`elementos/senerine/`), nunca mockups inventados.

## Linguagem 3 · Editorial (em teste, referência Herground)
- Uma frase curta e com opinião por slide, **Inter Tight 800 em minúsculas**, entrelinha 0.9, `letter-spacing:-.06em`.
- A palavra-chave em **Instrument Serif itálica**, um pouco maior: azul no creme, azul claro no preto, preto no azul.
- Três fundos alternando pela grade: creme `#f2efea`, preto `#1e1d1e`, azul `#0a63b2`. Metade dos slides com imagem grande do banco (versão `-claro` no fundo escuro), metade só tipografia.
- Rodapé de conteúdo: texto pequeno em caixa alta (o complemento da frase) e a seta →. Nada de rótulo, fólio nem régua.

## Fontes
Todas em `fontes/fontes.css` (OFL). No HTML do modelo: `<link rel="stylesheet" href="../../fontes/fontes.css">`.
