from pyspark import SparkConf, SparkContext
import locale
locale.getdefaultlocale()
locale.getpreferredencoding()
import time



# Limit cores to 1, and tell each executor to use one core = only one executor is used by Spark
conf = SparkConf().set('spark.executor.cores', 1).set('spark.cores.max',1).set('spark.executor.memory', '1g')
sc = SparkContext(master='spark://spark-master:7077', appName='myAppName', conf=conf)

df = spark \
  .read \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "github-commits") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

df.write.save('/', format='parquet', mode='append')
