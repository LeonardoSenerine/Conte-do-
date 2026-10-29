"""Versões explicativas (sem figurinha) dos stories 02, 03 e 04 da série zine. 1080x1920."""
import re
base = open("zine-figurinhas.py").read()
CSS = re.search(r"CSS = r'''(.*?)'''", base, re.S).group(1)
CSS += '''
.tx { font-family:"JetBrains Mono",monospace; font-size:30px; line-height:1.5; letter-spacing:-.01em; }
.li { display:grid; grid-template-columns:70px 1fr; padding:18px 0; border-top:3px solid currentColor; }
.li b { font-family:"Anton",sans-serif; font-weight:400; font-size:44px; line-height:1; color:var(--blue); }
'''

S = []

# 02 · todo mundo olha pra bio: o porquê
S.append('''<section class="s" id="s1">
  <p class="ins" style="left:72px;top:250px;width:936px;font-size:112px;z-index:3">Todo mundo olha<br>pro <i>mesmo lugar:</i></p>
  <img src="../../elementos/tinta/eclipse-sol.png" style="left:140px;top:440px;width:800px">
  <div style="left:472px;top:678px;width:144px;height:144px;border-radius:50%;background:var(--blue);z-index:2"></div>
  <p class="anton" style="left:72px;top:1060px;font-size:200px;z-index:3">a sua <span style="color:var(--blue)">bio.</span></p>
  <p class="tx" style="left:72px;top:1260px;width:900px;z-index:3">Antes de seguir, chamar ou comprar, a pessoa passa pelo seu perfil. O link da bio é a porta: se ele leva direto pro que importa, ela entra. Se cai numa lista confusa, ela volta.</p>
  <img src="../../elementos/tinta/eclipse-gente.png" style="left:0;top:1560px;width:1080px">
  <div class="grain"></div>
</section>''')

# 03 · o nome que aparece no link
S.append('''<section class="s" id="s2" style="background:#111011;color:var(--paper)">
  <img src="../../elementos/tinta/mundo-claro.png" style="left:330px;top:330px;width:700px;opacity:.85">
  <p class="mono" style="left:72px;top:250px;color:#7cbcf2">o endereço também comunica</p>
  <p class="bod" style="left:66px;top:310px;font-size:136px;font-weight:600;z-index:3">O nome<br>que aparece<br><span style="color:#4aa3ea">importa.</span></p>
  <div style="left:0;right:0;top:1150px;z-index:3">
    <p style="margin-left:72px;font-family:'JetBrains Mono',monospace;font-size:64px;letter-spacing:-.02em;background:var(--paper);color:var(--ink);display:inline-block;padding:6px 18px">linktr.ee/seunegocio</p>
    <p class="mono" style="margin:14px 0 0 72px;font-size:24px;opacity:.75">↑ o nome da plataforma vem primeiro</p>
    <p class="anton" style="margin:40px 0 0 72px;font-size:106px;background:var(--blue);color:#fff;display:inline-block;padding:14px 22px 6px">seunegocio.com.br</p>
    <p class="mono" style="margin:14px 0 0 72px;font-size:24px;color:#7cbcf2">↑ o seu nome vem primeiro</p>
  </div>
  <p class="tx" style="left:72px;top:1530px;width:900px;z-index:3">Quem salva, compartilha ou digita o seu link lembra do nome que vem na frente. Com domínio próprio, esse nome é o seu, e o endereço continua seu mesmo se você trocar de site.</p>
  <div class="grain lt"></div>
</section>''')

# 04 · olha de perto: os dobermans de óculos
S.append('''<section class="s" id="s3">
  <img src="../../elementos/tinta/dobermans.png" style="left:0;top:950px;width:1080px">
  <p class="mono" style="left:72px;top:250px">revisão de link na bio</p>
  <p class="anton" style="left:66px;top:296px;font-size:196px;line-height:.92">Olha de<br><span style="color:var(--blue)">perto.</span></p>
  <p class="ins" style="left:600px;top:486px;width:420px;font-size:50px">O link da sua bio <i>com os olhos de quem nunca te viu:</i></p>
  <div class="tx" style="left:72px;top:690px;width:936px;font-size:28px;z-index:3">
    <div class="li"><b>01</b><span>Dá pra saber logo de cara o que você vende?</span></div>
    <div class="li"><b>02</b><span>O botão que mais importa é o primeiro?</span></div>
    <div class="li" style="border-bottom:3px solid currentColor"><b>03</b><span>Parece com a sua marca ou com a de todo mundo?</span></div>
  </div>
  <div class="grain"></div>
</section>''')

open("stories2.html", "w").write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head>
<body>{"".join(S)}</body></html>''')
