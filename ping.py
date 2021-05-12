import kafka_helper

while True:
    producer = kafka_helper.get_kafka_producer()
    print('sending message')
    v = (1024).to_bytes
    producer.send('connecticut-84549.my-topic', 'my key', v)

    print('reading message')
    consumer = kafka_helper.get_kafka_consumer('connecticut-84549.my-topic')
    for message in consumer:
        print(message)

time.sleep(1000)
