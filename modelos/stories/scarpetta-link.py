"""Story do site da Scarpetta no padrão dos primeiros posts (fundo escuro, cartão na cor da casa, faixa azul),
com espaço pra figurinha de link. 1080x1920."""

HEAD = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../fontes/fontes.css"><style>
:root { --bg:#1e1d1e; --ink:#f2efea; --muted:rgba(242,239,234,.66); --line:rgba(242,239,234,.16); --blue:#0a63b2; --warm:#d99278; }
* { box-sizing:border-box; margin:0; padding:0; }
body { width:1080px; background:#000; font-family:"Inter Tight",sans-serif; }
.s { position:relative; width:1080px; height:1920px; overflow:hidden; background:var(--bg); color:var(--ink); }
.s > * { position:absolute; }
.mono { font-family:"JetBrains Mono",monospace; font-size:22px; letter-spacing:.02em; }
.kick { left:72px; top:66px; display:flex; align-items:center; gap:14px; font-size:26px; font-weight:500; }
.kick i { width:12px; height:12px; border-radius:50%; background:currentColor; }
.folio { right:72px; top:70px; color:var(--muted); }
.rule { left:72px; right:72px; height:1px; background:var(--line); }
.logo { left:72px; top:1358px; font-size:30px; font-weight:700; letter-spacing:-.05em; }
.logo span { color:#5aa3e8; }
.logo i { display:inline-block; width:8px; height:8px; border-radius:50%; background:#5aa3e8; margin:0 1px 0 2px; }
.swipe { right:72px; top:1364px; color:var(--muted); }
.card { left:72px; right:72px; top:156px; height:720px; border-radius:28px; overflow:hidden; background:#f2efea; color:#1e1d1e; }
.card > * { position:absolute; }
.band { left:20px; right:20px; bottom:20px; height:88px; border-radius:16px; background:var(--blue); color:#fff; display:flex; align-items:center; gap:22px; padding:0 30px; font-size:27px; font-weight:500; letter-spacing:-.02em; z-index:10; }
.band .mono { font-size:18px; letter-spacing:.06em; text-transform:uppercase; opacity:.7; flex:none; }
.t { left:72px; right:72px; top:926px; font-size:88px; font-weight:700; line-height:.98; letter-spacing:-.055em; }
.t em { font-style:normal; color:var(--warm); }
.dot { display:inline-block; width:.15em; height:.15em; border-radius:50%; background:#3d8fe0; margin-left:.04em; }
.p { left:72px; width:820px; top:1140px; font-size:31px; line-height:1.4; color:var(--muted); letter-spacing:-.015em; }
.scr { border-radius:30px; overflow:hidden; box-shadow:0 30px 60px -30px rgba(30,29,30,.55); }
.scr img { position:absolute; left:0; display:block; }
.ui { font-family:"Inter Tight",sans-serif; }
.scr img { width:100%; top:0; }
.cap { font-family:"JetBrains Mono",monospace; font-size:18px; letter-spacing:.06em; text-transform:uppercase; color:#efe5c8; opacity:.75; }
</style></head><body>
'''



C = "../../elementos/clientes/scarpetta/"
S = f"""<section class="s" id="s1">
  <p class="kick" style="top:250px"><i></i>Site novo no ar</p><p class="folio mono" style="top:254px">senerine.dev</p>
  <div class="rule" style="top:310px"></div>
  <div class="card" style="top:350px;height:820px;background:#0f3d2c">
    <div class="scr" style="left:238px;top:40px;width:460px;height:700px"><img src="{C}site.webp"></div>
    <div class="band"><span class="mono">Cliente real</span><span>Scarpetta Cucina.</span></div></div>
  <h2 class="t" style="top:1220px">O site da Scarpetta<br><em>está no ar</em><span class="dot"></span></h2>
  <p class="p" style="top:1430px">Cardápio, reserva e o salão, num link só.</p>
  <div style="left:190px;top:1540px;width:700px;height:130px">
    <i style="position:absolute;left:0;top:0;width:40px;height:40px;border-left:4px solid var(--ink);border-top:4px solid var(--ink)"></i>
    <i style="position:absolute;right:0;top:0;width:40px;height:40px;border-right:4px solid var(--ink);border-top:4px solid var(--ink)"></i>
    <i style="position:absolute;left:0;bottom:0;width:40px;height:40px;border-left:4px solid var(--ink);border-bottom:4px solid var(--ink)"></i>
    <i style="position:absolute;right:0;bottom:0;width:40px;height:40px;border-right:4px solid var(--ink);border-bottom:4px solid var(--ink)"></i>
    <p class="mono" style="position:absolute;inset:0;display:grid;place-items:center;color:var(--muted);text-transform:uppercase;letter-spacing:.08em">link aqui</p></div>
</section></body></html>"""
open("scarpetta-link.html", "w").write(HEAD + S)
