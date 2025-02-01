import requests
import api_check
import secrets

url = "https://tiktok-scraper7.p.rapidapi.com/feed/search"

querystring = {"keywords": "fyp", "region": "us", "count": "10", "cursor": "0", "publish_time": "0", "sort_type": "0"}

headers = {
    "x-rapidapi-key": secrets.instaapi_key,
    "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
api_check.check("Tiktok Scraper", response)
