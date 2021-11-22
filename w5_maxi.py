import websocket, requests,random, uuid,json
import urllib.request
import time,sys,datetime
logfile='webscoket.log'
def _log(message):
#    fh=open(logfile,"a",encoding="cp1251")
    fh=open(logfile,"a",encoding="utf-8")
    text=str(datetime.datetime.now())+" "+str(message)+"\r\n"
    print(text)
    fh.write(text)
    fh.close()
    return True

import requests

def get_uuid():
    return str(uuid.uuid4())


#main logic

while True:
    url= urllib.request.urlopen("http://json.stopfraud.cyou:8000")
    data = json.loads(url.read().decode())

    characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    userId="".join(random.sample(characters, 51))
    userId="1"+userId
    print (userId)
    json1={
  "userId": "1MLP6XZB3AUP70055jnn5mta9614168315923WSG4ALH6sky7DWB",
  "userName": data["final_name"],
  "phone": data["phone_full"],
  "email": data["email"],
  "lastName": data["surname"],
  "firstName": data["name"],
  "invoiceNumber": None,
  "accountNumber": None,
  "channelId": "58614a56-7139-4052-9356-c6d333c4152c",
  "messenger": "smartbot"
    }
    json1["userId"]=userId
    print(json1)
    r = requests.post('https://ask.globalcloudteam.com/chat-backend/client_auth',json=json1, timeout=15)
    #example {"id":"1a9dce48-d27d-43c7-a97f-45b961a9a09c","status":"active"}
    json2=json.loads(r.text)
    userId=json2["id"]
    print(userId)
#    sys.exit()




#sys.exit()
    websocket.enableTrace(False)
    try:
        ws = websocket.WebSocket()
#    ws2 = websocket.WebSocket()
#        ws.connect("wss://node-eu1-b-1.jivosite.com/cometcn", origin="testing_websockets.com")
        ws.connect('wss://ask.globalcloudteam.com/ws-proxy/ws?pingMsg=.&pingWait=120', origin="https://maximarkets.org")
#    ws2.connect("wss://node103.jivosite.com/cometcn", origin="testing_websockets.com")
#    ws.connect("wss://node-eu1-b-1.jivosite.com/cometcn", origin="testing_websockets.com")

#wss://node-eu1-b-1.jivosite.com/cometcn
        msg={"id":"2b883514-cbb8-4a4b-a355-9d004a864f7a","cmd":"auth_connection","args":{"userId":"1a9dce48-d27d-43c7-a97f-45b961a9a09c","channelId":"58614a56-7139-4052-9356-c6d333c4152c"}}
        msg["args"]["userId"]=userId
        msg['id']=get_uuid()
#        sys.exit()
#        msg['args']['userId']=get_uuid()
        
        print(msg)
        s=json.dumps(msg)
#        print(s)
#        sys.exit()
        ws.send(json.dumps(msg))
        _log(ws.recv())

        time.sleep(1)
#        sys.exit()
        msg={"id":"b83fc67f-b880-4a15-ba76-46961fa54bfe","cmd":"get_client_dialog_messages","args":{"isEarlier":False,"fromMsgID":0,"count":0}}
        msg['id']=get_uuid()
        print(msg)
        ws.send(json.dumps(msg))
        _log(ws.recv())
#        time.sleep(1)
        msg={"id":"54c0e6ac-2601-4d81-aa61-4a9f539d42f2","cmd":"new_message","args":{"text":"С какой биржей работаете?","language":"ru","additionalInfo":{"url":"https://maximarkets.so/contacts/","pageName":"Контакты Форекс Брокера Максимаркетс, поддержка трейдеров | | MaxiMarkets (МаксиМаркетс)"}}}
#        msg={"id":"54c0e6ac-2601-4d81-aa61-4a9f539d42f2","cmd":"new_message","args":{"text":"У меня 3 вопроса по поводу регистрации","language":"ru","additionalInfo":{"url":"https://maximarkets.so/contacts/","pageName":"???????? ?????? ??????? ????????????, ????????? ????????? | | MaxiMarkets (????????????)"}}}
        msg['id']=get_uuid()
        msg["args"]["text"]=data["phrase"]
        ws.send(json.dumps(msg))
        print(msg)
#        _log(ws.recv())
#        sys.exit()

