import requests
import secrets
import telegram

chatpush_history = open("chatpush_history.txt", "r+")
chatpush_history_list = list(map(int, chatpush_history.read().split()))
try:
    last = chatpush_history_list[-1]
except:
    last = 0

url = 'https://api.chatpush.ru/api/v1/account'

data = {}

headers = {
    'Authorization': 'Bearer ' + secrets.chatpush_bearer,
}

response = requests.get(
    url,
    data=data,
    headers=headers,
    timeout=30
)

print(response.status_code)

result = response.json()
if response.status_code == 200:
    money = int(float(result["account"]["total_amount"]))
    chatpush_history.write(f"{money}\n")
    delta = last - money
    # telegram.bot_sendtext(f"Сейчас {money}\nЧас назад {last}")
    if delta >= secrets.chatpush_delta_threshold:
        telegram.bot_sendtext(f"С последнего запроса на чатпуше ушло {delta} рэ\nВозможно спам")
    else:
        print(delta, 'yay')
