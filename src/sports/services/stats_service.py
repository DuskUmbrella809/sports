from sports.models import MatchStats
from sports.providers.api_football import APIFootballProvider


class StatsService:
    def __init__(self):
        self.provider = APIFootballProvider()

    def get_stats(
        self,
        fixture_id: int,
    ) -> MatchStats:
        """
        Retrieve detailed statistics for a match.

        If the API is unavailable or the fixture has no
        statistics yet, return an empty MatchStats object.
        """

        try:
            data = self.provider.get_match_stats(
                fixture_id
            )

            if not data:
                return self._empty_stats()

            return MatchStats(
                goals=data.get("goals", 0),
                shots=data.get("shots", 0),
                shots_on_target=data.get(
                    "shots_on_target",
                    0,
                ),
                corners=data.get("corners", 0),
                yellow_cards=data.get(
                    "yellow_cards",
                    0,
                ),
                red_cards=data.get(
                    "red_cards",
                    0,
                ),
                substitutions=data.get(
                    "substitutions",
                    0,
                ),
            )

        except Exception as error:
            print(f"⚠ StatsService: {error}")
            return self._empty_stats()

    def _empty_stats(self) -> MatchStats:
        return MatchStats(
            goals=0,
            shots=0,
            shots_on_target=0,
            corners=0,
            yellow_cards=0,
            red_cards=0,
            substitutions=0,
        )