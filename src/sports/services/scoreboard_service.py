from sports.providers.api_football import APIFootballProvider


class ScoreboardService:
    def __init__(self):
        self.provider = APIFootballProvider()

    def get_matches(self):
        return self.provider.get_matches()