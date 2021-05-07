import pika,time, psutil, time, json, math
from datetime import datetime

def getusage():
    agent = "example"
    cpu=str(psutil.cpu_percent())
    memory=str(psutil.virtual_memory().percent)
    data = """
    <heartbeat>
    <header>
      <code>2000</code>
      <origin>{}</origin>
      <timestamp>{}</timestamp>
    </header>
    <body>
      <nameService>{}</nameService>
      <CPUload>{}</CPUload>
      <RAMload>{}</RAMload>
    </body>
    </heartbeat>""".format(agent,datetime.now(), "",cpu, memory)
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
        print(" [x] Sent heartbeat")
    connection.close()

while(1):
  try:
    main()
  except:
    print("RMQ offline")
    print("retrying in 5 seconds...")
    time.sleep(5)
