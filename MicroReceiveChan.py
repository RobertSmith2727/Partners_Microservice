import pika
import sys
import os
from sql import insert


def microReceiveChan():
    connection = pika.BlockingConnection(pika.ConnectionParameters
                                         (host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='formData')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode('ascii')}")
        data = []
        string = ''
        newBody = body.decode('ascii')

        for element in newBody:
            if element == '[' or element == '"' or element == "'":
                element = ''
            if element == ' ' and newBody[newBody.index
                                          (element) + 1].isalpha():
                string = string + element
            elif element == ',' or element == ']':
                data.append(string)
                string = ''
            else:
                string = string + element
                # call sql
        insert(data)
        # call send to partner

    channel.basic_consume(queue='formData', on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages from Parnters Project. To exit \
          press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        microReceiveChan()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
