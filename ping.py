import kafka_helper

while True:
  producer = kafka_helper.get_kafka_producer()
  producer.send('my-topic', key='my key', value={'k': 'v'})

  consumer = kafka_helper.get_kafka_consumer(topic='my-topic')
  for message in consumer:
      print(message)

  time.sleep(10000)
