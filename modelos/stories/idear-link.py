"""Story do site da Idear Empreendimentos no estilo do case grande (mesmo do scarpetta-link.py), nas cores e na Cormorant da Idear,
com espaço pra figurinha de link. 1080x1920. Gerar: python3 idear-link.py && node ../render.mjs idear-link.html saida 1080 1920 1"""

CSS = r'''
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; height:1920px; overflow:hidden; position:relative; font-family:"Manrope",sans-serif; }
.a { position:absolute; }
.bg { top:0; width:1080px; height:1440px; }
.bg img { width:100%; height:100%; object-fit:cover; display:block; }
.linhas { top:0; width:1080px; height:1440px; background:repeating-linear-gradient(180deg, transparent 0 63px, rgba(15,61,44,.08) 63px 64px); }
.top, .pe { font-size:26px; font-weight:500; letter-spacing:-.01em; z-index:6; }
.h { font-family:"Cormorant Garamond",serif; font-weight:500; line-height:.9; letter-spacing:-.02em; z-index:5; }
.h i { font-style:italic; }
.it { font-family:"Pinyon Script",cursive; line-height:1; z-index:5; }
.p { font-size:34px; line-height:1.35; letter-spacing:-.015em; z-index:5; }
.cel { border-radius:64px; padding:14px; background:#0b0b0b; z-index:4; box-shadow:0 60px 90px -30px rgba(0,0,0,.55); }
.cel img { display:block; width:100%; border-radius:50px; }
.item { display:flex; align-items:baseline; gap:26px; padding:20px 0; border-top:2px solid rgba(15,61,44,.16); font-size:44px; font-weight:500; letter-spacing:-.03em; }
.item b { font-family:"Fraunces",serif; font-style:italic; font-weight:400; color:#c4362b; font-size:34px; width:44px; }
.ft { overflow:hidden; border-radius:10px; z-index:3; }
.ft img { width:100%; height:100%; object-fit:cover; display:block; }
.ft p { position:absolute; left:20px; right:20px; bottom:18px; color:#fff; font-family:"Fraunces",serif; font-size:32px; line-height:1.05; text-shadow:0 2px 14px rgba(0,0,0,.6); }
.ft::after { content:""; position:absolute; inset:50% 0 0 0; background:linear-gradient(transparent, rgba(0,0,0,.55)); }
.ft p { z-index:2; }
.bolha { background:#fff; color:#111; border-radius:30px 30px 30px 8px; padding:34px 40px; font-size:36px; line-height:1.4; z-index:5; box-shadow:0 40px 60px -30px rgba(0,0,0,.5); }
'''


C = "../../elementos/clientes/idear/"
NAVY, DEEP, BRONZE_C, MARFIM = "#07324F", "#052640", "#C4B992", "#FAF8F4"
S = f"""<section id="s1" style="position:relative;width:1080px;height:1920px;overflow:hidden">
  <div class="a" style="inset:0;width:1080px;height:1920px"><img src="{C}casa/fachada-frontal.jpg" style="width:100%;height:100%;object-fit:cover;object-position:42% center"></div>
  <div class="a" style="inset:0;width:1080px;height:1920px;background:linear-gradient(180deg, rgba(5,38,64,.72) 0%, rgba(5,38,64,.2) 26%, rgba(5,38,64,.5) 50%, rgba(5,38,64,.92) 64%, {DEEP} 100%)"></div>
  <div class="a" style="left:56px;top:0;width:2px;height:1920px;background:{BRONZE_C};opacity:.55;z-index:2"></div>
  <p class="a top" style="left:104px;top:250px;color:{MARFIM};opacity:.85">@senerine.dev</p>
  <p class="a top" style="left:604px;width:400px;text-align:right;top:250px;color:{MARFIM};opacity:.85">site novo no ar</p>
  <div class="a cel" style="left:620px;top:330px;width:400px;rotate:5deg"><img src="{C}m-casa.jpg"></div>
  <p class="a" style="left:104px;top:1150px;font-size:24px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:{BRONZE_C};z-index:5">Idear Empreendimentos</p>
  <h2 class="a h" style="left:104px;top:1200px;font-size:150px;color:{MARFIM}">A Idear tem<br><i style="color:{BRONZE_C}">site novo.</i></h2>
  <p class="a p" style="left:104px;top:1500px;width:860px;color:{MARFIM}">A casa à venda, a planta e a visita, num link só.</p>
  <div class="a" style="left:190px;top:1580px;width:700px;height:116px;z-index:6">
    <i style="position:absolute;left:0;top:0;width:44px;height:44px;border-left:5px solid {MARFIM};border-top:5px solid {MARFIM}"></i>
    <i style="position:absolute;right:0;top:0;width:44px;height:44px;border-right:5px solid {MARFIM};border-top:5px solid {MARFIM}"></i>
    <i style="position:absolute;left:0;bottom:0;width:44px;height:44px;border-left:5px solid {MARFIM};border-bottom:5px solid {MARFIM}"></i>
    <i style="position:absolute;right:0;bottom:0;width:44px;height:44px;border-right:5px solid {MARFIM};border-bottom:5px solid {MARFIM}"></i>
    <p style="position:absolute;inset:0;display:grid;place-items:center;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:{MARFIM};opacity:.6">link aqui</p></div>
</section>"""
open("idear-link.html", "w").write(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head><body>{S}</body></html>""")
