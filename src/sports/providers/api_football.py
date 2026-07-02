import requests

from sports.config.settings import API_FOOTBALL_KEY
from sports.models import Match
from sports.providers.base import BaseProvider


class APIFootballProvider(BaseProvider):
    BASE_URL = "https://v3.football.api-sports.io"

    def get_matches(self) -> list[Match]:
        response = requests.get(
            f"{self.BASE_URL}/fixtures",
            headers={
                "x-apisports-key": API_FOOTBALL_KEY,
            },
            params={
                "live": "all",
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        matches = []

        for fixture in data["response"]:
            matches.append(
                Match(
                    fixture_id=fixture["fixture"]["id"],

                    league=fixture["league"]["name"],
                    country=fixture["league"]["country"],

                    home_team=fixture["teams"]["home"]["name"],
                    away_team=fixture["teams"]["away"]["name"],

                    home_score=str(fixture["goals"]["home"] or 0),
                    away_score=str(fixture["goals"]["away"] or 0),

                    status=fixture["fixture"]["status"]["short"],
                )
            )

        return matches