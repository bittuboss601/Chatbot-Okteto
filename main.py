import requests
url = 'https://bittuchatbot.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
"message": "Hey",
"sender": 1,
}
x = requests.post(url, json = myobj)
print(x.text)