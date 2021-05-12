import kafka_helper

while True:
    producer = kafka_helper.get_kafka_producer()
    print('sending message')
    k = 'my key'.encode('utf-8')
    producer.send('connecticut-84549.my-topic', key=k, value='my value')

    print('reading message')
    consumer = kafka_helper.get_kafka_consumer('connecticut-84549.my-topic')
    for message in consumer:
        print(message)

time.sleep(1000)
