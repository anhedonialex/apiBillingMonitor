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
    answer_str = f"ScrapTik истрачен на {percentage:.2f}%\nПотрачено: {limit-remaining:,} запросов\nОсталось: {remaining:,} запросов\nЛимит: {limit:,}"
    if percentage > 60:
        answer_str = f"Опасно!\n" + answer_str
    try:
        print(response.json())
    except:
        answer_str = answer_str + "\nNot responding"
    telegram.bot_sendtext(answer_str)
else:
    telegram.bot_sendtext(__file__ + "\nNot responding")