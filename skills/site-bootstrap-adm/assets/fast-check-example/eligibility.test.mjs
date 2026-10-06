import assert from 'node:assert/strict';
import test from 'node:test';
import fc from 'fast-check';
import { eligible } from './eligibility.mjs';
import { propertyOptions } from './property-options.mjs';

const config = {
  enabled: true,
  allowedHosts: ['demo.example.invalid'],
  publicPaths: ['/', '/pricing', '/privacy'],
};
const base = 'https://demo.example.invalid';

test('exact registered public page is eligible', () => {
  assert.equal(eligible(config, base + '/pricing'), true);
});

test('deployment disabled forbids collection', () => {
  fc.assert(fc.property(fc.webUrl(), (url) => {
    assert.equal(eligible({ ...config, enabled: false }, url), false);
  }), propertyOptions());
});

test('lookalike hostname cannot activate a copied configuration', () => {
  // Fault detected: replacing exact membership with endsWith/substring.
  fc.assert(fc.property(fc.stringMatching(/^[a-z]{1,20}$/), (prefix) => {
    const host = prefix + '.demo.example.invalid';
    assert.equal(eligible(config, 'https://' + host + '/'), false);
  }), propertyOptions());
});

test('unregistered private route cannot collect', () => {
  // Fault detected: allowing every same-host path.
  fc.assert(fc.property(fc.stringMatching(/^[a-z]{1,20}$/), (suffix) => {
    assert.equal(eligible(config, base + '/account/' + suffix), false);
  }), propertyOptions());
});

test('parsed credential query key excludes the entire page', () => {
  // Fault detected: scanning only raw query text, or omitting credential guards.
  fc.assert(fc.property(
    fc.constantFrom('token', 'TOKEN', 't%6fken', 'email', 'st%61te', 'code'),
    fc.string({ maxLength: 120 }),
    (key, value) => {
      assert.equal(eligible(config, base + '/?utm_source=google&' + key + '=' + encodeURIComponent(value)), false);
    },
  ), propertyOptions());
});

test('encoded empty token regression remains excluded', () => {
  assert.equal(eligible(config, base + '/?t%6fken='), false);
});

test('malformed URL fails closed', () => {
  assert.equal(eligible(config, 'not a URL'), false);
});

test('invalid property configuration fails loudly', () => {
  for (const value of ['', '0', '-1', '1.2', 'abc']) {
    assert.throws(() => propertyOptions({ FC_NUM_RUNS: value }), /FC_NUM_RUNS/);
  }
  assert.throws(() => propertyOptions({ FC_SEED: 'bad' }), /FC_SEED/);
  assert.throws(() => propertyOptions({ FC_PATH: '0:1' }), /FC_SEED/);
  assert.deepEqual(propertyOptions({ FC_NUM_RUNS: '1000', FC_SEED: '-42', FC_PATH: '0:1' }),
    { numRuns: 1000, seed: -42, path: '0:1' });
});
