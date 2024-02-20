import pika
import sys
import os


def partnerReceiveChan():
    connection = pika.BlockingConnection(pika.ConnectionParameters
                                         (host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='SQLData')

    def callback(ch, method, properties, body):
        print(f" [x] From Microservice Received: {body.decode('ascii')}")
        # TODO do something here with "body.decode('ascii')"
    channel.basic_consume(queue='SQLData', on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages from Microservice. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        partnerReceiveChan()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
