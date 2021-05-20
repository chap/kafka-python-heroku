# from dotenv import load_dotenv
# load_dotenv()  # take environment variables from .env.

import os
import kafka_helper
import time


topic = os.environ['KAFKA_PREFIX'] + 'my-topic'
print('listening to topic:', topic)

consumer = kafka_helper.get_kafka_consumer(topic)
for message in consumer:
    print(message)