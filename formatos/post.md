# Post no feed (carrossel e post único)

## Padrão quando ele só diz "faz um post sobre X"
- **Carrossel de 7 a 9 slides**, linguagem **zine**, **1080x1440 (3:4)**.
- Slide 1: gancho que cria curiosidade ou toca na dor. Slides do meio: um ponto por slide. Penúltimo: a nuance (ser justo). Último: chamada (direct ou link da bio) com o ponto azul. O rosto do Leonardo em tinta grande ficou "estranho" (modelo pronto); prefira fechar com uma imagem do próprio post e o ponto (ex.: o terno sem cabeça volta com o ponto azul no lugar da cara).
- Entregar junto: a legenda (ver `legenda.md`) se ele pedir.

## Especificações
- Tamanho: **1080x1440**. A grade do perfil mostra 3:4; 4:5 (1080x1350) é cortado nas laterais. Se usar 1080x1350, título da capa dentro dos 1012 px centrais.
- Margem lateral 64 a 72 px. Cabeçalho (rótulo + fólio "01 / 07") e rodapé (senerine.dev + "vira a página →") fixos em todos os slides.
- Texto mínimo legível no celular: 24 px (mono), 27 px (corpo). Manchete de 120 a 180 px.

## Estruturas que já funcionaram
| Estrutura | Como é | Exemplo | Modelo |
|---|---|---|---|
| Zine com imagens | manchete Anton + imagem em tinta sobre ponto azul + papelzinho com o texto | Link na bio (zine), Ninguém lê (zine nº 02), Modelo pronto (zine nº 03, com faixa vertical) | `modelos/posts/zine.py`, `ninguem-le.py`, `modelo-pronto.py` |
| Linha contínua | uma frase curta por slide, uma linha azul atravessa os slides e encosta no texto, que alterna esquerda/direita; termina no ponto | Caro e barato | `modelos/posts/linha-continua.py` (panorama) |
| Fio + mockups | um fio azul que vira a linha do rodapé e anda como progresso | Link na bio (Senerine) | `modelos/posts/fio-mockups.py` (panorama) |
| Capturas reais em grade | cartão com captura do site, faixa "passa batido", título com ponto | 5 detalhes | `modelos/posts/senerine-capturas.py` |

Renderizar: `node modelos/render.mjs <html> <saida> 1080 1440 <n>` (acrescente `panorama` quando a linha atravessa slides).

## Funciona
- **Zine**: foi o "FICOU INCRÍVEL". Imagens fortes em tinta, um só azul, tipografia que mistura Anton, serifa e mono.
- **Elemento que atravessa os slides** (linha, fio): convida a arrastar.
- **Colagem de fotos P&B recortadas com uma cor só** (as do "ninguém lê": megafone, botas, homem lâmpada, leitor da folha azul, cabeça aberta, multidão, cabeça azul): "gostei da seleção". Preferidas a estampas, texturas e nanquim, que ficaram sem graça no "modelo pronto".
- **Imagem dele como fundo do slide inteiro** (flores no "modelo pronto é estampa"): texto na área clara, halo cor de papel na nota e etiqueta de papel no cabeçalho e no rodapé.
- **Nota com linha** no lugar do papelzinho: texto solto no fio, linha fina até o detalhe da imagem.
- **Paradoxo como gancho** ("caro e barato ao mesmo tempo") e contraste de público ("caro pra quem... / barato pra quem...").
- **Imagem como metáfora** de cada slide (menino correndo = cliente chegando; batida = o barato que sai caro).
- **Um slide sendo justo** ("Linktree não é vilão"): dá credibilidade.
- **Capturas reais** do site no lugar de ilustração.
- Grade rígida: tudo alinhado na mesma margem e nas mesmas alturas.

## Não funciona
- Copiar a base de outro designer sem adaptar (as versões "Pixel" e "Nexora" foram "bem ruim" e "ruizinho").
- **Cara de IA**: elementos desalinhados, cartões com ícone, enfeite sem função.
- Slide que não acrescenta (o slide da "aba" foi cortado).
- Cores fortes demais.
- Texto pequeno cortado no limite do cartão; imagem cobrindo rosto ou logo importante.
- Preço ou número inventado para imitar uma referência.
- **Imagem que não conversa com a frase** (megafone em "enfeite no lugar do que importa"): "não tem sentido estar ali". Cada imagem tem que ser metáfora direta do slide.
- Slide final azul "segue pra ver os próximos" no modelo pronto: tirado. Fechar na chamada do direct.
- **Rosto do Leonardo grande em tinta** na chamada final: "estranho". Tirar.
- **Papelzinho com fita em todo slide**: "sem graça". O texto corrido agora é uma **nota**: solto no papel sobre um fio, com uma linha fina até o detalhe da imagem, que ganha um ponto azul (`nota()` em `ninguem-le.py` e `modelo-pronto.py`). Menos enfeite, mais minimalista.
- Imagem pequena esticada no slide (borda serrilhada): converter em 2x (`DOBRO` no `tinta.py`).
- **Recolorir a cor original de uma ilustração** para o azul do ponto: a cabeça azul do "ninguém lê" ficou "bem ruim" no azul da marca. Imagem que já vem com cor própria fica com a cor dela; o azul do ponto só entra onde a cor sumiria (ou no lugar do vermelho).
- Acento da Anton embaixo de outra letra (É, Ã, Ê no começo ou no meio da 2ª linha): mesmo com `line-height:1.08` encosta. Quebrar a linha de modo que o acento fique na 1ª linha ou embaixo de espaço vazio.

## Checklist antes de mandar
- [ ] 3:4, texto da capa inteiro na grade
- [ ] Nada sobreposto sem querer, nenhum acento cortado
- [ ] Sem travessão, sem número inventado, sem cidade
- [ ] Último slide com chamada
- [ ] Imagens de terceiros anotadas para crédito na legenda
