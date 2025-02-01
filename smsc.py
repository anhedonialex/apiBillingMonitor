import requests
import telegram

url = 'https://smsc.ru/sys/balance.php?login='

data = {}

headers = {}

response = requests.get(
    url,
    data=data,
    headers=headers,
    timeout=30
)

print(response.status_code)

result = response.json()
if response.status_code == 200:
    if int(float(result)) < 15000:
        telegram.bot_sendtext("На смсцентре менее 15к")
    else:
        print("yay")
