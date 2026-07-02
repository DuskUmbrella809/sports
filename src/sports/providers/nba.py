import requests

from sports.config.settings import API_FOOTBALL_KEY
from sports.models import Match
from sports.providers.base import BaseProvider


class NBAProvider(BaseProvider):
    BASE_URL = "https://v2.nba.api-sports.io"

    def get_matches(self) -> list[Match]:
        response = requests.get(
            f"{self.BASE_URL}/games",
            headers={
                "x-apisports-key": API_FOOTBALL_KEY,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        matches: list[Match] = []

        for game in data.get("response", []):

            matches.append(
                Match(
                    fixture_id=int(game["id"]),

                    league=game["league"]["name"],
                    country=game["country"]["name"],

                    home_team=game["teams"]["home"]["name"],
                    away_team=game["teams"]["visitors"]["name"],

                    home_score=str(
                        game["scores"]["home"]["points"] or 0
                    ),
                    away_score=str(
                        game["scores"]["visitors"]["points"] or 0
                    ),

                    status=game["status"]["long"],
                )
            )

        return matches