# Architecture Blueprint (v1)

## Overview
Python ETL ⇢ JSON on S3/R2 ⇢ Next.js 14 (React 19) ⇢ react‑force‑graph‑2d  
Deployed on Vercel with Edge Functions for subgraph BFS.

## Repo Layout
- `apps/web/` ‑ Next.js  
- `apps/etl/` ‑ Python pipeline  
- `packages/ui/` ‑ Tailwind & shadcn components  
- `packages/types/` ‑ shared Zod + TS types  
- `.github/workflows/` ‑ `etl.yml`, `web.yml`  
- `turbo.json` ‑ monorepo orchestration

## ETL Flow
1. Read CSVs → pandas  
2. Build `nodes.json`, `edges.json`  
3. Compute `govt_amt_by_org.json`  
4. Upload to `s3://<bucket>/data/` with versioned paths  
5. Emit `meta.json` containing SHA‑256 checksums & data version

## Next.js Flow
- `app/graph/[ein]/page.tsx` renders graph from JSON  
- SWR + `DATA_VERSION` to revalidate cache  
- `/api/subgraph` Edge Function performs BFS

## Dev, CI & Prod
| Layer    | Tooling                                                       |
|----------|---------------------------------------------------------------|
| Dev Env  | pnpm, turbopack, Docker                                       |
| Lint/Format | ESLint, Prettier, Ruff, Black                             |
| Tests    | Vitest, React Testing Library, pytest                         |
| CI       | GitHub Actions (lint → test → build → deploy)                 |
| Hosting  | Vercel (web), R2/S3 (data JSON)                               |