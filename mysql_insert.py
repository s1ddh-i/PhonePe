import pandas as pd
from sqlalchemy import create_engine

# ===============================
# MYSQL CONNECTION
# ===============================
username = "root"
password = "Siddhi.2005"
host = "localhost"
database = "phonepe_project"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# ===============================
# LOAD CSV
# ===============================
df = pd.read_csv("phonepe_transactions.csv")

# Rename columns to match SQL table
df.columns = [
    "state",
    "year",
    "quarter",
    "transaction_type",
    "count",
    "amount"
]

# ===============================
# INSERT INTO MYSQL
# ===============================
df.to_sql(
    name="aggregated_transaction",
    con=engine,
    if_exists="append",
    index=False
)

print("✅ Data inserted into MySQL successfully!")