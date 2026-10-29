// Renderiza um reel "diretor" (HTML com uma função global render(t) que desenha o quadro no tempo t
// e devolve a duração total) em JPGs a 30 fps. Para acelerar, rode em 3 processos com faixas de quadros.
// Uso: node render-frames.mjs <arquivo.html> <pasta-quadros> [quadro-inicial] [quadro-final]
// Depois: ffmpeg -framerate 30 -i <pasta>/f%04d.jpg -c:v libx264 -crf 19 -pix_fmt yuv420p -movflags +faststart reel.mp4
import { createRequire } from "module";
import { mkdirSync } from "fs";
import { resolve } from "path";
const require = createRequire(import.meta.url);
let pw; try { pw = require("playwright"); } catch { pw = await import("/opt/node-tools/node_modules/playwright/index.mjs"); }
const [file, out, from = "0", to] = process.argv.slice(2);
mkdirSync(out, { recursive: true });
const b = await pw.chromium.launch({ args: ["--allow-file-access-from-files"] });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto("file://" + resolve(file), { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
const END = await p.evaluate(() => render(0));
const N = Math.ceil(END * 30), f0 = +from, f1 = to ? +to : N;
for (let f = f0; f < f1; f++) {
  await p.evaluate(t => render(t), f / 30);
  await p.screenshot({ path: `${out}/f${String(f).padStart(4, "0")}.jpg`, type: "jpeg", quality: 92 });
}
console.log("quadros", N, "duração", END);
await b.close();
