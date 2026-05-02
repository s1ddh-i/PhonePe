
# 📱 PhonePe Transaction Insights

## 📌 Project Overview
PhonePe Transaction Insights is a data analytics project developed to analyze digital payment trends using the PhonePe Pulse dataset. The project focuses on transaction behavior, state-wise performance, category analysis, and business growth opportunities through data-driven insights.

An interactive dashboard was built using Streamlit, while MySQL was used for structured data storage and SQL analytics.

---

## 🎯 Objectives

- Analyze state-wise transaction performance across India
- Compare payment categories and usage trends
- Study yearly digital payment growth
- Build an interactive dashboard for decision-making
- Generate business recommendations using data

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit
- MySQL
- SQL
- Jupyter Notebook

---

## 📂 Project Structure

```text
PhonePe/
│── app.py
│── main.py
│── mysql_insert.py
│── queries.sql
│── PhonePe_Analysis.ipynb
│── phonepe_transactions.csv
│── README.md
````

---

## ⚙️ Workflow

1. Extract JSON data from PhonePe Pulse dataset
2. Clean and transform data using Python
3. Store structured data in MySQL tables
4. Perform SQL queries for analysis
5. Build Streamlit dashboard
6. Generate business insights and reports

---

## 📊 Key Insights

* Telangana recorded the highest transaction amount
* Karnataka and Maharashtra followed closely
* Peer-to-peer payments dominated transaction categories
* Merchant payments showed strong growth
* Digital payments increased significantly year over year

---

## 🗄️ SQL Implementation

Created MySQL database: `phonepe_project`

Tables Created:

* aggregated_transaction
* aggregated_user
* aggregated_insurance
* map_user
* map_map
* map_insurance
* top_user
* top_map
* top_insurance

---

## 🚀 How to Run

### Install Packages

```bash
pip install pandas streamlit matplotlib sqlalchemy pymysql
```

### Run Data Extraction

```bash
python main.py
```

### Insert Data into MySQL

```bash
python mysql_insert.py
```

### Launch Dashboard

```bash
streamlit run app.py
```

---

## 📈 Dashboard Features

* Year Filter
* State Filter
* KPI Metrics
* Top States Chart
* Category Analysis
* Growth Trend Visualization

---

## 💼 Business Use Cases

* Market Expansion Strategy
* User Engagement Analysis
* Transaction Trend Monitoring
* Insurance Growth Opportunities
* Regional Performance Benchmarking

---

## 👩‍💻 Developed By

**Siddhi Kothari**

---

## 🙏 Thank You

