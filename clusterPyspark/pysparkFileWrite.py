#from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import locale
locale.getdefaultlocale()
locale.getpreferredencoding()
import time
spark = SparkSession \
        .builder \
        .appName("myAppName") \
        .config("spark.sql.debug.maxToStringFields", "100") \
        .getOrCreate()


# Limit cores to 1, and tell each executor to use one core = only one executor is used by Spark
#conf = SparkConf().set('spark.executor.cores', 1).set('spark.cores.max',1).set('spark.executor.memory', '1g')
#sc = SparkContext(master='spark://spark-master:7077', appName='myAppName', conf=conf)

df = spark \
  .read \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "github-commits") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

df.write.save('/', format='parquet', mode='append')
