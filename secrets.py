import dotenv

# SECRETS
env_path = ".env"
instaapi_key = dotenv.get_key(env_path, "INSTA_API")
insta_rocket_api_key = dotenv.get_key(env_path, "INSTA_ROCKET_API")
youtube_md_api_key = dotenv.get_key(env_path, "YOUTUBE_MD_API")
tiktok_scrap_api_key = dotenv.get_key(env_path, "TIKTOK_SCRAP_API")
bot_token = dotenv.get_key(env_path, "BOT_TOKEN")
bot_chatID = dotenv.get_key(env_path, "CHAT_ID")
chatpush_bearer = dotenv.get_key(env_path, "CHATPUSH_BEARER")

# CONFIG
chatpush_threshold = int(dotenv.get_key(env_path, "CHATPUSH_TRESHOLD"))
chatpush_delta_threshold = int(dotenv.get_key(env_path, "CHATPUSH_DELTA_TRESHOLD"))
pushgateway_ip = dotenv.get_key(env_path, "PUSHGATEWAY_IP")
