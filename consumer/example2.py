from hdfs import InsecureClient
from kafka import KafkaConsumer
import time

consumer = KafkaConsumer(
    'github-commits',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='group1',
     api_version=(0,10,2),
     value_deserializer=lambda x: x.decode('utf-8'))

hdfs = InsecureClient("http://namenode:9870")

# Poll for new records and write them to HDFS
with hdfs.write("/path/to/file.txt", encoding="utf-8", overwrite=True) as writer:
    for record in consumer:
        writer.write(record.value)
        writer.write("\n")       
