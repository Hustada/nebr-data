// © 2025 The Victor Collective — MIT License

# Nebraska Charity Money Flow Graph

Visualize the flow of taxpayer-sourced contributions between Nebraska nonprofits, political committees, and government-connected organizations. This project provides an interactive, transparent, and accessible web-based graph for journalists, government insiders, watchdogs, and the public.

## Features

- **Interactive graph** of organizations and financial relationships
- **Search, filter, and browse** graph data
- **Exportable summaries** and downloadable subgraphs
- **Accessible UI** (keyboard navigation, ARIA, color contrast AA)
- **Data versioning** and cache revalidation

## Tech Stack

- **Frontend:** React 19.x, Next.js 15.x, TypeScript, Tailwind CSS, shadcn/ui
- **Graph:** react-force-graph-2d (webgl for >5K nodes)
- **Data:** Python ETL (CSV → JSON), hosted on S3/R2
- **API:** Next.js Edge Function (`/api/subgraph`) for BFS traversal
- **Testing:** Vitest, React Testing Library, pytest
- **CI/CD:** GitHub Actions, Vercel

## Folder Structure

- `docs/` — Project docs, requirements, architecture, API cheat sheet
- `public/data/` — Graph JSON payloads
- `apps/web/` — Next.js frontend (if monorepo)
- `apps/etl/` — Python ETL pipeline (if monorepo)
- `packages/ui/` — Shared UI components
- `packages/types/` — Shared TypeScript/Zod types

## Data Pipeline

- **Input:** Manually downloaded CSVs (`2025_ContributionLoanExtract.csv`, `2025_ExpenditureExtract.csv`)
- **ETL:** Python script outputs `nodes.json`, `edges.json`, `govt_amt_by_org.json`, `meta.json`
- **API:** `/api/subgraph` returns BFS subgraphs for visualization

## Development

```sh
pnpm install
pnpm dev
# or for Python ETL
cd apps/etl && poetry install && poetry run python extract_graph_data.py
```

## Contributing

See [.windsurfrules.md](./.windsurfrules.md) for coding standards and conventions.

## License

MIT — see LICENSE file.
