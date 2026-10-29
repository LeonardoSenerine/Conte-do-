"""Carrossel v4 "5 detalhes que passam batido" (a aba saiu): a estrutura da base Pixel (cartão com faixa, título,
texto, cabeçalho e rodapé fixos) no sistema visual do próprio senerine.dev. Tudo numa grade só
(margem de 72 px, mesmas alturas em todos os slides) e as imagens são capturas reais do site.
1080x1350 (4:5)."""

M = 72
HEAD = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>
:root { --bg:#1e1d1e; --ink:#f2efea; --muted:rgba(242,239,234,.66); --line:rgba(242,239,234,.16); --blue:#0a63b2; --warm:#d99278; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; font-family:"Inter Tight",sans-serif; }
.s { position:relative; width:1080px; height:1350px; overflow:hidden; background:var(--bg); color:var(--ink); }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.02em; }
.kick { left:72px; top:66px; display:flex; align-items:center; gap:14px; font-size:26px; font-weight:500; }
.kick i { width:12px; height:12px; border-radius:50%; background:currentColor; }
.folio { right:72px; top:70px; color:var(--muted); }
.rule { left:72px; right:72px; height:1px; background:var(--line); }
.logo { left:72px; top:1268px; font-size:30px; font-weight:700; letter-spacing:-.05em; }
.logo span { color:#5aa3e8; }
.logo i { display:inline-block; width:8px; height:8px; border-radius:50%; background:#5aa3e8; margin:0 1px 0 2px; }
.swipe { right:72px; top:1274px; color:var(--muted); }
.card { left:72px; right:72px; top:156px; height:640px; border-radius:28px; overflow:hidden; background:#f2efea; color:#1e1d1e; }
.card > * { position:absolute; }
.band { left:20px; right:20px; bottom:20px; height:88px; border-radius:16px; background:var(--blue); color:#fff; display:flex; align-items:center; gap:22px; padding:0 30px; font-size:27px; font-weight:500; letter-spacing:-.02em; z-index:10; }
.band .mono { font-size:18px; letter-spacing:.06em; text-transform:uppercase; opacity:.7; flex:none; }
.t { left:72px; right:72px; top:846px; font-size:88px; font-weight:700; line-height:.98; letter-spacing:-.055em; }
.t em { font-style:normal; color:var(--warm); }
.dot { display:inline-block; width:.15em; height:.15em; border-radius:50%; background:#3d8fe0; margin-left:.04em; }
.p { left:72px; width:820px; top:1052px; font-size:31px; line-height:1.4; color:var(--muted); letter-spacing:-.015em; }
.scr { border-radius:30px; overflow:hidden; box-shadow:0 30px 60px -30px rgba(30,29,30,.55); }
.scr img { position:absolute; left:0; display:block; }
.ui { font-family:"Inter Tight",sans-serif; }
</style></head><body>
'''


def shell(n, kick, folio, inner, swipe="arrasta →"):
    return f'''<section class="s" id="s{n}">
  <p class="kick"><i></i>{kick}</p><p class="folio mono">{folio}</p>
  <div class="rule" style="top:120px"></div>
  {inner}
  <div class="rule" style="top:1236px"></div>
  <p class="logo">senerine<i></i><span>dev</span></p><p class="swipe mono">{swipe}</p>
</section>'''


def detail(n, kick, art, bad, title, text, plate="#f2efea"):
    return shell(n, kick, f"{n - 2:02d} / 05", f'''<div class="card" style="background:{plate}">{art}
    <div class="band"><span class="mono">Passa batido</span><span>{bad}</span></div></div>
  <h2 class="t">{title}<span class="dot"></span></h2>
  <p class="p">{text}</p>''')


def screen(src, y0, scale=1.2, top=40, h=560):
    """Captura de celular (390 px de largura, @3x) mostrada como uma tela sem moldura, centrada no cartão."""
    w = round(390 * scale)
    return f'<div class="scr" style="left:{(936 - w) // 2}px;top:{top}px;width:{w}px;height:{h}px"><img src="{src}" style="top:{-y0 * scale}px;width:{w}px"></div>'


out = [HEAD]

# 1 · capa
out.append(shell(1, "Depois do site pronto", "senerine.dev", '''<div class="card" style="background:#0b5cad">
    <img src="../../elementos/senerine/leo-cut.png" style="left:118px;top:-330px;width:700px;height:1244px">
    <div class="band" style="background:#1e1d1e"><span class="mono">Atenção</span><span>Pronto não é o mesmo que completo.</span></div></div>
  <h2 class="t">Seu site ficou pronto.<br><em>E os detalhes?</em></h2>
  <p class="p">Cinco coisas pequenas que passam batido e fazem o cliente ficar ou ir embora.</p>'''))

# 2 · índice
items = [("Botão de ação", "O botão que chama"), ("Capa de link", "A prévia no WhatsApp"), 
         ("Google", "Título e descrição"), ("Página 404", "Quando o link quebra"), ("Contato", "Um toque no celular")]
rows = ''.join(f'''<div style="display:grid;grid-template-columns:96px 1fr auto;align-items:baseline;padding:30px 0;border-top:1px solid var(--line)">
  <span class="mono" style="color:#5aa3e8">{i + 1:02d}</span><span style="font-size:44px;font-weight:600;letter-spacing:-.04em">{a}</span><span style="font-size:26px;color:var(--muted)">{b}</span></div>''' for i, (a, b) in enumerate(items))
out.append(shell(2, "Índice", "5 detalhes", f'''<h2 class="t" style="top:170px">O que passa batido<br>no site <em>pronto</em><span class="dot"></span></h2>
  <div style="left:72px;right:72px;top:470px;border-bottom:1px solid var(--line)">{rows}</div>'''))

# 3 · 01 botão (recorte real do início do senerine.dev no celular, sem costura com o fundo)
art = '<img src="../../elementos/senerine/m-hero.png" style="left:0;top:-1344px;width:936px">'
out.append(detail(3, "Botão de ação", art, "“Saiba mais” e o contato lá no rodapé.", "Um botão que<br>chama cliente",
                  "Logo no começo, um botão claro que abre o WhatsApp com a mensagem pronta."))

# 4 · 02 capa de link (a imagem, o título e a descrição são os reais do site)
art = '''<div style="inset:0;background:#efeae2;background-image:radial-gradient(rgba(0,0,0,.05) 1.5px,transparent 1.7px);background-size:20px 20px"></div>
  <div class="ui" style="right:40px;top:40px;width:600px;padding:8px;border-radius:18px;background:#d9fdd3;box-shadow:0 1px 2px rgba(0,0,0,.15)">
    <div style="display:flex;flex-direction:column;border-radius:12px;overflow:hidden;background:#c9eabf">
      <img src="../../elementos/senerine/og.png" style="width:584px;height:307px;object-fit:cover;display:block">
      <div style="padding:14px 18px 16px"><p style="font-size:22px;font-weight:700;line-height:1.25">Senerine.dev · Sites e aplicações de Leonardo Senerine</p>
      <p style="font-size:18px;color:#4a5a48;margin-top:6px;line-height:1.35;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">Estúdio digital autoral: sites e aplicações para marcas e negócios</p>
      <p style="font-size:17px;color:#4a5a48;margin-top:4px">senerine.dev</p></div></div></div>'''
out.append(detail(4, "Capa de link", art, "o link pelado, sem imagem nem título.", "O link chega<br>bonito",
                  "Quando mandam o site no WhatsApp, aparece imagem, título e descrição."))

# 5 · 03 aba (ícone e título reais, ao lado de uma aba genérica)
art = '''<div style="inset:0;background:#dfe1e5"></div>
  <div class="ui" style="left:40px;top:40px;width:470px;height:84px;border-radius:20px 20px 0 0;background:#f2efea;display:flex;align-items:center;gap:18px;padding:0 26px;font-size:26px;font-weight:500;white-space:nowrap;overflow:hidden">
    <img src="../../elementos/senerine/icon.svg" style="width:40px;height:40px;flex:none"><span style="overflow:hidden;text-overflow:ellipsis">Senerine.dev · Sites e aplicações</span></div>
  <div class="ui" style="left:530px;top:40px;width:366px;height:84px;display:flex;align-items:center;gap:14px;padding:0 20px;font-size:24px;color:#80868b;white-space:nowrap">
    <span style="width:30px;height:30px;border-radius:50%;border:2.5px solid #9aa0a6;flex:none"></span>React App</div>
  <div style="left:0;right:0;top:124px;height:76px;background:#f2efea"></div>
  <div class="ui" style="left:40px;right:40px;top:136px;height:52px;border-radius:26px;background:#e6e2db;display:flex;align-items:center;padding:0 24px;font-size:22px;color:#4a474c">senerine.dev/pt</div>
  <div style="left:0;right:0;top:200px;height:322px;overflow:hidden"><img src="../../elementos/senerine/d-hero.png" style="position:absolute;left:0;top:-130px;width:936px"></div>'''
_aba = (detail(5, "Ícone e título", art, "o “React App” com um globo cinza.", "Sua marca<br>até na aba",
                  "Ícone e título que dizem quem você é, em cada aba aberta do navegador."))

# 6 · 04 Google (título e descrição reais)
g = '<span style="color:#4285f4">G</span><span style="color:#ea4335">o</span><span style="color:#fbbc05">o</span><span style="color:#4285f4">g</span><span style="color:#34a853">l</span><span style="color:#ea4335">e</span>'
art = f'''<div style="inset:0;background:#fff"></div>
  <p class="ui" style="left:44px;top:46px;font-size:44px;font-weight:700;letter-spacing:-.03em">{g}</p>
  <div class="ui" style="left:228px;top:40px;right:44px;height:62px;border-radius:31px;border:1.5px solid #dfe1e5;display:flex;align-items:center;padding:0 26px;font-size:25px;color:#202124">senerine</div>
  <div style="left:0;right:0;top:134px;height:1px;background:#ebebeb"></div>
  <div class="ui" style="left:44px;top:166px;display:flex;align-items:center;gap:16px"><img src="../../elementos/senerine/icon.svg" style="width:48px;height:48px;border-radius:50%"><div><p style="font-size:24px;color:#202124">Senerine.dev</p><p style="font-size:20px;color:#4d5156">https://senerine.dev › pt</p></div></div>
  <p class="ui" style="left:44px;top:242px;width:850px;font-size:36px;color:#1a0dab;letter-spacing:-.01em;line-height:1.25">Senerine.dev · Sites e aplicações de Leonardo Senerine</p>
  <p class="ui" style="left:44px;top:344px;width:850px;font-size:24px;line-height:1.5;color:#4d5156">Estúdio digital autoral: sites e aplicações para marcas e negócios que não querem passar batido. Design, código e publicação na mesma mão.</p>'''
out.append(detail(5, "Google", art, "o título “Home” e nenhuma descrição.", "Apareça certo<br>no Google",
                  "Título e descrição escritos pra quem procura entender o que você faz."))

# 7 · 05 404 (a página real)
out.append(detail(6, "Página 404", screen("../../elementos/senerine/m-404.png", 176), "“404 Not Found” e mais nada.", "Até o erro tem<br>a sua cara",
                  "Link quebrado acontece. Com uma página da marca, o cliente volta em vez de ir embora."))

# 8 · 06 contato (o bloco real)
out.append(detail(7, "Contato", screen("../../elementos/senerine/m-contato2.png", 116), "telefone em texto, pra copiar e colar.", "Contato<br>num toque",
                  "No celular, o contato vira botão: um toque e já abre o WhatsApp ou o e-mail."))

# 9 · checklist
rows = ''.join(f'''<div style="display:grid;grid-template-columns:96px 1fr;align-items:baseline;padding:38px 0;border-top:1px solid rgba(255,255,255,.22)">
  <span class="mono" style="color:rgba(255,255,255,.7)">{i + 1:02d}</span><span style="font-size:38px;font-weight:600;letter-spacing:-.035em">{t}</span></div>''' for i, t in enumerate(
    ["Botão que chama cliente", "Capa do link no WhatsApp", "Título e descrição no Google", "Página de erro com a sua cara", "Contato num toque"]))
out.append(shell(8, "Checklist", "Salva esse", f'''<div style="left:72px;right:72px;top:156px;height:1040px;border-radius:28px;background:#0a63b2;padding:64px 56px">
    <h2 style="font-size:88px;font-weight:700;line-height:.98;letter-spacing:-.055em">Seu site tem<br>os cinco?</h2>
    <div style="margin-top:56px;border-bottom:1px solid rgba(255,255,255,.22)">{rows}</div></div>'''))

# 10 · convite (como o bloco de contato do site)
out.append(shell(9, "Contato", "senerine.dev", '''<img src="../../elementos/senerine/leonardo-ponto.webp" style="left:72px;top:250px;width:168px;height:168px;border-radius:50%">
  <p style="left:268px;top:300px;font-size:30px;font-weight:600;letter-spacing:-.03em">Leonardo Senerine</p><p class="mono" style="left:268px;top:344px;color:var(--muted)">quem faz o senerine.dev</p>
  <h2 class="t" style="top:470px;font-size:104px">Vamos fazer o seu<br>não passar <em>batido</em><span class="dot"></span></h2>
  <p class="p" style="top:730px">Me conta da marca e do que ela precisa.<br>Quem responde sou eu.</p>
  <div style="left:72px;top:900px;display:flex;align-items:center;gap:14px;padding:26px 40px;border-radius:999px;background:#f2efea;color:#0a63b2;font-size:32px;font-weight:600;letter-spacing:-.02em">Chama no direct <span>↗</span></div>''', swipe="@senerine.dev"))

out.append('</body></html>')
open("post5.html", "w").write("\n".join(out))
print(len(out) - 2, "slides")
