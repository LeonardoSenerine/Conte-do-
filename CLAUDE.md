# senerine-conteudo

Arsenal de conteúdo do Instagram **@senerine.dev** (Leonardo Senerine). Aqui ficam referências, elementos visuais,
ideias e os modelos que geram os posts. O objetivo do conteúdo é **vender** (gerar contatos de negócio), não ser um portfólio de dev.

## Como trabalhar aqui

1. Leia `ideias.md` (o arsenal) e `referencias/README.md` antes de propor algo.
2. Novas referências que o Leonardo mandar: salve em `referencias/` com o nome `AAAA-MM-DD-tema.jpg` e anote no `referencias/README.md` **o que** chama atenção (gancho, formato, tipografia, ritmo).
3. Novos elementos (imagens para usar): original em `elementos/originais/`, versão em tinta em `elementos/tinta/` (veja `modelos/zine/tinta.py`) e uma linha no `elementos/README.md`.
4. Para criar um post, parta de um modelo em `modelos/`, gere o HTML com o `.py` e renderize com `node modelos/render.mjs` (instruções no README).
5. O que foi feito vai para `postados/<tema>/` e a ideia muda de status no `ideias.md`.
6. Sempre faça commit e push no fim: a sessão é temporária, o que não está no GitHub some.

## Regras de conteúdo (não negociáveis)

- Senerine.dev é um **estúdio digital autoral de uma pessoa só** que faz **"sites e aplicações"**. Nunca "desenvolvedor de sites".
- Texto **sem travessões**. Não inventar números, preços, depoimentos, prazos ou clientes. Só fatos que estão no site (senerine.dev) ou nos estudos de caso.
- Nunca citar a cidade dele: ele atende qualquer lugar.
- **Convite de casamento é confidencial**: nunca mostrar link, nome ou imagem nítida.
- **SURAMU está em negociação**: não citar.
- Projeto em sigilo (o "próximo projeto"): não revelar nome, logo nem cidade até o Leonardo liberar.
- Clientes reais: Doce&Sabor, Cantina Pôr do Sol, Gordinho Lanches, D'Conde Barbearia. Conceituais: Vincenzo Saggio, Flanar Café, Samoa, Ponto Alto, Meraki.
- Imagens de terceiros (Pinterest etc.): usar com crédito na legenda quando o autor for conhecido; marcas d'água e assinaturas ficam.
- Evitar vermelho. Evitar "cara de IA" (grade de cards com ícone, números genéricos).
- Ideia central: **"não passar batido"** (o site do cliente não passa batido; no trabalho, nenhum detalhe passa batido).

## Sistema visual

- Cores: azul `#0a63b2` (o ponto, assinatura), preto `#1e1d1e` / tinta `#121112`, papel `#e8e6e0`, off-white `#f2efea`, tom de pele `#d99278`.
- **O ponto azul** fecha títulos, vira progresso, abraça a foto do Leonardo. Reaproveite antes de inventar outro recurso.
- Duas linguagens já aprovadas:
  - **Senerine** (site): fundo escuro, Inter Tight bold com letter-spacing -0.055em, JetBrains Mono nos rótulos.
  - **Zine** (a que mais agradou): papel de fotocópia com grão, imagens em tinta preta (`mix-blend-mode:multiply`), um único azul de risografia, manchetes em **Anton**, serifas **Bodoni Moda** itálica e **Instrument Serif**, texto em **JetBrains Mono**, papéis colados com fita e carimbos.
- Fontes em `fontes/fontes.css` (todas OFL).

## Formatos

- Carrossel: **1080x1440 (3:4)** daqui pra frente. A grade do Instagram corta 4:5 nas laterais; se usar 1080x1350, mantenha o texto da capa no centro.
- Stories: 1080x1920. Faixa segura: texto importante entre y=250 e y=1700.
- Capa de destaque: 1080x1920 com o desenho centralizado (o Instagram recorta um círculo no meio).
- Legenda: gancho na primeira linha, explicação curta, CTA (direct ou link da bio), hashtags no fim.
