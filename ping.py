import kafka_helper

while True:
  producer = kafka_helper.get_kafka_producer()
  producer.send('connecticut-84549.my-topic', 'my key', 'my value')

  consumer = kafka_helper.get_kafka_consumer('connecticut-84549.my-topic')
  for message in consumer:
      print(message)

  time.sleep(10000)
