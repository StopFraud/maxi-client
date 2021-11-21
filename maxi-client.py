import urllib.request, json, os,time,pika
import requests
cred_file="cred.txt"
def _cred(s,u,p):
    fh=open(cred_file,"a",encoding="utf-8")
#    fh=open(logfile,"a")
#    text=str(datetime.datetime.now())+" "+str(message)+"\r\n"
    text=s+","+u+","+p+"\r\n"
#    _log(text)
    fh.write(text)
    fh.close()
    return True

def service_check(pip):
    #2do: add json hostname to dns
    url= urllib.request.urlopen("http://json.stopfraud.cyou:8000")
    data = json.loads(url.read().decode())
#    print(data)

    proxies={'https':'http://'+pip}
    print(proxies)

    json2={\
      "firstName": "\u041a\u0430\u043f\u0447\u0430",\
      "lastName": "\u0412\u0430\u0440\u0432\u0430\u0440\u043e\u0432\u043d\u0430",\
      "email": "captchacheck@yandex.ru",\
      "country": "RU",\
      "phone": "94536985422",\
      "password": "Maxi123*",\
      "terms": "true"\
    }
    json2["firstName"]=data["name"]
    json2["lastName"]=data["surname"]
    json2["email"]=data["email"]
    json2["password"]=data["password"]
    json2["phone"]=data["phone_short"]

    try:    
        r = requests.post('https://maximarkets.org/wp-json/xcritical/1.0/registration',json=json2,proxies=proxies, timeout=15)
        print (r.text)
        print (r.status_code)
        print ('--------------------')
        if 'leadGuid' in r.text:
            print('::::::::::MAXI reg OK:::::::::::')
            print(data['name'])
            print(data['surname'])
            print(data['email'])
            print(data['password'])
            _cred('maxi',data['email'],data['password'])
    except Exception as e:
        print (e)
        pass




def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    service_check(body.decode("utf-8"))


RABBITMQ_SERVER=os.getenv("RABBITMQ_SERVER")
RABBITMQ_USER=os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD=os.getenv("RABBITMQ_PASSWORD")



while True:
    try:
        credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
        parameters = pika.ConnectionParameters(RABBITMQ_SERVER,
                                       5672,
                                       '/',
                                       credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
#        channel.basic_qos(prefetch_count=1, global_qos=False)
        channel.queue_declare(queue='maxi')
        channel.basic_consume(queue='maxi', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
#    except pika.exceptions.AMQPConnectionError:
#        print ("retry connecting to rabbit")
#        time.sleep(6)
    except Exception as e1:
        print (e1)
        print ("retry connecting to rabbit")
        time.sleep(6)

