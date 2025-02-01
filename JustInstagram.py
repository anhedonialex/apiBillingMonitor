import requests
import api_check
import secrets

url = "https://instagram243.p.rapidapi.com/userinfo/instagram"

headers = {
	"x-rapidapi-key": secrets.instaapi_key,
	"x-rapidapi-host": "instagram243.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
api_check.check("\"Instagram\"", response)