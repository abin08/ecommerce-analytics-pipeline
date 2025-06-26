from pyspark.sql import SparkSession


# initialize Spark
spark = SparkSession.builder.appName("Retailkart").getOrCreate()
# Enable Arrow optimization
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

# Load cleaned transaction data
input_path = "data/retail_cleaned.parquet"
df = spark.read.parquet(input_path)


