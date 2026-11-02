// Usage: node html_to_pdf.js <input.html> <output.pdf>   (uses the preinstalled Chromium)
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [inp, out] = process.argv.slice(2).map(p => path.resolve(p));
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + inp);
  await page.pdf({
    path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#777;">page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
    margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' },
  });
  await browser.close();
})();
