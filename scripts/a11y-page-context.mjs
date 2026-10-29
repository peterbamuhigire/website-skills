// Keep the page and browser context explicit for Playwright APIs that require
// context ownership (including axe-playwright).
export async function withA11yPage(browser, options, scan) {
  const context = await browser.newContext(options);
  try {
    const page = await context.newPage();
    return await scan(page);
  } finally {
    await context.close();
  }
}
