# 🧾 Project Requirements Document  
**Project Name:** Nebraska Charity Money Flow Graph  
**Prepared For:** Mark Hustad  
**Prepared By:** AI Business Analyst (ChatGPT)  
**Date:** 2025‑04‑17  

---

## 1. 🎯 Project Overview

This project aims to recreate the functionality of the [DataRepublican Exposé Graph](https://datarepublican.com/expose/) using Nebraska-specific nonprofit data. The goal is to visualize the flow of funds — particularly taxpayer-sourced contributions — between entities such as political committees, nonprofits, and government-connected organizations. The final product will be interactive, web-based, and optimized for both government insiders and public transparency.

---

## 2. 🎯 Objectives

- Visualize financial relationships between Nebraska-based organizations.  
- Highlight flows of taxpayer money (government contributions).  
- Enable searching, filtering, and browsing of graph data interactively.  
- Make data transparent and useful for politicians, watchdog groups, and eventually the general public.  
- Provide exportable graph summaries and downloadable subgraphs.

---

## 3. 👤 Target Users

| User Group          | Needs                                                         |
|---------------------|---------------------------------------------------------------|
| Government Officials| Understand how taxpayer money flows between nonprofits        |
| Journalists         | Research and expose network patterns and connections          |
| Watchdog Groups     | Audit use of public funds and influence                       |
| General Public      | Improve transparency and understanding of financial networks |

---

## 4. 🧱 Technical Stack

| Component                        | Technology                                       |
|----------------------------------|--------------------------------------------------|
| Frontend Framework               | **React + Next.js**                              |
| Graph Visualization              | **react-force-graph** (preferred) or D3.js       |
| Data Parsing (backend/preprocessing) | **Python** with CSV → JSON pipeline          |
| Hosting                          | **Vercel** or any Next.js-compatible provider    |
| Styling                          | **Tailwind CSS** (optional)                     |

---

## 5. 📁 Data Input Requirements

### Source Format: CSV files (manually downloaded)
- **Files:**
  - `2025_ContributionLoanExtract.csv`
  - `2025_ExpenditureExtract.csv`

### Key Fields Needed:

| Field Name                            | Purpose                                 |
|---------------------------------------|-----------------------------------------|
| `Org ID`                              | Unique organization identifier          |
| `Filer Name`, `Candidate Name`        | Node labeling                           |
| `Receipt Amount`                      | Monetary value of contribution          |
| `Contributor or Transaction Source Type` | Determines if it's government-sourced |
| `Contributor or Source Name`          | Helps match to public entities          |
| `Receipt Transaction/Contribution Type` | Metadata for edge labeling             |
| `Date`, `Description`                 | Tooltip/metadata                        |

---

## 6. 🔎 Data Processing Logic

### 6.1 General Node & Edge Extraction
- Each **organization** becomes a node.  
- Each **contribution** or **expenditure** becomes a directed edge (source → target).  
- Use `ORG_###` and `SRC_###` as node keys (already implemented).

### 6.2 Taxpayer Fund Calculation (`govt_amt`)
- Apply keyword matching to contribution sources to identify likely government contributors.  
- Keywords: `"STATE"`, `"DEPARTMENT"`, `"GOVERNMENT"`, `"FEDERAL"`, `"COUNTY"`, etc.  
- Output a `govt_amt_by_org.json` with:
  ```json
  {
    "7582": 19420.23,
    "7669": 12056.50,
    ...
  }