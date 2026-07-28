import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Ensure page length and layout is set for a premium feel
st.set_page_config(page_title="Customer Churn Analysis Dashboard", page_icon="📊", layout="wide")

# Custom CSS for a dynamic look
st.markdown("""
<style>
    .reportview-container .main .block-container{
        padding-top: 2rem;
    }
    .kpi-box {
        background: linear-gradient(135deg, #1f2937, #111827);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #374151;
    }
    .kpi-title {
        font-size: 14px;
        color: #9ca3af;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .kpi-value {
        font-size: 32px;
        font-weight: bold;
        color: #60a5fa;
    }
</style>
""", unsafe_allow_html=True)

# Cache data loading for performance
@st.cache_data
def load_data():
    df = pd.read_csv("customer_churn.csv")
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(subset=['TotalCharges'], inplace=True)
    return df

df = load_data()

# ----------------- SIDEBAR -----------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3126/3126647.png", width=100)
st.sidebar.title("Filters")
st.sidebar.write("Explore the data dynamically:")
selected_contract = st.sidebar.multiselect("Select Contract Type", options=df['Contract'].unique(), default=df['Contract'].unique())
selected_payment = st.sidebar.multiselect("Select Payment Method", options=df['PaymentMethod'].unique(), default=df['PaymentMethod'].unique())

# Filter data
filtered_df = df[(df['Contract'].isin(selected_contract)) & (df['PaymentMethod'].isin(selected_payment))]

# ----------------- MAIN TITLES -----------------
st.title("📊 End-to-End Customer Churn Analysis")
st.markdown("An interactive dashboard to explore why customers leave and how to retain them. Filter the data from the left sidebar to see dynamic changes.")

# ----------------- GLOBAL KPIs -----------------
st.markdown("### Top Level Metrics")
col1, col2, col3, col4 = st.columns(4)

total_customers = len(filtered_df)
total_churned = len(filtered_df[filtered_df['Churn'] == 'Yes'])
churn_rate = (total_churned / total_customers * 100) if total_customers > 0 else 0
avg_monthly = filtered_df['MonthlyCharges'].mean()

with col1:
    st.markdown(f'<div class="kpi-box"><div class="kpi-title">Total Customers</div><div class="kpi-value">{total_customers:,}</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="kpi-box"><div class="kpi-title">Churned Customers</div><div class="kpi-value">{total_churned:,}</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="kpi-box"><div class="kpi-title">Overall Churn Rate</div><div class="kpi-value">{churn_rate:.1f}%</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="kpi-box"><div class="kpi-title">Avg Monthly Charge</div><div class="kpi-value">${avg_monthly:.2f}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------- TABS -----------------
tab1, tab2, tab3 = st.tabs(["📈 Exploratory Data Analysis", "📜 Executive Summary & Findings", "💾 View Raw Data"])

with tab1:
    st.markdown("### 🔍 Visualizing the Key Drivers of Churn")
    
    c1, c2 = st.columns(2)
    # Chart 1: Churn Distribution (Pie)
    with c1:
        churn_counts = filtered_df['Churn'].value_counts().reset_index()
        fig_pie = px.pie(churn_counts, values='count', names='Churn', title="Overall Churn Distribution", hole=0.4, color='Churn', color_discrete_map={'Yes':'#ef4444', 'No':'#3b82f6'})
        fig_pie.update_layout(margin=dict(t=40, b=40, l=40, r=40))
        st.plotly_chart(fig_pie, use_container_width=True)

    # Chart 2: Contract Type vs Churn
    with c2:
        df_contract = filtered_df.groupby(['Contract', 'Churn']).size().reset_index(name='Count')
        fig_contract = px.bar(df_contract, x="Contract", y="Count", color="Churn", title="Churn by Contract Type", barmode='group', color_discrete_map={'Yes':'#ef4444', 'No':'#3b82f6'})
        st.plotly_chart(fig_contract, use_container_width=True)

    c3, c4 = st.columns(2)
    # Chart 3: Monthly Charges vs Churn (Boxplot)
    with c3:
        fig_charge = px.box(filtered_df, x="Churn", y="MonthlyCharges", color="Churn", title="Monthly Charges vs. Churn", color_discrete_map={'Yes':'#ef4444', 'No':'#3b82f6'})
        st.plotly_chart(fig_charge, use_container_width=True)

    # Chart 4: Tenure Distribution
    with c4:
        fig_tenure = px.histogram(filtered_df, x="tenure", color="Churn", title="Customer Tenure Distribution (Months)", nbins=30, opacity=0.8, color_discrete_map={'Yes':'#ef4444', 'No':'#3b82f6'})
        st.plotly_chart(fig_tenure, use_container_width=True)
        
    st.markdown("---")
    # Chart 5: Payment Method
    df_payment = filtered_df.groupby(['PaymentMethod', 'Churn']).size().reset_index(name='Count')
    fig_pay = px.bar(df_payment, y="PaymentMethod", x="Count", color="Churn", orientation='h', title="Churn by Payment Method", color_discrete_map={'Yes':'#ef4444', 'No':'#3b82f6'})
    st.plotly_chart(fig_pay, use_container_width=True)


with tab2:
    st.markdown("### 📑 Executive Summary")
    st.info("""
    In today's highly competitive telecommunications market, retaining existing customers is just as critical as acquiring new ones. 
    This report analyzes historical customer data from a fictional telecommunications company to understand why customers are leaving (churning) and what can be done to keep them.
    
    Our analysis explored variables such as customer demographics, account tenure, subscribed services, contract types, and billing methods. The findings reveal a clear pattern: customers who are on month-to-month contracts, those with higher monthly charges, and relatively new customers (with short tenure) face the highest risk of leaving. 
    """)
    
    st.markdown("### 📌 Top 4 Key Findings")
    colA, colB = st.columns(2)
    with colA:
        st.success("**1. The Contract Trap (Month-to-Month Risk)**\n\nCustomers who have not committed to a long-term contract (i.e., those on a month-to-month basis) are vastly more likely to leave the company.")
        st.error("**2. Higher Monthly Charges Drive Customers Away**\n\nThe distribution of monthly charges shows that a significant portion of churning customers are concentrated in the higher billing brackets (specifically above $70/month).")
    with colB:
        st.warning("**3. New Customers Are Highly Vulnerable**\n\nThe majority of customers who left the company did so within their first few months of service. As tenure increases, churn likelihood drops dramatically.")
        st.info("**4. Electronic Check Users Churn More**\n\nCustomers who pay manually via 'Electronic check' represent a disproportionately large share of the churned user base compared to automatic payment users.")
        
    st.markdown("### 💡 Recommendations")
    st.markdown("""
    Based on these findings, we recommend the following strategic actions:
    *   **Incentivize Long-Term Contracts:** Offer targeted discounts or complimentary service upgrades to customers who agree to switch from month-to-month to a 1-year contract.
    *   **Launch a "New Customer Care" Campaign:** Implement a proactive check-in program during a customer's first 3 months to resolve early friction points and build loyalty.
    *   **Promote Auto-Pay Options:** Offer small monthly discounts to encourage a transition away from manual 'Electronic Checks' to automatic payments (Credit Card or Bank Transfer).
    """)

with tab3:
    st.markdown("### 💾 Raw Dataset (Filtered)")
    st.dataframe(filtered_df, use_container_width=True)
    st.caption("Expand the columns to view all available metrics.")
