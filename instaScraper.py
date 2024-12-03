import requests
import json

import secrets
import telegram

url = "https://instagram-scraper-api2.p.rapidapi.com/v1/info"

querystring = {"username_or_id_or_url":"mrbeast"}

headers = {
	"X-RapidAPI-Key": secrets.instaapi_key,
	"X-RapidAPI-Host": "instagram-scraper-api2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
print(response.headers)
'''
import json
with open('data.json', 'w') as f:
    json.dump(response.json(), f)
'''
if response.status_code == 200:
    limit = int(response.headers["X-RateLimit-Requests-Limit"])
    remaining = int(response.headers["X-RateLimit-Requests-Remaining"])
    percentage = (limit-remaining)*100/limit
    print(percentage)
    if percentage > 60:
        #pass
        telegram.bot_sendtext(f"Опасно!\nInstaScraper истрачен на {percentage:.2f}%\nПотрачено: {limit-remaining:,} запросов\nОсталось: {remaining:,} запросов\nЛимит: {limit:,}")
    else:
        telegram.bot_sendtext(f"InstaScraper истрачен на {percentage:.2f}%\nПотрачено: {limit - remaining:,} запросов\nОсталось: {remaining:,} запросов\nЛимит: {limit:,}")
        print("yay")