#test below
#        ws.send('{"name":"startup","jv_widget_id":"PLTgSgJhDK","site_id":1761234,"current_page":{"title":"Pulse Trade","url":"https://pulse-trade.com/"},"is_mobile":false,"visits_count":2,"page_visible":true,"chat_opened":true,"widget_version":"46.10.0","history":[{"url":"https://pulse-trade.com/","title":"Pulse Trade","time":1636598569345},{"url":"https://pulse-trade.com/register","title":"Pulse Trade","time":1636520453405}],"new_utm":{"campaign":"(direct)","source":"(direct)"},"visitor_id":"5c632844fb5ca979"}')
#        ws.send('{"name":"startup","jv_widget_id":"vUBkOE6cqi","site_id":1672855,"current_page":{"title":"","url":"https://pulse-trade.com/"},"is_mobile":false,"visits_count":1,"page_visible":true,"chat_opened":true,"widget_version":"46.10.0","history":[{"url":"https://pulse-trade.com/","title":"","time":1636595222879}],"new_utm":{"campaign":"(referral)","source":"jsfiddle.net","medium":"referral","content":"/"},"visitor_id":"68b5a2ea49b916d5"}')
#    ws.send('{"name":"startup","jv_widget_id":"KSPtF7hWOu","site_id":1576660,"current_page":{"title":"24xFOREX","url":"https://24xforex.com/"},"is_mobile":false,"visits_count":1,"page_visible":true,"chat_opened":true,"widget_version":"32.4.0","history":[{"url":"https://24xforex.com/","title":"24xFOREX","time":'+str(t)+'}],"new_utm":{"campaign":"(direct)","source":"(direct)"},"visitor_id":"f07d59bbc15f5547"}')
#    ws2.send('{"name":"startup","jv_widget_id":"CJ3NNhuoCA","site_id":1562477,"current_page":{"title":"Ingoinvest","url":"https://ingoinvest.com/ru"},"is_mobile":false,"visits_count":1,"page_visible":true,"chat_opened":true,"widget_version":"32.4.0","history":[{"url":"https://ingoinvest.com/","title":"Ingoinvest","time":1620538442796},{"url":"https://ingoinvest.com/ru","title":"Ingoinvest","time":1620538511296},{"url":"https://ingoinvest.com/ru/register","title":"Ingoinvest - Ingoinvest","time":1619651663124},{"url":"https://ingoinvest.com/#contact","title":"Ingoinvest","time":1619651013371}],"new_utm":{"campaign":"(direct)","source":"(direct)"},"visitor_id":"a81f44fa643251a2"}')
#                                                                                                                                                                                                                                                      1619908687848
        while True:
            a=ws.recv()
            print(a)
            if 'agent_info' in str(a):
                print("Agent found")
            if '"sender":"agent"' in str(a):

                msg={"id":"54c0e6ac-2601-4d81-aa61-4a9f539d42f2","cmd":"new_message","args":{"text":"С какой биржей работаете?","language":"ru","additionalInfo":{"url":"https://maximarkets.so/contacts/","pageName":"Контакты Форекс Брокера Максимаркетс, поддержка трейдеров | | MaxiMarkets (МаксиМаркетс)"}}}
#        msg={"id":"54c0e6ac-2601-4d81-aa61-4a9f539d42f2","cmd":"new_message","args":{"text":"У меня 3 вопроса по поводу регистрации","language":"ru","additionalInfo":{"url":"https://maximarkets.so/contacts/","pageName":"???????? ?????? ??????? ????????????, ????????? ????????? | | MaxiMarkets (????????????)"}}}
                msg['id']=get_uuid()
                msg["args"]["text"]=data["phone_full"]
                ws.send(json.dumps(msg))
            a=ws.recv()
            print(a)

#    _log(ws2.recv())
#time.sleep(1)
#ws.send('.')
#print(ws.recv())



#        m='{"name":"introduction","client_name":"'+final_name+'","phone":"'+tnf+'","email":"'+email+'","description":null,"accept_eula":null}'
#        _log(m)
#        ws.send(m)
#    ws2.send(m)
#        m='{"name":"client_message","message":"'+question+'","private_id":"a2143b95-a0bd-7990-69cd-1a70f4235961"}'
#        _log(m)
#        ws.send(m)

#    m='{"name":"client_message","message":"'+question+'","private_id":"a2143b95-a0bd-7990-69cd-1a70f4235961"}'
#    _log(m)
#    ws.send(m)


#    ws2.send(m)

#ws.send('{"name":"introduction","client_name":"'+final_name+'","phone":"'+tnf+'","email":"'+email+'","description":null,"accept_eula":null}')
#ws.send('{"name":"client_message","message":"'+question+'","private_id":"a2143b95-a0bd-7990-69cd-1a70f4235961"}')

        _log(ws.recv())
        _log(ws.recv())
        _log(ws.recv())


#print(ws.recv())
#print(ws.recv())
#    sys.exit()
        time.sleep(10)
        ws.close()
    except Exception as e:
        print (e)
        pass

