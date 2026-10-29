import test from 'node:test';
import assert from 'node:assert/strict';
import { withA11yPage } from '../scripts/a11y-page-context.mjs';

function fakeBrowser() {
  const calls = [];
  const page = { id: 'context-page' };
  const browser = {
    async newContext(options) {
      calls.push(['newContext', options]);
      return {
        async newPage() { calls.push(['newPage']); return page; },
        async close() { calls.push(['close']); },
      };
    },
    async newPage() { throw new Error('browser.newPage must not be used'); },
  };
  return { browser, calls, page };
}

test('a11y page is created through a context and context closes after scan', async () => {
  const { browser, calls, page } = fakeBrowser();
  const result = await withA11yPage(browser, { viewport: { width: 390, height: 844 } }, async (actual) => actual);
  assert.equal(result, page);
  assert.deepEqual(calls.map(([name]) => name), ['newContext', 'newPage', 'close']);
});

test('a11y context closes when scan throws', async () => {
  const { browser, calls } = fakeBrowser();
  await assert.rejects(withA11yPage(browser, {}, async () => { throw new Error('scan failed'); }), /scan failed/);
  assert.deepEqual(calls.map(([name]) => name), ['newContext', 'newPage', 'close']);
});
