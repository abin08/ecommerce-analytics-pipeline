from pyspark.sql import SparkSession
from pyspark.sql.functions import count, max as spark_max

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