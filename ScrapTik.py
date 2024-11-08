import requests
import json

import secrets
import telegram

url = "https://scraptik.p.rapidapi.com/get-user"
querystring = {"sec_user_id":"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}

headers = {
	"x-rapidapi-key": secrets.youtube_md_api_key,
	"x-rapidapi-host": "scraptik.p.rapidapi.com"
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

    if percentage > 60:
        pass
        telegram.bot_sendtext(f"Опасно!\nScrapTik истрачен на {percentage:.2f}%\nПотрачено: {limit-remaining:,} запросов\nОсталось: {remaining:,} запросов\nЛимит: {limit:,}")
    else:
        print(f"ScrapTik истрачен на {percentage:.2f}%\nПотрачено: {limit-remaining:,} запросов\nОсталось: {remaining:,} запросов\nЛимит: {limit:,}")
        telegram.bot_sendtext(f"ScrapTik истрачен на {percentage:.2f}%\nПотрачено: {limit - remaining:,} запросов\nОсталось: {remaining:,} запросов\nЛимит: {limit:,}")
        print("yay")
