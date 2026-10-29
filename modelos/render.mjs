// Renderiza um HTML de modelo em PNG.
// Uso: node modelos/render.mjs <arquivo.html> <pasta-saida> <largura> <altura> <quantidade> [panorama]
//  - normal: cada slide é uma <section id="s1">, "s2"...
//  - panorama: a página inteira tem largura*quantidade e é fatiada (para linhas que atravessam slides)
import { createRequire } from "module";
import { mkdirSync } from "fs";
import { resolve } from "path";
const require = createRequire(import.meta.url);
let pw; try { pw = require("playwright"); } catch { pw = await import("/opt/node-tools/node_modules/playwright/index.mjs"); }
const [file, out, w, h, n, modo] = process.argv.slice(2);
mkdirSync(out, { recursive: true });
const b = await pw.chromium.launch({ args: ["--allow-file-access-from-files"] });
const pano = modo === "panorama";
const p = await b.newPage({ viewport: { width: pano ? +w * +n : +w, height: +h } });
await p.goto(`file://${resolve(file)}`, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
if (pano) await p.waitForSelector("body[data-ok]", { timeout: 5000 }).catch(() => {});
await p.waitForTimeout(250);
for (let i = 1; i <= +n; i++) {
  const path = `${out}/${String(i).padStart(2, "0")}.png`;
  if (pano) await p.screenshot({ path, clip: { x: (i - 1) * +w, y: 0, width: +w, height: +h } });
  else await (await p.$(`#s${i}`)).screenshot({ path });
}
await b.close();
console.log(`${n} imagens em ${out}`);
