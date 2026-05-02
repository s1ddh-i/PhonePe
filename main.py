import os
import json
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# PHONEPE DATA EXTRACTION PROJECT
# Full Starter Code for main.py
# =====================================================

# CHANGE THIS PATH TO YOUR CLONED REPO LOCATION
base_path = r"./pulse/data/aggregated/transaction/country/india/state"

all_data = []

# -----------------------------------------------------
# READ ALL JSON FILES
# -----------------------------------------------------
for state in os.listdir(base_path):
    state_path = os.path.join(base_path, state)

    if os.path.isdir(state_path):

        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)

            if os.path.isdir(year_path):

                for file in os.listdir(year_path):

                    if file.endswith(".json"):

                        quarter = file.replace(".json", "")

                        file_path = os.path.join(year_path, file)

                        with open(file_path, "r") as f:
                            data = json.load(f)

                            try:
                                transactions = data["data"]["transactionData"]

                                for item in transactions:
                                    trans_type = item["name"]
                                    count = item["paymentInstruments"][0]["count"]
                                    amount = item["paymentInstruments"][0]["amount"]

                                    all_data.append({
                                        "State": state.replace("-", " ").title(),
                                        "Year": int(year),
                                        "Quarter": int(quarter),
                                        "Transaction_Type": trans_type,
                                        "Count": count,
                                        "Amount": amount
                                    })

                            except:
                                pass

# -----------------------------------------------------
# CREATE DATAFRAME
# -----------------------------------------------------
df = pd.DataFrame(all_data)

print("\nDATA LOADED SUCCESSFULLY\n")
print(df.head())

# -----------------------------------------------------
# SAVE CSV
# -----------------------------------------------------
df.to_csv("phonepe_transactions.csv", index=False)
print("\nCSV FILE SAVED: phonepe_transactions.csv")

# -----------------------------------------------------
# BASIC INSIGHTS
# -----------------------------------------------------

print("\nTOP 10 STATES BY TRANSACTION AMOUNT\n")
top_states = df.groupby("State")["Amount"].sum().sort_values(ascending=False).head(10)
print(top_states)

print("\nTOP TRANSACTION TYPES\n")
top_types = df.groupby("Transaction_Type")["Amount"].sum().sort_values(ascending=False)
print(top_types)

# -----------------------------------------------------
# BAR CHART - TOP STATES
# -----------------------------------------------------
plt.figure(figsize=(12,6))
top_states.plot(kind="bar")
plt.title("Top 10 States by Transaction Amount")
plt.xlabel("State")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_states_chart.png")
plt.show()

# -----------------------------------------------------
# YEARLY TREND
# -----------------------------------------------------
yearly = df.groupby("Year")["Amount"].sum()

plt.figure(figsize=(10,5))
yearly.plot(marker="o")
plt.title("Yearly Transaction Growth")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.grid(True)
plt.tight_layout()
plt.savefig("yearly_growth_chart.png")
plt.show()

# -----------------------------------------------------
# FINAL MESSAGE
# -----------------------------------------------------
print("\nPROJECT ANALYSIS COMPLETE ✅")