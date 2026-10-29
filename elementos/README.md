# Elementos

`originais/` guarda a imagem como chegou; `tinta/` guarda a versão sem fundo (PNG com transparência) pronta para colar no papel do zine.
Para converter um original novo, adicione uma linha em `modelos/tinta.py` (nome, preto, branco) e rode `python3 tinta.py <nome>` dentro de `modelos/`. Se a imagem tiver uma cor que deve virar o azul do ponto (em vez de sumir), acrescente o teste em `COR`.

| Nome | O que é | Já usado em | Combina com |
|---|---|---|---|
| menino | menino correndo com flores | capa do carrossel link na bio (zine) | cliente empolgado, chegada, pressa boa |
| pressa | homem de chapéu e maleta pulando | link na bio (zine), "quem tem pressa" | tempo, pressa, cliente que não espera |
| tvs | pilha de TVs com olhos | link na bio (zine), "todo mundo vê igual" | atenção, vigilância, todo mundo vendo |
| flor | flor aberta em alto contraste | link na bio (zine), "sua cara" | identidade, florescer |
| fim | homem com jornal THE END IS NEAR | link na bio (zine), "calma, não é o fim" | exagero, alarme, ironia |
| mundo | surfistas em volta do globo | link na bio (zine), stories (quiz e explicativo) | alcance, internet, o link roda o mundo |
| petala | metade de uma flor saindo da borda | story "post novo" | anúncio, novidade |
| eclipse | eclipse com pessoas olhando | story "todo mundo olha pra sua bio" | atenção, revelação, lançamento |
| cao | cão latindo com grill, de baixo | story "sem dó" (trocado) | crítica direta, avaliação |
| dobermans | dois dobermans de óculos | story "olha de perto", destaque Processo (Entender) | análise, revisão, olhar técnico |
| terno | homem de terno sem cabeça pulando | caro e barato, "site genérico deixa o negócio sem cara", modelo pronto ("sem cara" e chamada com o ponto como cabeça) | sem identidade, anônimo |
| tulipa | tulipa desenhada a grafite | capa caro e barato | sofisticação, valor |
| faixa | flores brancas em faixa preta | caro e barato, "vitrine que nunca fecha" | vitrine, contraste |
| lirios | dois lírios | caro e barato, "barato pra quem quer cliente" | crescimento, resultado |
| batida | dois carros batendo | caro e barato, "o barato que sai caro" | erro, prejuízo, retrabalho |
| porsche | Porsche de corrida de frente (assinatura RRM) | caro e barato, "caro pra quem só quer ter" | luxo, desempenho |
| mao | mão gigante e homem caindo (em `tinta/` como mao-mao e mao-homem) | caro e barato, "cliente chega e vai embora" | perder cliente, quase |
| cabeca-azul | perfil de cabeça azul com a faixa do olho (mantém o azul original; trocar pelo do ponto ficou ruim) | capa "ninguém lê o seu site" | olhar, atenção, primeira impressão |
| multidao | multidão correndo para a direita | "ninguém lê", "todo mundo passa correndo" | pressa, feed, gente passando batido |
| cabeca-aberta | homem com o topo da cabeça aberto (rosto de ator conhecido) | "ninguém lê", "ele decide antes de pensar" | decisão, mente do cliente, impressão |
| lampada | homem de terno com cabeça de lâmpada numa poltrona | "ninguém lê", "e julga do sofá" | julgamento, ideia, cliente exigente |
| megafone | mulher gritando num megafone | "ninguém lê", "gritar não adianta" | excesso, propaganda, chamar atenção |
| botas | homem visto de baixo, solas das botas | "ninguém lê", "um ângulo que você nem olha" | ponto de vista, celular, perspectiva |
| washington | George Washington da nota de dólar apontando para baixo de um parapeito | "ninguém lê", lista "o que ele precisa ver primeiro" | apontar, lista, dinheiro |
| leitor | homem lendo numa cadeira, folha que vira o azul do ponto | "ninguém lê", "texto importa, sim" | leitura, conteúdo, ser justo |
| reverencia | homem de casaca fazendo reverência | chamada final "ninguém lê" | convite, a seu dispor, bem-vindo |
| toile-flores | estampa de flores em gravura, repetida | capa "modelo pronto", "bonito e igual ao de todo mundo" | estampa, padrão, repetição, modelo |
| pele-cobra | textura de pele de cobra (usar em faixa vertical) | "modelo pronto é estampa" | estampa, superfície, faixa |
| passaros-borrados | pássaros borrados passando | "o olho já viu isso e passa batido" | passar batido, pressa, movimento |
| ornamento | ornamento barroco (cortar a moldura com `clip-path:inset(1.6%)`) | "enfeite no lugar do que importa" | excesso, enfeite sem função |
| leoes | leões e uma figura de preto parada ao lado | "no meio de todo mundo, quem é diferente fica" | destaque, coragem, o diferente |
| borboletas | três borboletas em alto contraste | "modelo pronto não é vilão" | começo, crescer, leveza |
| leo / leonardo-ponto | o Leonardo (tinta e no ponto azul) | chamadas finais, foto de perfil | CTA, apresentação |

### Originais ainda sem versão em tinta (chegaram em 2026-10-29)
Estão em `originais/` com estes nomes; converter quando forem usados.
- **Bichos:** `cobra-fumaca`, `cobra-galho`, `cobra-escura`, `coruja`, `tigre-faixa`, `leopardos` (brigando), `pegaso` (gravura), `andorinhas-faixa`, `gansos-faixa`, `mulher-pombas` (gravura), `libelula` (com tipografia).
- **Flores e plantas:** `videira` (gravura de uva), `peonias-faixa`, `lirios-faixa`, `iris`, `ramo-pontilhado`, `flor-nanquim`, `flores-bitmap`, `flores-silhueta`, `flores-fluidas`, `toile-vermelho` (estampa; o vermelho não entra, só como forma), `tecido-floral`.
- **Texturas e gestos:** `caligrafia` (pinceladas pretas e dourado), `pincelada`, `explosao` (raios de tinta), `reticula-escura`, `reticula-clara`, `nuvens-reticula` (meio-tom, combina com o ponto).

## senerine/
Capturas reais do senerine.dev (celular @3x, 390 px de largura) e a foto do Leonardo, para a linguagem Senerine:
`m-hero.png` (início no celular), `m-contato2.png`, `m-404.png`, `og.png` (capa de link), `d-hero.png` (computador), `icon.svg`, `leo-cut.png` (recorte), `leonardo-ponto.webp` (foto no ponto azul).

## terceiros/ (fora do repositório)
Memes e músicas usados nos reels ficam em `elementos/terceiros/`, que o `.gitignore` não envia (direitos de terceiros). Peça os arquivos de novo ao Leonardo se precisar.
