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

count = 0
text = ''
start = time.time()

for msg in consumer:
    msg = msg.value
    if (msg == 'EOF'):
        break
    text = text + msg + '\n'
    count += 1

with client.write('/alice-in-kafkaland.txt', encoding='utf-8', overwrite=True) as writer:
    writer.write(text)

duration = time.time() - start
print('Processed {0} messages in {1} seconds'.format(count, round(duration, 2)))
