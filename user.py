#1bqlnNV0sA3FtWdEZCahTxkrQmM4y7YeDvJ2i0PKcogBSG8wjX16
#1RBW6MOB353570065EZY59804bke5MLF35621UHL493747985ri
#1MLP6XZB3AUP70055jnn5mta9614168315923WSG4ALH6sky7DWB
import random,requests
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
userId="".join(random.sample(characters, 51))
userId="1"+userId
print (userId)
json1={
  "userId": "1MLP6XZB3AUP70055jnn5mta9614168315923WSG4ALH6sky7DWB",
  "userName": "Валентина",
  "phone": None,
  "email": "sleta88841@yandex.ru",
  "lastName": None,
  "firstName": None,
  "invoiceNumber": None,
  "accountNumber": None,
  "channelId": "58614a56-7139-4052-9356-c6d333c4152c",
  "messenger": "smartbot"
}
json1["userId"]=userId
print(json1)
r = requests.post('https://ask.globalcloudteam.com/chat-backend/client_auth',json=json1, timeout=15)
print (r.text)
print (r.status_code)

r=requests.get('https://ask.globalcloudteam.com/chat-backend/channels/58614a56-7139-4052-9356-c6d333c4152c/clients/'+'1a9dce48-d27d-43c7-a97f-45b961a9a09c/assigned_agent')
print (r.content)
print (r.status_code)