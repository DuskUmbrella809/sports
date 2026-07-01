import requests

from sports.models import Match


class ESPNProvider:
    BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world"

    def get_matches(self):

        response = requests.get(
            f"{self.BASE_URL}/scoreboard",
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        matches = []

        for event in data["events"]:

            competition = event["competitions"][0]

            home = competition["competitors"][0]
            away = competition["competitors"][1]

            matches.append(
                Match(
                    home_team=home["team"]["displayName"],
                    away_team=away["team"]["displayName"],
                    home_score=home["score"],
                    away_score=away["score"],
                    status=competition["status"]["type"]["shortDetail"],
                )
            )

        return matches