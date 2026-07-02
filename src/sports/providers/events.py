import requests

from sports.config.settings import API_FOOTBALL_KEY


class EventProvider:
    BASE_URL = "https://v3.football.api-sports.io"

    def get_events(self, fixture_id: int) -> list[dict]:
        response = requests.get(
            f"{self.BASE_URL}/fixtures/events",
            headers={
                "x-apisports-key": API_FOOTBALL_KEY,
            },
            params={
                "fixture": fixture_id,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]