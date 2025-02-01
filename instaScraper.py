import requests
import api_check
import secrets


url = "https://instagram-scraper-api2.p.rapidapi.com/v1/info"

querystring = {"username_or_id_or_url": "mrbeast"}

headers = {
    "X-RapidAPI-Key": secrets.instaapi_key,
    "X-RapidAPI-Host": "instagram-scraper-api2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
api_check.check("InstaScraper", response)
