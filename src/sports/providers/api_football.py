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

    def get_match_stats(
        self,
        fixture_id: int,
    ) -> dict:

        response = requests.get(
            f"{self.BASE_URL}/fixtures/statistics",
            headers={
                "x-apisports-key": API_FOOTBALL_KEY,
            },
            params={
                "fixture": fixture_id,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()["response"]

        if len(data) < 2:
            return {
                "shots": 0,
                "shots_on_target": 0,
                "corners": 0,
                "yellow_cards": 0,
                "red_cards": 0,
                "substitutions": 0,
            }

        home = data[0]
        away = data[1]

        def get_stat(team: dict, stat_name: str) -> int:
            for stat in team["statistics"]:
                if stat["type"] == stat_name:
                    return stat["value"] or 0
            return 0

        return {
            "shots": (
                get_stat(home, "Total Shots")
                + get_stat(away, "Total Shots")
            ),
            "shots_on_target": (
                get_stat(home, "Shots on Goal")
                + get_stat(away, "Shots on Goal")
            ),
            "corners": (
                get_stat(home, "Corner Kicks")
                + get_stat(away, "Corner Kicks")
            ),
            "yellow_cards": (
                get_stat(home, "Yellow Cards")
                + get_stat(away, "Yellow Cards")
            ),
            "red_cards": (
                get_stat(home, "Red Cards")
                + get_stat(away, "Red Cards")
            ),
            "substitutions": (
                get_stat(home, "Substitutions")
                + get_stat(away, "Substitutions")
            ),
        }