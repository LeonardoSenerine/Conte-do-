# Conteúdo · @senerine.dev

Arsenal de conteúdo do Instagram do Leonardo Senerine. O conteúdo existe para **vender** (gerar contatos de negócio).

## Roteador: qual arquivo ler para cada pedido

| O Leonardo pede | Leia antes de fazer qualquer coisa |
|---|---|
| "post", "carrossel", "post no feed" | `formatos/post.md` |
| "stories", "story" | `formatos/stories.md` |
| "reels", "vídeo" | `formatos/reels.md` |
| "destaque", "capa de destaque" | `formatos/destaques.md` |
| "legenda", "texto do post", "comentário" | `formatos/legenda.md` |
| "perfil", "bio", "foto de perfil" | `formatos/perfil.md` |
| "ideia", "pauta", "o que postar" | `ideias/` (o arquivo do formato) e `ideias/ganchos.md` |
| manda imagens de referência | `referencias/<formato>/README.md` (salvar e anotar) |
| manda imagens para usar | `elementos/README.md` (salvar, passar para tinta, catalogar) |

Sempre leia também `marca/regras.md` e `marca/visual.md`. Os pedidos chegam no formato de `COMO-PEDIR.md`; se faltar algo, use o padrão do guia do formato em vez de perguntar.

## Fluxo

1. Ler o guia do formato e as regras da marca.
2. Partir de um modelo em `modelos/<formato>/` (gerar HTML com o `.py`, renderizar com `modelos/render.mjs`).
3. Conferir o resultado olhando as imagens (sobreposição, corte, legibilidade, faixa segura) antes de mandar.
4. Mandar ao Leonardo. Quando ele aprovar, salvar em `postados/<formato>/AAAA-MM-<tema>/` e atualizar o status em `ideias/`.
5. Anotar no guia do formato o que ele elogiou ou reclamou (seção "Funciona" / "Não funciona"). É assim que o arsenal aprende.
6. Commit e push no fim. A sessão é temporária: o que não está no GitHub some.
