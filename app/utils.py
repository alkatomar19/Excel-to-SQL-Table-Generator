from graphviz import Digraph

def generate_er_diagram(tables_metadata):
    dot = Digraph(comment='Data Warehouse ERD')

    # Add nodes
    for table in tables_metadata:
        dot.node(table["name"], table["name"])

    # Add relationships
    for table in tables_metadata:
        for fk in table.get("foreign_keys", []):
            ref_table = fk.replace("_id", "")
            dot.edge(table["name"], ref_table)

    return dot