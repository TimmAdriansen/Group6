from hdfs import InsecureClient
from kafka import KafkaConsumer
import time

client = InsecureClient('http://namenode:9870', user='root')
consumer = KafkaConsumer(
    'alice-in-kafkaland',
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='group1',
     value_deserializer=lambda x: x.decode('utf-8'))

hdfs = InsecureClient("http://namenode:9870")

# Poll for new records and write them to HDFS
with hdfs.write("/path/to/file.txt", encoding="utf-8", overwrite=True) as writer:
    for record in consumer:
        writer.write(record.value)
        writer.write("\n")       
