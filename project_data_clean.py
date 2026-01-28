import pandas as pd

df_cust = pd.read_csv(r"C:\Users\mrmik\OneDrive\Desktop\nda\sales_stores\customer_data.csv") 
df_proudct = pd.read_csv(r"C:\Users\mrmik\OneDrive\Desktop\nda\sales_stores\product_data.csv") 
df_store = pd.read_csv(r"C:\Users\mrmik\OneDrive\Desktop\nda\sales_stores\store_data.csv") 
df_sales = pd.read_csv(r"C:\Users\mrmik\OneDrive\Desktop\nda\sales_stores\sales_data.csv")

cust=df_cust.copy()
product=df_proudct.copy()
store=df_store.copy()
sales=df_sales.copy()

print("************orginal data*******************************")
print("customer_data******************************************")
print(cust.head(10))
print("product_data*******************************************")
print(product.head(10))
print("store_data*********************************************")
print(store.head(20))
print("sales_data*********************************************")
print(sales.head(10))

cust.columns = cust.columns.str.lower().str.replace(" ", "_").str.strip()
product.columns=product.columns.str.lower().str.replace(" ", "_"). str.strip()
store.columns=store.columns.str.lower().str.replace(" ", "_"). str.strip()
sales.columns=sales.columns.str.lower().str.replace(" ","_").str.strip()

print("********fixed_cleaned_column_names********")
print("customer_columns:", cust.columns)
print("product_columns:", product.columns)
print("store_columns:", store.columns)
print("sales_columns:", sales.columns)
sales["date"] = pd.to_datetime(sales["date"], errors="coerce")

print("Parse_ date_formats")
print(sales["transaction_id"].head(10))

sales ["discount"]= sales["discount"].fillna(0)

print("invalid_data_remove")

product = product[product["category"] != "???"]
print("removed_???:" ,product.shape)

cust = cust.dropna(subset=["email"])
print("removed_email:" ,cust.shape)

store=store.dropna(subset=["store_id"])
print("store_id_missing:" ,store.shape)

sales = sales.merge(product[["product_id", "list_price"]], on="product_id", how="left")
print(sales.head(10))

sales["sale_month"] = sales["date"].dt.to_period("m")
print(sales[["sale_month", "date"]].head(10))

monthly_revenue=sales.groupby(["sale_month", "customer_id"])["list_price"].sum().reset_index()
print(monthly_revenue)