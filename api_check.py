import requests
import secrets
import telegram


def check(service_name, response):
    """Обрабатывает response и отправляет уведомление в Telegram."""
    print(response.json())
    print(response.headers)
    if response.status_code == 200:
        limit = int(
            response.headers.get("X-RateLimit-Requests-Limit") or
            response.headers.get("X-RateLimit-Scraping-API-Limit") or
            response.headers.get("X-RateLimit-All-Limit", 1))

        remaining = int(
            response.headers.get("X-RateLimit-Requests-Remaining") or
            response.headers.get("X-RateLimit-Scraping-API-Remaining") or
            response.headers.get("X-RateLimit-All-Remaining", 0))
        percentage = (limit - remaining) * 100 / limit

        answer_str = (f"{service_name} истрачен на {percentage:.2f}%\n"
                      f"Потрачено: {limit - remaining:,} запросов\n"
                      f"Осталось: {remaining:,} запросов\n"
                      f"Лимит: {limit:,}")

        if percentage > 60:
            answer_str = f"Опасно!\n" + answer_str

        try:
            print(response.json())
        except:
            answer_str += "\n\nNot responding"

        telegram.bot_sendtext(answer_str)
    else:
        telegram.bot_sendtext(f"{service_name}: Ошибка запроса\nКод: {response.status_code}\nОтвет: {response.text}")
