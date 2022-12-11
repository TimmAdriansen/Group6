from kafka import KafkaClient, KafkaConsumer
from hdfs import InsecureClient

# Create a new Kafka client and consumer
client = KafkaClient.insecure_client("broker:9092")
consumer = KafkaConsumer(client)
consumer.subscribe(["github-commits"])

# Create a new HDFS client
hdfs = InsecureClient("http://namenode:9870")

# Poll for new records and write them to HDFS
with hdfs.write("/path/to/file.txt", encoding="utf-8", overwrite=True) as writer:
    for record in consumer:
        writer.write(record.value)
        writer.write("\n")
