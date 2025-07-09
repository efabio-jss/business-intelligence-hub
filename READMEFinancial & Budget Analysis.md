# 📈 Financial Budget & Forecast Dashboard – Power BI

This Power BI project is a **finance-focused dashboard** designed to analyze performance vs. budget and forecast across regions, departments, and cost centers. It provides **YTD (Year-To-Date) financial tracking**, variance analysis, and drill-down capabilities using dummy data.

> 🎯 Ideal for financial controllers, FP&A analysts, and BI professionals looking to replicate a structured budgeting insight model.

---

## 🗂️ Project Overview

The report is built around **three pages**, each offering specific angles of financial insights:

---

### 📄 1. Executive Summary (YTD View)

- **Actual vs Forecast vs Budget**: Monthly trend comparison
- **Gauge** showing current YTD actuals vs annual budget
- **Budget vs Forecast %** breakdowns:
  - By **region** (e.g. Europe, Latin America, USA)
  - By **cost category** (e.g. CAPEX, Labor, Admin)
  - By **business area** (Infrastructure, Governance, Enablement…)
- **Running Totals** by month
- Donut visual showing deviation from budget goals

---

### 🌍 2. Regional Breakdown

- **Bar charts** comparing actual vs budget by region
- **Matrix view**:
  - Cross-analysis by **IT area** and **Cost Element Group**
  - Columns by region
  - Color-coded variance indicators (positive/negative)
- **Bubble chart** visualizing deviation per country

---

### 🌐 3. Drill-Down View (Hierarchical)

- **Decomposition Tree**:
  - Root: Budget vs Forecast variance
  - Expand by: Cost Element Group → Country → IT Department
- Allows pinpointing exactly **where** and **why** financial performance is diverging

---

## 🧠 Features & Techniques

- ⚡ Dynamic DAX Measures for:
  - Forecast Variance
  - Actual YTD metrics
  - Goal comparison
- 🎨 Conditional formatting for clear financial signals
- 🧩 Interactive slicers (Region, Cost Category)
- 🔍 Drill-down decomposition for granular insights

---

## 🧪 Dataset

- Data is fully fictional and anonymized.
- Simulates:
  - Budgets (planned)
  - Forecasts (updated)
  - Actuals (realized)
- Dimensions include:
  - Region
  - Country
  - Department
  - Cost Element
  - Month (Jan–Dec 2020)


