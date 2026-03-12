const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.setViewport({ width: 1100, height: 800 });

  const htmlPath = path.resolve(__dirname, 'docs/cv/resume/caroline-maguire-cv.html');
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });

  await page.emulateMediaType('screen');

  await page.addStyleTag({
    content: `
      body {
        background: linear-gradient(to right, #B59D69 35%, #fff 35%);
        margin: 0;
        padding: 0;
      }
      .cv-container { margin: 0; box-shadow: none; max-width: 100%; width: 100%; }
      .sidebar { background: transparent; }
      .sidebar-page-break { display: none; }
      .portfolio-item { break-inside: avoid; page-break-inside: avoid; }
    `
  });

  const outputPath = path.resolve(__dirname, 'docs/cv/resume/caroline-maguire-cv.pdf');
  await page.pdf({
    path: outputPath,
    format: 'A4',
    printBackground: true,
    scale: 0.85,
    margin: { top: '0px', right: '0px', bottom: '0px', left: '0px' }
  });

  console.log(`PDF generated: ${outputPath}`);
  await browser.close();
})();
