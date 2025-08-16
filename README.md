📊 Lab-2: ETL Pipeline, Data Analysis & VIP Customer Classification
🎯 Objective

This lab experiment provides practical experience in building a basic ETL (Extract, Transform, Load) data pipeline using Python. It demonstrates how raw sales and customer feedback data can be processed, analyzed, and used for machine learning tasks such as VIP customer classification.

The project also simulates real-world collaboration between Business Analysts, Data Engineers, Data Analysts, and ML Engineers in the data lifecycle.

✅ Outcomes

By completing this lab, you will:

Identify and describe the stages of the data engineering lifecycle.

Explain the roles and responsibilities of different stakeholders at each stage.

Perform basic ETL and data analysis tasks within a simulated environment.

Apply machine learning (K-Means clustering) to classify VIP customers.

Export enriched datasets (reverse ETL) for business use.

📂 Project Structure
Lab-2/
│── raw_data/                         # Raw, unprocessed data sources
│   ├── sale_price.csv                # Sales transactions dataset
│   ├── customer_feedback.json        # Customer reviews & sentiments
│
│── data_warehouse/                   # Processed datasets (data lake/warehouse)
│   ├── processed_sales_data.csv      # Cleaned & merged dataset
│   ├── processed_sales_data_with_vip.csv  # Enriched dataset with VIP tagging
│   ├── processed_sales_data_with_vip.xlsx
│
│── DA.py                             # Data Analysis tasks (Top products, sentiment)
│── ETL.py                            # ETL pipeline (Extract → Transform → Load)
│── ML.py                             # ML pipeline (VIP classification, Reverse ETL)
│── Lab-2.docx                        # Documentation / Lab report

⚙️ Setup & Requirements

Install dependencies:

pip install pandas matplotlib scikit-learn

🔄 Workflow
Stage 1: Business Analyst Task

Reviewed raw datasets (sale_price.csv, customer_feedback.json).

Defined business question:
"What are the top 5 products by revenue in the last quarter, and how does customer sentiment vary for these products?"

Required data points: product_id, sale_price, quantity, sale_date, customer_id, sentiment_score.

Stage 2: Data Engineer Task (ETL.py)

Extract – Load raw sales & feedback data using Pandas.

Transform –

Clean missing values, fix data types, standardize dates.

Calculate total_revenue = sale_price × quantity.

Merge datasets on product_id & customer_id.

Load – Export final dataset to:

data_warehouse/processed_sales_data.csv

Stage 3: Data Analyst Task (DA.py)

Aggregated data to find Top 5 Products by Revenue.

Calculated Average Sentiment Score for each product.

Generated visualizations:

📊 Bar Chart → Top 5 Products by Revenue.

📈 Line Plot → Average Sentiment Score.

Sample Output:

Business insight:

"Product X generated the highest revenue, but has below-average sentiment → potential quality issues."

Data feedback:

Some missing sentiment scores and inconsistent dates detected.

Stage 4: Machine Learning Task (ML.py)

Goal: Classify customers into VIP vs Non-VIP using purchasing behavior.

Steps:

Feature engineering → total_purchase_amount, purchase_frequency, avg_transaction_value.

Normalize features with MinMaxScaler.

Apply K-Means clustering (k=2).

Assign VIP label to cluster with higher total purchase.

Perform Reverse ETL → Export enriched data with VIP status.

Output Files:

processed_sales_data_with_vip.csv

processed_sales_data_with_vip.xlsx

Example:

customer_id	total_purchase_amount	purchase_frequency	avg_transaction_value	VIP
C001	5200.0	12	433.3	VIP
C002	700.0	3	233.3	Non-VIP
📈 Final Results & Insights

✅ Top 5 Products by Revenue identified with corresponding average sentiment.

✅ Visualizations created (Revenue bar chart, Sentiment line chart).

✅ VIP Customers classified using clustering approach.

✅ Reverse ETL exported enriched dataset for business use (targeted marketing, personalization).

📝 Conclusion

This lab successfully demonstrated how to build an end-to-end data pipeline with:

ETL for data preparation

Data Analysis for insights

Machine Learning for customer segmentation

Reverse ETL for operational use

This workflow mirrors real-world data engineering and analytics projects, showcasing how raw data can be turned into actionable business insights.
