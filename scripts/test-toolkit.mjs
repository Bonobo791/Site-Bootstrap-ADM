import assert from 'node:assert/strict';
import { cpSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn, spawnSync } from 'node:child_process';
import { setTimeout as delay } from 'node:timers/promises';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const site = mkdtempSync(join(tmpdir(), 'site-toolkit-'));
const env = { ...process.env, ASTRO_TELEMETRY_DISABLED: '1', SITE_URL: 'https://example.com', SOURCE_COMMIT: 'a'.repeat(40) };
let server;
try {
  cpSync(join(root, 'skills/site-bootstrap-adm/assets/site'), site, { recursive: true });
  const page = join(site, 'src/pages/index.astro');
  writeFileSync(page, readFileSync(page, 'utf8').replace('Replace this page with your website content.', 'Fresh website content.'));
  for (const args of [['ci', '--ignore-scripts', '--no-audit', '--no-fund'], ['run', 'check'], ['run', 'build']]) {
    const result = spawnSync('npm', args, { cwd: site, env, stdio: 'inherit' });
    assert.equal(result.status, 0, `npm ${args.join(' ')} failed`);
  }
  server = spawn(process.execPath, ['dist/server/entry.mjs'], { cwd: site, env: { ...env, HOST: '127.0.0.1', PORT: '4329' }, stdio: 'inherit' });
  const base = 'http://127.0.0.1:4329';
  let ready = false;
  for (let attempt = 0; attempt < 100; attempt++) {
    assert.equal(server.exitCode, null, 'production server exited');
    try {
      const response = await fetch(`${base}/healthz`, { signal: AbortSignal.timeout(1000) });
      if (response.ok && (await response.text()).trim() === 'ok') { ready = true; break; }
    } catch {}
    await delay(100);
  }
  assert.ok(ready, 'production server did not become ready');
  const home = await fetch(base);
  assert.equal(home.status, 200);
  assert.match(home.headers.get('content-type'), /text\/html/);
  const html = await home.text();
  assert.match(html, /Site template/);
  assert.match(html, /Fresh website content\./);
  assert.match(html, /https:\/\/example.com\//);
  assert.equal((await fetch(`${base}/not-a-page`)).status, 404);
  const robots = await fetch(`${base}/robots.txt`);
  assert.equal(robots.status, 200);
  assert.match(await robots.text(), /Disallow: \//);
  const marker = await fetch(`${base}/build.json`);
  assert.equal(marker.status, 200);
  assert.equal((await marker.json()).commit, env.SOURCE_COMMIT);
  const health = await fetch(`${base}/healthz`);
  assert.match(health.headers.get('content-type'), /text\/plain/);
  console.log('Fresh template: install, check, build, standalone server, home, static asset, 404, health and source marker passed.');
} finally {
  if (server && server.exitCode === null) {
    server.kill('SIGTERM');
    await new Promise(resolve => server.once('exit', resolve));
  }
  rmSync(site, { recursive: true, force: true });
}
