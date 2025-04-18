import csv
import json
import os

# Paths
assets_dir = os.path.dirname(os.path.abspath(__file__))
contrib_file = os.path.join(assets_dir, '2025_ContributionLoanExtract.csv')
exp_file = os.path.join(assets_dir, '2025_ExpenditureExtract.csv')
nodes_file = os.path.join(assets_dir, 'nodes.json')
edges_file = os.path.join(assets_dir, 'edges.json')

def normalize_name(*parts):
    return ' '.join([p for p in parts if p]).strip().upper()

def extract_nodes_and_edges():
    nodes = {}
    edges = []
    
    # --- Contributions/Loans (incoming flows) ---
    with open(contrib_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['State'] != 'NE':
                continue
            # Target node (committee, candidate, org)
            target_id = f"ORG_{row['Org ID']}"
            target_label = normalize_name(row['Filer Name'], row['Candidate Name'])
            nodes[target_id] = {
                'id': target_id,
                'label': target_label,
                'type': row['Filer Type'],
                'city': row['City'],
                'state': row['State'],
                'zip': row['Zip']
            }
            # Source node (contributor, PAC, individual, business, etc.)
            src_type = row['Contributor or Transaction Source Type']
            src_last = row['Contributor or Source Name (Individual Last Name)']
            src_first = row['First Name']
            src_id = normalize_name(src_first, src_last)
            if not src_id:
                src_id = 'UNKNOWN_SOURCE'
            src_node_id = f"SRC_{abs(hash(src_id)) % (10 ** 8)}"
            nodes[src_node_id] = {
                'id': src_node_id,
                'label': src_id,
                'type': src_type,
                'city': row['City'],
                'state': row['State'],
                'zip': row['Zip']
            }
            # Edge
            edges.append({
                'source': src_node_id,
                'target': target_id,
                'amount': float(row['Receipt Amount']) if row['Receipt Amount'] else 0.0,
                'type': row['Receipt Transaction/Contribution Type'],
                'date': row['Receipt Date'],
                'description': row['Description']
            })
    # --- Expenditures (outgoing flows) ---
    with open(exp_file, encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['State'] != 'NE':
                continue
            # Source node (committee/org)
            src_id = f"ORG_{row['Org ID']}"
            src_label = normalize_name(row['Filer Name'], row['Candidate Name'])
            nodes[src_id] = {
                'id': src_id,
                'label': src_label,
                'type': row['Filer Type'],
                'city': row['City'],
                'state': row['State'],
                'zip': row['Zip']
            }
            # Target node (payee, vendor, recipient)
            tgt_type = row['Payee or Recipient or In-Kind Contributor Type']
            tgt_last = row['Payee or Recipient or In-Kind Contributor Name']
            tgt_first = row['First Name']
            tgt_id = normalize_name(tgt_first, tgt_last)
            if not tgt_id:
                tgt_id = 'UNKNOWN_PAYEE'
            tgt_node_id = f"TGT_{abs(hash(tgt_id)) % (10 ** 8)}"
            nodes[tgt_node_id] = {
                'id': tgt_node_id,
                'label': tgt_id,
                'type': tgt_type,
                'city': row['City'],
                'state': row['State'],
                'zip': row['Zip']
            }
            # Edge
            edges.append({
                'source': src_id,
                'target': tgt_node_id,
                'amount': float(row['Expenditure Amount']) if row['Expenditure Amount'] else 0.0,
                'type': row['Expenditure Transaction Type'],
                'date': row['Expenditure Date'],
                'description': row['Description']
            })
    # Save
    with open(nodes_file, 'w') as f:
        json.dump(list(nodes.values()), f, indent=2)
    with open(edges_file, 'w') as f:
        json.dump(edges, f, indent=2)
    print(f"Extracted {len(nodes)} nodes and {len(edges)} edges.")

if __name__ == '__main__':
    extract_nodes_and_edges()
