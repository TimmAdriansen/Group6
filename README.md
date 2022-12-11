![image](../images/confluent-logo-300-2.png)
  
# Documentation

You can find the documentation and instructions for this repo at [https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html](https://docs.confluent.io/platform/current/tutorials/build-your-own-demos.html?utm_source=github&utm_medium=demo&utm_campaign=ch.examples_type.community_content.cp-all-in-one)


# Commands for confluent
docker cp ./confluentinc-kafka-connect-github-2.1.2/. connect:/usr/share/java

sudo docker restart connect

curl https://localhost:8083/connectors-plugins

curl -X POST -H "Content-Type: application/json" --data @github-connector-config.json http://localhost:8083/connectors

