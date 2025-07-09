# 🎲 Modern BI Pipeline: From Raw Data to Strategic Insights (Online Betting)

This project showcases a **production-ready Business Intelligence (BI) pipeline** tailored for the **online betting industry**, leveraging a modern stack of tools to turn raw data into actionable dashboards — in an automated and scalable way.

---

## ⚙️ Tech Stack

| Tool      | Role in the Pipeline |
|-----------|----------------------|
| **SQL**   | Fast extraction of large datasets with filters and logic |
| **PySpark** | Scalable data transformation and churn analysis |
| **Python** | ETL orchestration and Power BI refresh automation |
| **DAX**    | Measures and calculated columns for KPIs |
| **Power BI** | Interactive dashboard layer for strategic decision-making |

---

## 📊 Dashboard Overview

Key Metrics Visualized:

- 💰 **Total Bets (€)**  
- 📈 **Estimated Net Profit (€)**  
- 📊 **Top Players by Bet Volume**  
- ⏸️ **Player Inactivity Distribution (Churn Risk)**  
- 🎯 **Risk vs Value Bubble Chart**  
  - Cross-analysis of inactive days and total value  
- 📅 **Last Play Filtering**  
- 👤 **Dynamic Player Filtering (via slicers)**

All metrics are generated **automatically from processed churn datasets**, and the dashboard is **refreshed via Python-triggered Power BI API**.

---

## 🧠 Example Use Cases

- 🔁 **Churn Prediction** based on days inactive  
- 🧮 **Net Profit by Game or Player Segment**  
- 📉 **Session Trends & Drop-Off Analysis**  
- 🌍 **Geo-Segmentation by Risk or Country**  
- 💡 **Player Lifetime Value & Retention Insights**

---

## 🧱 Pipeline Architecture

The process is **modular, repeatable, and scalable**:

### 1. **SQL**
```sql
SELECT player_id, session_id, game, bet_amount, win_amount, timestamp, country
FROM casino_sessions
WHERE timestamp >= CURRENT_DATE - INTERVAL '60 days';


2. PySpark (churn analysis)
df_churn = df.groupBy("player_id").agg(
    countDistinct("session_id").alias("total_sessions"),
    sum("bet_amount").alias("total_bet"),
    sum("win_amount").alias("total_win"),
    ...
)


3. Python Orchestration
Runs SQL

Triggers PySpark job

Copies output CSV

Triggers Power BI refresh via REST API


4. DAX Measures (Power BI)

Total Bets = SUM(casino_data[bet_amount])
Net Profit = [Total Bets] - [Total Wins]
Churn Risk = DATEDIFF(MAX(casino_data[timestamp]), TODAY(), DAY)


🚀 Pipeline Automation
✅ One-click or scheduled execution

🔁 Fully automated: from SQL to dashboard refresh

📤 No manual steps required for data refresh


📷 Visual Preview
🧪 Pipeline Architecture

📊 Power BI Dashboard



📌 Why This Matters
In industries like online gaming, speed and automation are critical. This pipeline enables:

Near real-time analysis

High-volume scalability

Reproducible insights

Easy collaboration between data engineers and business users



