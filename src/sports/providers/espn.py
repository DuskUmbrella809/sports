import requests


class ESPNProvider:
    BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world"

    def get_scoreboard(self):
        response = requests.get(
            f"{self.BASE_URL}/scoreboard",
            timeout=10,
        )

        response.raise_for_status()

        return response.json()