import os
import kafka_helper

producer = kafka_helper.get_kafka_producer()
print('sending message')
topic = os.environ['KAFKA_PREFIX'] + 'my-topic'
producer.send(topic, value='my value')
