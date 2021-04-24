import pika,time, psutil, time

def getusage():
    agent = "OFFICE"
    cpu=str(psutil.cpu_percent())
    memory=str(psutil.virtual_memory().percent)
    new_data = "{} - {} - {}".format(agent,memory, cpu)
    data = """
<heartbeat>
    <header>
      <code>2000</code>
      <origin>FrontEnd</origin>
      <timestamp>2021-05-25T12:00:00+01:00</timestamp>
    </header>
    <body>
      <nameService>Website</nameService>
      <CPUload>5.63</CPUload>
      <RAMload>86.13</RAMload>
    </body>
</heartbeat>"""
    return data


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.3.56.6'))
    channel = connection.channel()
    #channel.queue_declare(queue='hello')
    while(1):
        time.sleep(1)
        msg = getusage()
        channel.basic_publish(exchange='',
                            routing_key='monitoring',
                            body=msg, )
        print((" [x] Sent {}").format(msg))
    connection.close()

main()