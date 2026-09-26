import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Retail Sales Forecasting",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

data = pd.read_csv("inventory_dashboard_data.csv")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Intelligent Retail Sales Forecasting")
st.subheader("Inventory Optimization System")

st.write(
    "Machine Learning based system for sales demand analysis "
    "and inventory reorder recommendations."
)

st.divider()

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

total_products = len(data)

reorder_products = (
    data["Inventory_Status"] == "REORDER"
).sum()

low_stock_products = (
    data["Inventory_Status"] == "LOW STOCK"
).sum()

sufficient_products = (
    data["Inventory_Status"] == "SUFFICIENT"
).sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📦 Total Products",
    total_products
)

col2.metric(
    "🚨 Reorder Required",
    reorder_products
)

col3.metric(
    "⚠️ Low Stock",
    low_stock_products
)

col4.metric(
    "✅ Sufficient Stock",
    sufficient_products
)

st.divider()

# --------------------------------------------------
# PRODUCT ANALYSIS
# --------------------------------------------------

st.header("🔎 Product Analysis")

product = st.selectbox(
    "Select a product",
    sorted(data["Product_Name"].unique())
)

selected = data[
    data["Product_Name"] == product
].iloc[0]

# --------------------------------------------------
# PRODUCT METRICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Daily Demand",
    f"{selected['Average_Daily_Demand']:.2f}"
)

col2.metric(
    "Current Stock",
    int(selected["Current_Stock"])
)

col3.metric(
    "Safety Stock",
    int(selected["Safety_Stock"])
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Reorder Point",
    int(selected["Reorder_Point"])
)

col2.metric(
    "Recommended Order",
    int(selected["Recommended_Order"])
)

col3.metric(
    "Inventory Status",
    selected["Inventory_Status"]
)

st.divider()

# --------------------------------------------------
# REORDER MESSAGE
# --------------------------------------------------

status = selected["Inventory_Status"]

if status == "REORDER":
    st.error(
        f"🚨 {product} requires reordering. "
        f"Recommended quantity: "
        f"{int(selected['Recommended_Order'])} units."
    )

elif status == "LOW STOCK":
    st.warning(
        f"⚠️ {product} has low stock. "
        f"Monitor inventory closely."
    )

else:
    st.success(
        f"✅ {product} has sufficient inventory."
    )

st.divider()

# --------------------------------------------------
# INVENTORY TABLE
# --------------------------------------------------

st.header("📋 Inventory Recommendation")

display_data = data.copy()

display_data.columns = [
    "Product",
    "Avg Daily Demand",
    "Current Stock",
    "Safety Stock",
    "Reorder Point",
    "Recommended Order",
    "Status"
]

st.dataframe(
    display_data,
    use_container_width=True,
    hide_index=True
)

st.divider()

# --------------------------------------------------
# RECOMMENDED ORDER CHART
# --------------------------------------------------

st.header("📈 Recommended Order Quantity")

chart_data = data[
    ["Product_Name", "Recommended_Order"]
].copy()

chart_data = chart_data.set_index(
    "Product_Name"
)

st.bar_chart(chart_data)

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Intelligent Retail Sales Forecasting and "
    "Inventory Optimization System | ML Project"
)