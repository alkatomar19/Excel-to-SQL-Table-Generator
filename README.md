# “I built an intelligent schema inference engine that profiles raw Excel data, detects candidate keys, infers optimal SQL Server types, and generates production-ready staging tables with metadata and quality insights.” “I built a data modeling assistant that not only generates SQL schemas from raw data but also infers relationships, identifies measures, and suggests indexing strategies for optimized warehouse performance.”
Real SCD2 often uses:

HASH comparison (better performance)
Separate INSERT after UPDATE
# Excel-to-SQL-Table-Generator
Built a Python-based schema inference tool that:
- Reads Excel datasets
- Infers SQL Server-compatible data types
- Generates optimized CREATE TABLE scripts
- Supports multi-sheet ingestion
- Includes Streamlit UI for interactive use

# 🚀 Excel to Data Warehouse Automation Engine

An intelligent data engineering tool that transforms raw Excel datasets into production-ready data warehouse assets.

excel-to-datawarehouse-engine/
│
├── app/
│   ├── main.py
│   ├── schema_inference.py
│   ├── scd_merge.py
│   ├── erd_generator.py
│
├── ui/
│   └── streamlit_app.py
│
├── output/
│   ├── sample_create.sql
│   ├── sample_merge.sql
│   ├── erd.png
│
├── data/
│   └── sample.xlsx
│
├── requirements.txt
└── README.md

## 🔥 Features

- 📊 Schema Inference Engine
  - Detects data types (INT, DECIMAL, VARCHAR, DATETIME)
  - Optimizes string lengths
  - Handles nullability

- 🧠 Smart Data Modeling
  - Classifies tables into **Dimension** or **Fact**
  - Detects **Primary Keys** and **Foreign Keys**
  - Identifies **Measure Columns**

- 🧬 SCD Type 2 Automation
  - Generates Slowly Changing Dimension logic
  - Adds:
    - effective_date
    - expiry_date
    - is_current

- ⚡ Performance Optimization
  - Auto-generates index recommendations
  - Suggests clustered and non-clustered indexes

- 🔁 MERGE Script Generator
  - Creates SCD Type 2 SQL MERGE statements
  - Handles change detection and history tracking

- 📈 ER Diagram Generator
  - Automatically builds visual data models
  - Detects relationships between tables

- 🌐 Interactive UI
  - Built with Streamlit
  - Upload Excel → Generate SQL + ERD instantly

---

## 🛠️ Tech Stack

- Python (pandas, numpy)
- SQL Server (T-SQL)
- Streamlit (UI)
- Graphviz (ER diagrams)

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt

### 2. Run CLI tool

python app/main.py data/sample.xlsx customers

### 3. Run Web App
streamlit run ui/streamlit_app.py