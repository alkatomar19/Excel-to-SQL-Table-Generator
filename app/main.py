import pandas as pd
import sys
from schema_inference import generate_create_table

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <excel_file> <table_name>")
        return
    
    file_path = sys.argv[1]
    table_name = sys.argv[2]

    df = pd.read_excel(file_path)

    sql = generate_create_table(df, table_name)

    output_file = f"output/{table_name}.sql"
    
    with open(output_file, "w") as f:
        f.write(sql)

    print(f"SQL file generated: {output_file}")

    diagram = generate_er_diagram(tables_metadata)
    diagram.render("output/erd", format="png", view=True)
if __name__ == "__main__":
    main()