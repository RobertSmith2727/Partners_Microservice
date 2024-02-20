import pika


def sendToPartner(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='SQLData')

    channel.basic_publish(exchange='', routing_key='SQLData',
                          body=str(message))
    print(f" [x] Sent to Partners Project: '{message}'")
    connection.close()


def sendToMicroservice(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='formData')

    channel.basic_publish(exchange='', routing_key='formData',
                          body=str(message))
    print(f" [x] Sent to Microservice: '{message}'")
    connection.close()
