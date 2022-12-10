FROM confluentinc/cp-kafka-connect-base:

RUN   confluent-hub install --no-prompt confluentinc/kafka-connect-github:latest