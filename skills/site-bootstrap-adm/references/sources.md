# Website provenance

Prepared 2026-10-06. Primary website example is Lippincott, inspected at a pinned snapshot from the same date.

| Source | Inspected evidence |
| --- | --- |
| [Lippincott snapshot](https://github.com/Bonobo791/the-lippincott-team/tree/92bfa5ad5d876730c09198d7b3d9c63923715b24) | Astro/Tina content site and conditional request-time routes |
| [Package](https://github.com/Bonobo791/the-lippincott-team/blob/92bfa5ad5d876730c09198d7b3d9c63923715b24/package.json), [AGENTS](https://github.com/Bonobo791/the-lippincott-team/blob/92bfa5ad5d876730c09198d7b3d9c63923715b24/AGENTS.md) | Actual scripts/runtime/manager and source-specific policies |
| [Astro config](https://github.com/Bonobo791/the-lippincott-team/blob/92bfa5ad5d876730c09198d7b3d9c63923715b24/astro.config.mjs), [layout](https://github.com/Bonobo791/the-lippincott-team/blob/92bfa5ad5d876730c09198d7b3d9c63923715b24/src/layouts/Base.astro) | Static/server boundary, shared UI and canonical origin |
| [Tina check](https://github.com/Bonobo791/the-lippincott-team/blob/92bfa5ad5d876730c09198d7b3d9c63923715b24/scripts/check-tina-schema.mjs), [contact](https://github.com/Bonobo791/the-lippincott-team/blob/92bfa5ad5d876730c09198d7b3d9c63923715b24/src/pages/api/contact.ts) | Generated schema consistency and actual validation/delivery boundaries |
| [Official fast-check 4.9.0](https://github.com/dubzzz/fast-check/releases/tag/v4.9.0) | Bundled example version, published 2026-07-08 |
| [Maintainer 4.10.0 note](https://fast-check.dev/blog/2026/09/13/whats-new-in-fast-check-4-10-0/) | Newer release published 2026-09-13; 4.9.0 is not claimed latest |

References/templates are original derived setup guidance. They include enhancements beyond source implementation, including independent properties, formal task records and default-off optional analytics. Verify current official compatibility/provider contracts before reuse. Referenced project code/data/licenses are not republished here.
