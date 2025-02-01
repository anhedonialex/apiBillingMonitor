import requests
import json

import api_check
import secrets
import telegram

url = "https://instagram-scraper-2022.p.rapidapi.com/ig/user_id/"

querystring = {"user":"cr7cristianoronaldo"}

headers = {
	"x-rapidapi-key": secrets.instaapi_key,
	"x-rapidapi-host": "instagram-scraper-2022.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
api_check.check("Instagram Scraper 2022", response)