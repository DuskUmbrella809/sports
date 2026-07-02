import requests
from datetime import date

from sports.config.settings import API_FOOTBALL_KEY

response = requests.get(
    "https://v3.football.api-sports.io/fixtures",
    headers={
        "x-apisports-key": API_FOOTBALL_KEY,
    },
    params={
        "date": date.today().isoformat(),
    },
    timeout=10,
)

print(response.status_code)

data = response.json()

print(data)