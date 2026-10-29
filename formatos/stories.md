# Stories

## Padrão quando ele só diz "faz stories sobre X"
- **3 a 4 stories explicativos, sem figurinha de interação** (é a preferência dele: "quero ser mais explicativo, sem interação").
- Linguagem zine, **cada story com um fundo diferente** (azul cheio, papel, preto, papel) e uma combinação de fontes diferente. Ele pediu para "explorar as fontes e quebrar o padrão" e gostou de todos.
- Uma imagem forte por story, ocupando boa parte da tela (sangrando na borda funciona bem).
- Se for divulgar um post: o primeiro story é o "post novo" com espaço para a figurinha do post.

## Especificações
- **1080x1920**. Faixa segura: texto importante entre **y=250 e y=1700** (em cima ficam nome e barra de progresso; embaixo, o campo de resposta).
- Espaço para figurinha (quando pedir): cantoneiras com rótulo ("post aqui", "enquete aqui") entre y=1000 e y=1700.

## Modelos
- `modelos/stories/zine-explicativos.py`: eclipse ("todo mundo olha pra sua bio"), mundo ("o nome que aparece importa"), dobermans ("olha de perto", checklist de 3 perguntas).
- `modelos/stories/zine-figurinhas.py`: post novo, enquete, quiz, caixinha (com cantoneiras).
- `modelos/stories/destaque-processo.py`: série de stories numerada com caminho de progresso.
- Renderizar: `node modelos/render.mjs <html> <saida> 1080 1920 <n>`.

## Funciona
- Fundo diferente em cada story da sequência.
- Palavra gigante cortando a borda, texto vertical, serifa itálica enorme ("novo").
- Imagem que vira o ponto azul (a lua do eclipse) ou recebe o ponto (o globo).
- Checklist em perguntas (o leitor pensa no próprio caso sem precisar responder).
- Sequência com começo, meio e fim: o problema, o porquê, como saber se é o seu caso.
- Teaser com o fundo desfocado ("consegue adivinhar o próximo projeto?").

## Não funciona
- Figurinha de interação quando ele não pediu.
- Imagem agressiva sem relação com o texto (o cão latindo foi trocado pelos dobermans de óculos, que "combinam" com analisar).
- Texto colado na borda de cima ou de baixo (fica embaixo da interface do Instagram).
