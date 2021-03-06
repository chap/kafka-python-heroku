# from dotenv import load_dotenv
# load_dotenv()  # take environment variables from .env.

import os
import kafka_helper
import time

producer = kafka_helper.get_kafka_producer()
topic = os.environ['KAFKA_PREFIX'] + 'my-topic'

while True:
  print('sending message topic:', topic)
  producer.send(topic, value='my value')
  time.sleep(10)
