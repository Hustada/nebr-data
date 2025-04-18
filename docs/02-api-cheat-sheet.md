# API Cheat‑Sheet

### Edge Function – `/api/subgraph`
| Method | Query Params                          | Description                               |
|--------|---------------------------------------|-------------------------------------------|
| GET    | `root=<EIN>` (string, required)       | EIN that must exist in result            |
|        | `depth=<n>` (int, default = 2)        | BFS depth                                 |
|        | `limit=<n>` (int, default = 100)      | Max nodes returned                        |

**Response**
```json
{
  "nodes": [
    {
      "id": "ORG_7582",
      "label": "Lincoln Charity",
      "total_receipts": 19420.23,
      "govt_amt": 19420.23
    }
  ],
  "edges": [
    {
      "source": "ORG_7582",
      "target": "ORG_7669",
      "amount": 12056.5,
      "type": "Contribution"
    }
  ],
  "meta": {
    "generated_at": "2025-04-18T15:04:00Z",
    "depth": 2
  }
}