// Synthetic example: eligibility only. It never sends network requests.
const credentialKeys = new Set(['code', 'state', 'token', 'email']);

export function eligible(config, rawUrl) {
  if (config.enabled !== true) return false;
  let url;
  try {
    url = new URL(rawUrl);
  } catch {
    return false;
  }
  if (!config.allowedHosts.includes(url.hostname)) return false;
  if (!config.publicPaths.includes(url.pathname)) return false;
  for (const key of url.searchParams.keys()) {
    if (credentialKeys.has(key.toLowerCase())) return false;
  }
  return true;
}
