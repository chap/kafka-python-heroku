import kafka_helper

producer = kafka_helper.get_kafka_producer()
print('sending message')
producer.send('%{KAFKA_PREFIX}my-topic', value='my value')
