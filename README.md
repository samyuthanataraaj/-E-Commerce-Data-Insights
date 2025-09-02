

## Problem Statement

E-commerce platforms need to identify the products and users that drive the most revenue to optimize stock management, reward loyal customers, and improve sales strategies.

---

## Objective

* Explore e-commerce sales and user data.
* Derive **business insights** on product performance, revenue trends, and customer engagement.
* Visualize findings in an **interactive dashboard**.

---

## Dataset Details

The dataset contains the following columns:

| Column Name      | Description                                         |
| ---------------- | --------------------------------------------------- |
| **S.No**         | Serial number of the record                         |
| **BrandName**    | Brand associated with the product                   |
| **Product ID**   | Unique product identifier                           |
| **Product Name** | Name of the product                                 |
| **Brand Desc**   | Description of the brand/product                    |
| **Product Size** | Size or packaging detail                            |
| **Currency**     | Transaction currency (e.g., INR, USD)               |
| **MRP**          | Maximum Retail Price                                |
| **SellPrice**    | Actual selling price                                |
| **Discount**     | Discount percentage or value                        |
| **Category**     | Product category (e.g., Electronics, Fashion, etc.) |

---

## Requirements

1. **Data Analysis Tasks**

   * Identify **top-selling products** (based on sales volume & revenue).
   * Discover **top brands** contributing to revenue.
   * Analyze **discount impact** on sales.
   * Study **sales trends over time** (if time dimension is available).
   * Check **customer retention and reviews** (if user data is included).

2. **Visualization**

   * **Bar Charts** → Top products/brands.
   * **Pie Charts** → Revenue share by category.
   * **Line Charts** → Sales trends (daily, weekly, monthly).
   * **Histograms** → Discounts vs sales distribution.

---

##  Expected Outcome

* An **interactive dashboard** that highlights:
  ✅ Best-selling products & brands.
  ✅ Categories driving the most revenue.
  ✅ Effect of discounts on sales.
  ✅ Recommendations for stocking products & rewarding loyal users.

---

## Tech Stack

* **Python** (Pandas, NumPy, Matplotlib, Seaborn, Plotly)
* **Jupyter Notebook / Google Colab**
* (Optional) **Power BI / Tableau** for advanced dashboards

---

## Steps to Run

1. Clone this repo or download the dataset.
2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn plotly
   ```
3. Run the analysis notebook:

   ```bash
   jupyter notebook ecommerce_analysis.ipynb
   ```
4. Explore the interactive charts & insights.

---

## Sample Insights (Expected)

* **Brand X** contributes **35% of total revenue**.
* **Product Y** is the **highest selling item** with 10,000+ orders.
* **Category Z** shows peak sales during weekends.
* Discounts above **30%** significantly boost sales volume.

