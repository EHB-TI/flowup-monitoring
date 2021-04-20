import pika ,sys ,os ,time
filePath = "/logs/demo.log"
if os.path.exists(filePath):
    os.remove(filePath)
f = open(filePath, "a")
f.write('\n')
f.close()
print('waiting')
time.sleep(25)
print('stopped waiting')
def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='monitoring')
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        f = open(filePath, "a")
        f.write(body.decode("utf-8") + '\n')
        f.close()
    channel.basic_consume(
        queue='monitoring', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
    connection.close()

if __name__ == '__main__':
    main()

