import pika,time, psutil, time, json, math

def getusage():
    agent = "AD"
    cpu=str(psutil.cpu_percent())
    memory=str(psutil.virtual_memory().percent)
    #data_set = {"time" : a_time, "cpu": cpu, "memory" : memory}
    new_data = "{} - {} - {}".format(agent,memory, cpu)
    #message = "{'time':'"+str(time.time())+"', 'aaa_cpu' :'"++"', 'aaa_memory':'"++"'}"
    return new_data
    #return (str(psutil.cpu_percent())+','+str(psutil.virtual_memory().percent)+','+str(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total))


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