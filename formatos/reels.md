# Reels

## Padrão quando ele só diz "faz um reels sobre X"
- **Vertical 1080x1920, 30 fps, de 45 a 60 s**, cenas curtas com transição rápida.
- **Gancho nos 3 primeiros segundos** que gere curiosidade; no meio, ensinar algo; no fim, a pessoa sai recompensada (a resposta, a dica, o checklist) e vem a chamada.
- Texto na tela acompanhando a fala (legenda própria, não depender da automática).
- Áudio: a **voz do Leonardo** quando houver; música só como acento (ver abaixo).

## Como é feito (pipeline)
1. **Diretor em HTML**: uma página com uma função global `render(t)` que desenha o quadro no tempo `t` (segundos) e devolve a duração total. Cenas numa tabela de tempos (`const S = { S1:[0,3.05], ... }`).
   Modelos: `modelos/reels/5-testes.html` e `modelos/reels/php-gremio.html` (o meme e a música não estão no repositório; ficam em `elementos/terceiros/`, que é ignorado).
2. **Quadros**: `node modelos/reels/render-frames.mjs <html> <pasta> [início] [fim]`. Rode em 3 processos com faixas diferentes para acelerar.
3. **Vídeo**: `ffmpeg -framerate 30 -i <pasta>/f%04d.jpg -c:v libx264 -crf 19 -pix_fmt yuv420p -movflags +faststart reel.mp4`
4. **Voz** (áudios do WhatsApp): limpar com
   `highpass=f=85,afftdn=nr=16:nf=-48:tn=1,equalizer=f=220:t=q:w=1:g=-3,equalizer=f=3800:t=q:w=1:g=3,highshelf=f=9000:g=2,deesser,acompressor=threshold=-24dB:ratio=3:attack=5:release=80:makeup=4,alimiter=limit=0.9`
   Cortar as frases pelas pausas (`silencedetect`), posicionar cada frase com `adelay` e juntar com `amix=normalize=0`; no fim `loudnorm=I=-14`.
   Reconhecimento de fala (Whisper e afins) costuma estar bloqueado na rede da sessão; cortar pelas pausas funciona.
5. **Música**: volume de 0.75 a 0.8 (em 1.0 estourou), fade-out de 0.3 s.

## Funciona
- **Conexão inesperada** com algo que o público ama ("e como isso afeta o Grêmio?") sem afirmar nada falso sobre a outra parte ("não sei se é o caso do Grêmio, e não vou testar").
- **Dublagem do próprio Leonardo** com detalhes de voz ("9,2 do quê? 8,1 do quê?").
- **Meme entrando exatamente na fala** que ele comenta (o Walter White no "e como isso afeta o Grêmio"), com zoom em batidas.
- **Música só durante o meme, curta** (cerca de 2 s), não no vídeo inteiro.
- Cenas mais dinâmicas: corte com desfoque e deslocamento ("whip"), zoom de impacto.
- Gancho de curiosidade + ensinar + recompensa no fim.

## Não funciona
- Música estendida ou no fundo do vídeo todo ("não estenda o áudio, fica estranho").
- Vários memes no mesmo vídeo (ficou só um).
- Palavra duplicada na emenda de dois áudios: conferir as emendas e cortar a repetição.
- Meme entrando antes ou depois da fala certa.

## Checklist antes de mandar
- [ ] Gancho nos 3 primeiros segundos
- [ ] Texto da tela dentro da faixa segura (y 250 a 1700) e legível sem som
- [ ] Emendas da voz sem repetição; volume normalizado
- [ ] Crédito do meme/música na legenda quando houver
