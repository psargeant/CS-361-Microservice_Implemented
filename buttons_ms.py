import os
import subprocess

import pika


def message_respond(ch, method, properties, body):
    try:
        message = body.decode()
        print("check 1")

        if message.startswith('open_mp4_Intro_Video:'):
            file_path = message[len('open_mp4_Intro_Video:'):].strip()
            print("check 2")

            if os.path.exists(file_path):
                subprocess.run([file_path], shell=True)
                print("check 3")
            else:
                print(f"File not found: (file_path")

        elif message.startswith('open_pdf:'):
            file_path = message[len('open_pdf:'):].strip()
            print("check 4")

            if os.path.exists(file_path):
                subprocess.run([file_path], shell=True)
                print("check 5")
            else:
                print(f"File not found: (file_path")

        else:
            print(f"Received unknown message: {message}")
            print("check 6")
            ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"Error:{e}")


def main():
    parameters = pika.ConnectionParameters('localhost', heartbeat=600)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='messages')

    channel.basic_consume(queue='messages', on_message_callback=message_respond, auto_ack=True)

    print('Waiting for messages. To exit, press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
