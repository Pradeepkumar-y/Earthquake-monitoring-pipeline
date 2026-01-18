from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType

# Define earthquake schema
schema = StructType([
    StructField("id", StringType(), True),
    StructField("time", LongType(), True),
    StructField("mag", DoubleType(), True),
    StructField("place", StringType(), True),
    StructField("longitude", DoubleType(), True),
    StructField("latitude", DoubleType(), True),
    StructField("depth", DoubleType(), True)
])

# Start Spark
spark = SparkSession.builder.appName("EarthquakeRawToClean").getOrCreate()

# Read RAW JSON files (each file has column "json")
df_raw = spark.read.json("/raw/earthquake/*.json")

# Parse the nested JSON inside the "json" column
df_parsed = df_raw.select(
    from_json(col("json"), schema).alias("data")
)

# Extract fields from the struct
df_clean = df_parsed.select(
    "data.id",
    "data.time",
    "data.mag",
    "data.place",
    "data.longitude",
    "data.latitude",
    "data.depth"
)

# Write clean dataset to HDFS
df_clean.write.mode("overwrite").parquet("/clean/earthquake")

print("🎉 Clean data written successfully to /clean/earthquake")
spark.stop()
