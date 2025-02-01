import requests
import json

import api_check
import secrets
import telegram

url = "https://scraptik.p.rapidapi.com/get-user"
querystring = {"sec_user_id":"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}

headers = {
	"x-rapidapi-key": secrets.youtube_md_api_key,
	"x-rapidapi-host": "scraptik.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
api_check.check("ScrapTik", response)