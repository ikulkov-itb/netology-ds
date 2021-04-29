#!/usr/bin/python
"""BigQuery I/O PySpark example."""
from pyspark.sql import SparkSession
from datetime import datetime

spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('bigquery-to-gcs-app') \
  .getOrCreate()

# Use the Cloud Storage bucket for temporary BigQuery export data used
# by the connector.
bucket = "ikulkov_test_bucket"
spark.conf.set('temporaryGcsBucket', bucket)

# Load data from BigQuery.
words = spark.read.format('bigquery') \
  .option('table', 'cld-1-ikulkov-testprj:ikulkov_ds.test_tbl1') \
  .load()
words.show()

# Saving the data to BigQuery
words.write.csv(f'gs://{bucket}/test_tbl_{datetime.now().timestamp()}')
