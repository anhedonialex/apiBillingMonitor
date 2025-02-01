import sys
import requests
import secrets
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

url = 'https://api.chatpush.ru/api/v1/account'

data = {}

headers = {
    'Authorization': 'Bearer ' + secrets.chatpush_bearer,
}

response = requests.get(
    url,
    data=data,
    headers=headers,
    timeout=30
)

print(response.status_code)

result = response.json()
if response.status_code == 200:
    money = float(result["account"]["total_amount"])
    registry = CollectorRegistry()
    g = Gauge('chatpush_balance', 'Current balance in the account', registry=registry)
    g.set(money)
    push_to_gateway(secrets.pushgateway_ip, job='chatpush_balance_job', registry=registry)
else:
    sys.exit(1)
