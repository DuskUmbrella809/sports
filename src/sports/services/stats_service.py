from sports.models import MatchStats
from sports.providers.api_football import APIFootballProvider


class StatsService:
    def __init__(self):
        self.provider = APIFootballProvider()

    def get_stats(
        self,
        fixture_id: int,
    ) -> MatchStats:

        try:
            return self.provider.get_match_stats(
                fixture_id
            )

        except Exception:

            return MatchStats(
                shots=0,
                shots_on_target=0,
                corners=0,
                yellow_cards=0,
                red_cards=0,
                substitutions=0,
            )