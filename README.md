![image](../images/confluent-logo-300-2.png)
  
# Documentation

You can find the documentation and instructions for this repo at [https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html](https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html?utm_source=github&utm_medium=demo&utm_campaign=ch.examples_type.community_content.cp-all-in-one)


# Commands for confluent

sudo curl http://localhost:8083/connectors-plugins

sudo docker cp ./confluentinc-kafka-connect-github-2.1.2/. connect:/usr/share/java

sudo docker restart connect

sudo curl -X POST -H "Content-Type: application/json" --data @github-connector-config.json http://localhost:8083/connectors

kafkacat -C -b localhost:9092 -t github-commits
