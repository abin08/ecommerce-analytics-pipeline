from pyspark.sql import SparkSession
from pyspark.sql.functions import count, max as spark_max
import pandas as pd

# initialize Spark
spark = SparkSession.builder.appName("Retailkart").getOrCreate()
# Enable Arrow optimization
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

# Load cleaned transaction data
input_path = "data/retail_cleaned.parquet"
df = spark.read.parquet(input_path)
# df.show(5)

# Aggregate: Purchase count & last purchase timestamp 
# to find the purchase_count (number of times a customer bought a product) and the last_purchase_date
agg_df = df.groupBy("CustomerID", "StockCode").agg(
    count("*").alias("purchase_count"),
    spark_max("InvoiceDate").alias("last_purchase_date")
)

# agg_df.show(5)

# Convert to Pandas via Arrow
agg_pd = agg_df.toPandas()

# Perform Feature engineering in Pandas
# Ensure the 'last_purchase' column is in datetime format.
agg_pd["last_purchase_date"] = pd.to_datetime(agg_pd["last_purchase_date"])

# Calculate the number of days since the last purchase for each customer-product pair.
# Subtract the last_purchase date from the current timestamp to get a timedelta,
# then extract the number of days as an integer using .dt.days.
"""
# Use the below line for real time calculation which uses 
# current timestamp instead of reference date
agg_pd["recency_days"] = (pd.Timestamp.now() - agg_pd["last_purchase_date"]).dt.days
"""
# since the data is too old, I am taking max of last_purchase_date as reference date
reference_date = agg_pd["last_purchase_date"].max()
agg_pd["recency_days"] = (reference_date - agg_pd["last_purchase_date"]).dt.days
print(agg_pd.head())


