# 📦 Delivery Performance Dashboard – June 2024

## 📌 Overview
This project showcases a **Power BI interactive dashboard** analyzing delivery performance for different service areas in **June 2024**.  
The dataset is a **mock dataset** generated using Python to simulate realistic delivery scenarios, including delays and customer complaints.

The project demonstrates skills in:
- **Data generation & preparation** (Python, Pandas)
- **Data cleaning & transformation** (Excel / Power Query)
- **Data visualization** (Power BI)
- **KPI tracking & performance analysis**

---

## 🎯 Business Context
The dashboard simulates how a logistics company can monitor **key delivery metrics** to identify underperforming areas, improve operational efficiency, and enhance customer satisfaction.  

The KPIs tracked include:
- **Average Delay (mins)**
- **Total Delayed Deliveries**
- **Total Complaints**
- **On-Time Delivery Rate (%)**

---

## 🛠 Tech Stack
- **Python** – for dataset generation  
- **Pandas** – for basic data structuring  
- **Excel** – for light data cleaning  
- **Power BI** – for interactive data visualization

---

## 📂 Project Structure
```
project/
│
├── Data/
│   └── delivery_data.csv                # Final cleaned dataset
│
├── Output/
│   └── dashboard_screenshot.png         # Power BI dashboard screenshot
│
├── Scripts/
│   └── generate_mock_dataset.py         # Python script to create dataset
│
├── README.md                            # Project documentation
│
└── Prompts/                             # Optional - design notes, questions
```

---

## 📊 Dataset Details
The mock dataset consists of **100 deliveries** for June 2024 with the following distribution:
- **20 delayed deliveries**
- **16 customer complaints**
- **80% on-time delivery rate**
- 5 service areas:  
  - Downtown  
  - Industrial Park  
  - Suburb North  
  - Suburb South  
  - Uptown

### Dataset Columns:
| Column         | Description |
|----------------|-------------|
| `date`         | Delivery date (YYYY-MM-DD) |
| `area`         | Service area name |
| `delay_minutes`| Delay duration in minutes (0 for on-time deliveries) |
| `is_delayed`   | 1 if delayed, 0 if on-time |
| `is_complaint` | 1 if a complaint was logged, else 0 |

---

## 📈 Dashboard Features

![Delivery Performance Dashboard](Output/dashboard_screenshot.png)

### **KPI Cards**
- **Average Delay:** 4.82 mins
- **Total Delayed Deliveries:** 20
- **Total Complaints:** 16
- **On-Time Delivery Rate:** 80%

### **Visuals**
1. **Complaint and Delay by Area** – Combo chart comparing total complaints and average delay.
2. **Delay on Total** – Donut chart showing proportion of delayed vs. on-time deliveries.
3. **Items per Area** – Horizontal bar chart of deliveries per area.
4. **Detailed Table** – Breakdown of average delay and complaints per area.
5. **Area Buttons** – Navigation/filter buttons for each service area.

---

## 🎨 Dashboard Design
- **Layout**
  - Top row: KPI cards in a single horizontal row
  - Middle row: Key visuals (combo chart, donut chart, bar chart)
  - Bottom row: Filter buttons and data table

---

## 🖥 How to Run the Project

### 1️⃣ Generate the Dataset
```bash
cd Scripts
python generate_mock_dataset.py
```
This creates `delivery_data.csv` in the **Data/** folder.

### 2️⃣ Load into Power BI
1. Open Power BI Desktop.
2. Import `Data/delivery_data.csv`.
3. Create calculated measures for:
   ```DAX
   Avg Delay = AVERAGE(delivery_data[delay_minutes])
   Total Delayed = SUM(delivery_data[is_delayed])
   Total Complaints = SUM(delivery_data[is_complaint])
   On-Time Rate = DIVIDE(COUNTROWS(delivery_data) - SUM(delivery_data[is_delayed]), COUNTROWS(delivery_data))
   ```
4. Add visuals & apply theme colors.

---

## 📚 Skills Demonstrated
- **Data Preparation**: Mock data creation, structuring, and cleaning.
- **Data Modeling**: Calculated measures and aggregations in Power BI.
- **Visualization**: KPI cards, combo charts, donut charts, bar charts, and filter buttons.
- **Analytical Thinking**: Designing metrics to identify operational inefficiencies.

---

## 🔮 Possible Extensions
- Add **monthly trend analysis** across multiple months.
- Incorporate **geospatial maps** to visualize delays geographically.
- Connect to **real-time data sources** for live performance monitoring.
- Add **drill-through reports** for complaint investigation.

---
