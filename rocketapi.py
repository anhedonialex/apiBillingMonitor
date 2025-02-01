import requests
import json

import secrets
import telegram

url = "https://v1.rocketapi.io/usage"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Token " + secrets.insta_rocket_api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    limit = int(response.json()["limit"])
    requests = int(response.json()["requests"])
    percentage = (requests) * 100 / limit
    print(percentage)
    if percentage > 60:
        telegram.bot_sendtext(
            f"Опасно!\nInstagram RocketAPI истрачен на {percentage:.2f}%\nПотрачено: {requests:,} запросов\nОсталось: {limit - requests:,} запросов\nЛимит: {limit:,}")
    else:
        telegram.bot_sendtext(
            f"Instagram RocketAPI истрачен на {percentage:.2f}%\nПотрачено: {requests:,} запросов\nОсталось: {limit - requests:,} запросов\nЛимит: {limit:,}")
        print("yay")

else:
    telegram.bot_sendtext(__file__ + "\n\nNot responding")
