// Print ../build/guide.html to ../Lecture_by_Lecture_Study_Guide.pdf with the preinstalled Chromium.
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const out = path.resolve(__dirname, '..');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(out, 'build', 'guide.html'));
  await page.pdf({
    path: path.join(out, 'Lecture_by_Lecture_Study_Guide.pdf'),
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#777;">EEE 339 Power Electronics study guide &middot; page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
    margin: { top: '14mm', bottom: '16mm', left: '13mm', right: '13mm' },
  });
  await browser.close();
})();
