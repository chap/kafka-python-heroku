import os
import kafka_helper

producer = kafka_helper.get_kafka_producer()
topic = os.environ['KAFKA_PREFIX'] + 'my-topic'
print('sending message topic:%s', topic)
producer.send(topic, value='my value')
