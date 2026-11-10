"""Story do site da Scarpetta no estilo do case grande (inspirado no Teacher Leal), com espaço pra figurinha de link. 1080x1920."""

CSS = r'''
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; height:1920px; overflow:hidden; position:relative; font-family:"Inter Tight",sans-serif; }
.a { position:absolute; }
.bg { top:0; width:1080px; height:1440px; }
.bg img { width:100%; height:100%; object-fit:cover; display:block; }
.linhas { top:0; width:1080px; height:1440px; background:repeating-linear-gradient(180deg, transparent 0 63px, rgba(15,61,44,.08) 63px 64px); }
.top, .pe { font-size:26px; font-weight:500; letter-spacing:-.01em; z-index:6; }
.h { font-family:"Fraunces",serif; font-weight:600; line-height:.9; letter-spacing:-.035em; z-index:5; }
.h i { font-weight:400; }
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


C = "../../elementos/clientes/scarpetta/"
F = C + "fotos/"
VERDE, NOITE, CREME, MANJ, POMO = "#0f3d2c", "#0a2b1f", "#efe5c8", "#a9c99a", "#c4362b"
S = f"""<section id="s1" style="position:relative;width:1080px;height:1920px;overflow:hidden">
  <div class="a" style="inset:0;width:1080px;height:1920px"><img src="{F}forno.webp" style="width:100%;height:100%;object-fit:cover;object-position:center 30%"></div>
  <div class="a" style="inset:0;width:1080px;height:1920px;background:linear-gradient(180deg, rgba(10,43,31,.6) 0%, rgba(10,43,31,.2) 30%, rgba(10,43,31,.85) 62%, {NOITE} 100%)"></div>
  <div class="a" style="left:56px;top:0;width:2px;height:1920px;background:{POMO};opacity:.55;z-index:2"></div>
  <p class="a top" style="left:104px;top:250px;color:{CREME};opacity:.85">@senerine.dev</p>
  <p class="a top" style="left:604px;width:400px;text-align:right;top:250px;color:{CREME};opacity:.85">site novo no ar</p>
  <div class="a cel" style="left:600px;top:320px;width:440px;rotate:5deg"><img src="{C}site.webp"></div>
  <h2 class="a h" style="left:104px;top:1150px;font-size:150px;color:{CREME}">A Scarpetta<br><i>tem site.</i></h2>
  <p class="a it" style="left:104px;top:1440px;font-size:80px;color:{MANJ}">Benvenuti a casa.</p>
  <p class="a p" style="left:104px;top:1535px;width:860px;color:{CREME}">Cardápio, reserva e o salão, num link só.</p>
  <div class="a" style="left:190px;top:1630px;width:700px;height:130px;z-index:6">
    <i style="position:absolute;left:0;top:0;width:44px;height:44px;border-left:5px solid {CREME};border-top:5px solid {CREME}"></i>
    <i style="position:absolute;right:0;top:0;width:44px;height:44px;border-right:5px solid {CREME};border-top:5px solid {CREME}"></i>
    <i style="position:absolute;left:0;bottom:0;width:44px;height:44px;border-left:5px solid {CREME};border-bottom:5px solid {CREME}"></i>
    <i style="position:absolute;right:0;bottom:0;width:44px;height:44px;border-right:5px solid {CREME};border-bottom:5px solid {CREME}"></i>
    <p style="position:absolute;inset:0;display:grid;place-items:center;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:{CREME};opacity:.6">link aqui</p></div>
</section>"""
open("scarpetta-link.html", "w").write(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fontes/fontes.css"><style>{CSS}</style></head><body>{S}</body></html>""")
