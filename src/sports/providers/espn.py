import requests

from sports.models import Match


class ESPNProvider:
    BASE_URL = (
        "https://site.api.espn.com/apis/site/v2/"
        "sports/soccer/fifa.world"
    )

    def get_matches(self) -> list[Match]:
        response = requests.get(
            f"{self.BASE_URL}/scoreboard",
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        matches: list[Match] = []

        for event in data.get("events", []):

            competition = event["competitions"][0]

            competitors = competition["competitors"]

            home = next(
                team
                for team in competitors
                if team["homeAway"] == "home"
            )

            away = next(
                team
                for team in competitors
                if team["homeAway"] == "away"
            )

            league = (
                competition.get("league", {})
                .get("name", "Unknown League")
            )

            country = (
                competition.get("venue", {})
                .get("address", {})
                .get("country", "Unknown")
            )

            matches.append(
                Match(
                    fixture_id=int(event["id"]),
                    league=league,
                    country=country,
                    home_team=home["team"]["displayName"],
                    away_team=away["team"]["displayName"],
                    home_score=home.get("score", "0"),
                    away_score=away.get("score", "0"),
                    status=competition["status"]["type"][
                        "shortDetail"
                    ],
                )
            )

        return matches