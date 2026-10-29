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
- Papel `#e8e6e0` com grão (SVG feTurbulence em multiply, opacidade ~0.28).
- Imagens em **tinta preta sem fundo** (`elementos/tinta/`, `mix-blend-mode:multiply`).
- Um único azul, como segunda cor de risografia, também em multiply (ponto atrás da imagem, palavra da manchete).
- Manchete em **Anton** maiúscula; contraste com **Bodoni Moda** itálica 700 a 800 ou **Instrument Serif** (itálico na palavra-chave); texto corrido e rótulos em **JetBrains Mono**.
- Recursos: papelzinho colado com fita, carimbo azul inclinado, etiqueta preta com texto claro (estilo recorte), palavra riscada em azul.
- Atenção: Anton com `line-height` baixo esconde acentos e cedilha (É, Ó, Ç). Use `line-height:1` nas linhas com acento.

## Linguagem 2 · Senerine (a do site)
- Fundo `#1e1d1e`, Inter Tight bold com `letter-spacing:-.055em`, JetBrains Mono nos rótulos, ponto azul fechando o título.
- Estrutura de grade rígida: margem 72 px, cabeçalho com rótulo e fólio ("01 / 05"), régua, cartão de imagem, título, texto, rodapé com logo e "arrasta →".
- Imagens: **capturas reais** do site e dos projetos (`elementos/senerine/`), nunca mockups inventados.

## Fontes
Todas em `fontes/fontes.css` (OFL). No HTML do modelo: `<link rel="stylesheet" href="../../fontes/fontes.css">`.
