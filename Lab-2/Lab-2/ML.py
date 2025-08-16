
# Use processed sales dataset from data_warehouse
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

sales = pd.read_csv('data_warehouse/processed_sales_data.csv')

print("Initial dataset shape:", sales.shape)
print("\nMissing values per column:\n", sales.isnull().sum())
print("\nSample records:\n", sales.head())

# Ensure relevant columns exist
if {'sale_price', 'quantity', 'customer_id', 'sale_id'}.issubset(sales.columns):
    sales['sale_price'] = pd.to_numeric(sales['sale_price'], errors='coerce')
    sales['quantity'] = pd.to_numeric(sales['quantity'], errors='coerce')
    sales = sales.dropna(subset=['customer_id', 'sale_price', 'quantity'])
    sales['total_amount'] = sales['sale_price'] * sales['quantity']
    print("\nPreview of relevant features:")
    preview = sales[['customer_id', 'total_amount', 'sale_price', 'quantity']].head()
    print(preview)
else:
    raise ValueError("Required columns are missing in processed_sales_data.csv")

# Feature engineering
agg = sales.groupby('customer_id').agg(
    total_purchase_amount=('total_amount', 'sum'),
    purchase_frequency=('sale_id', 'count'),
    avg_transaction_value=('sale_price', 'mean')
).reset_index()

agg = agg.fillna(0)

# Normalize features
scaler = MinMaxScaler()
features = ['total_purchase_amount', 'purchase_frequency', 'avg_transaction_value']
agg_scaled = scaler.fit_transform(agg[features])

# KMeans clustering for VIP classification
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
agg['cluster'] = kmeans.fit_predict(agg_scaled)

# Determine which cluster is VIP (higher total purchase amount)
vip_cluster = agg.groupby('cluster')['total_purchase_amount'].mean().idxmax()
agg['VIP'] = np.where(agg['cluster'] == vip_cluster, 'VIP', 'Non-VIP')

# Merge VIP status back to original sales data
sales = sales.merge(agg[['customer_id', 'VIP']], on='customer_id', how='left')

# Reverse ETL: Export enriched data
sales.to_csv('data_warehouse/processed_sales_data_with_vip.csv', index=False)
sales.to_excel('data_warehouse/processed_sales_data_with_vip.xlsx', index=False)
print('VIP classification complete. Enriched data exported to data_warehouse/processed_sales_data_with_vip.csv')
print('Exported to:')
print('- raw_data/sale_price_with_vip.csv')
print('- raw_data/sale_price_with_vip.xlsx')