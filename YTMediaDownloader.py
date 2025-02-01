import requests
import json

import api_check
import secrets
import telegram

url = "https://youtube-media-downloader.p.rapidapi.com/v2/channel/details"
querystring = {"channelId":"UCuAXFkgsw1L7xaCfnd5JJOw"}

headers = {
	"x-rapidapi-key": secrets.youtube_md_api_key,
	"x-rapidapi-host": "youtube-media-downloader.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
api_check.check("YouTube Media Downloader", response)