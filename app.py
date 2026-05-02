import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------
st.set_page_config(
    page_title="PhonePe Transaction Insights",
    page_icon="📱",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_csv("phonepe_transactions.csv")

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;color:#6C2BD9;'>📱 PhonePe Transaction Insights Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------
st.sidebar.header("🔍 Filters")

year_list = sorted(df["Year"].unique())
state_list = sorted(df["State"].unique())

selected_year = st.sidebar.selectbox("Select Year", year_list)
selected_state = st.sidebar.selectbox("Select State", ["All States"] + state_list)

# Apply filters
filtered_df = df[df["Year"] == selected_year]

if selected_state != "All States":
    filtered_df = filtered_df[filtered_df["State"] == selected_state]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
total_amount = filtered_df["Amount"].sum()
total_count = filtered_df["Count"].sum()
top_state = filtered_df.groupby("State")["Amount"].sum().idxmax()
top_type = filtered_df.groupby("Transaction_Type")["Amount"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Amount", f"₹ {total_amount:,.0f}")
col2.metric("📦 Total Transactions", f"{total_count:,.0f}")
col3.metric("🏆 Top State", top_state)
col4.metric("⭐ Top Category", top_type)

st.markdown("---")

# ---------------------------------------------------
# TOP STATES CHART
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 States by Amount")

    top_states = (
        filtered_df.groupby("State")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_states)

# ---------------------------------------------------
# TRANSACTION CATEGORY CHART
# ---------------------------------------------------
with col2:
    st.subheader("📊 Transaction Categories")

    top_types = (
        filtered_df.groupby("Transaction_Type")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(top_types)

st.markdown("---")

# ---------------------------------------------------
# YEARLY TREND
# ---------------------------------------------------
st.subheader("📈 Yearly Growth Trend")

yearly = df.groupby("Year")["Amount"].sum()
st.line_chart(yearly)

st.markdown("---")

# ---------------------------------------------------
# RAW DATA
# ---------------------------------------------------
with st.expander("📄 View Raw Data"):
    st.dataframe(filtered_df)

# ---------------------------------------------------
# INSIGHTS SECTION
# ---------------------------------------------------
st.subheader("🧠 Key Insights")

st.success(f"""
✅ In {selected_year}, highest performing state: **{top_state}**

✅ Most used transaction category: **{top_type}**

✅ Total transaction amount recorded: **₹ {total_amount:,.0f}**

✅ Digital payments continue showing strong growth trends.
""")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ using Python, Pandas & Streamlit</center>",
    unsafe_allow_html=True
)