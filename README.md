# Telco Customer Churn Analysis

## 📌 Project Overview
This capstone project analyzes a telecommunications customer dataset to understand the key drivers of customer churn. The objective is to take raw customer data and transform it into actionable business intelligence through data cleaning, exploratory data analysis (EDA), and data visualization.

This analysis is designed for both technical and non-technical stakeholders, bridging the gap between raw Python code and a polished Executive Summary with clear strategic recommendations.

## 📁 Repository Structure
```
End-to-End-Customer-Churn-Analysis/
│
├── Customer_Churn_Analysis.ipynb   # Main Jupyter Notebook containing the full analysis
├── customer_churn.csv              # Raw dataset used for the project
├── Executive_Summary.pdf           # PDF export of the notebook for easy viewing
├── README.md                       # Project documentation
└── images/                         # Exported visualization graphics used in the report
    ├── chart1.png                  # Churn Distribution
    ├── chart2.png                  # Contract Type vs Churn
    ├── chart3.png                  # Monthly Charges vs Churn
    ├── chart4.png                  # Customer Tenure vs Churn
    ├── chart5.png                  # Payment Method vs Churn
    └── chart6.png                  # Correlation Heatmap
```

## 📊 Key Findings
Our analysis discovered four primary indicators for high customer churn:
1. **Contract Type:** Month-to-month contracts have the highest churn risk by a significant margin.
2. **Monthly Charges:** Customers with higher monthly bills (over $70) are more sensitive to pricing and leave at higher rates.
3. **Tenure Length:** New customers are highly vulnerable in their first few months, with churn likelihood dropping drastically as tenure increases.
4. **Payment Methods:** Customers utilizing manual "Electronic check" payments churn significantly more than those using automated payment solutions.

## 💡 Strategic Recommendations
Based on the data, we developed three actionable recommendations:
* **Incentivize Long-Term Contracts:** Transition month-to-month customers to 1- or 2-year contracts.
* **Launch a Dedicated "New Customer Care" Campaign:** Focus heavily on engagement and support during the first 1-3 months.
* **Promote Auto-Pay Options:** Offer small monthly discounts to encourage a switch away from manual Electronic Check payments.

## 🚀 How to Run Locally
To explore the technical aspects and run the code on your own machine:
1. Clone this repository directly to your local environment.
2. Ensure you have Python installed, along with Jupyter Notebook or JupyterLab.
3. Install the required libraries using `pip install pandas matplotlib seaborn`.
4. Open `Customer_Churn_Analysis.ipynb` and execute the Appendix cells to generate the visualizations from scratch.

> **Note on Notebook Structure:** The notebook is designed with a "Bottom-Up" technical flow. The Executive Summary, Methodology, and Findings are at the top (with no raw code visible for business users), while the raw data cleaning and EDA code is located in the Appendix at the bottom for technical reviewers.
