import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const [,, html, out, dsf] = process.argv;
const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const p = await b.newPage({ viewport: { width: 1080, height: 1440 }, deviceScaleFactor: +dsf });
await p.goto('file://' + html); await p.waitForSelector('body[data-ok]'); await p.waitForTimeout(400);
await p.screenshot({ path: out });
await b.close();
