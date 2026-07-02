import requests

from sports.providers.api_football import APIFootballProvider
from sports.models import Match


class ScoreboardService:
    def __init__(self):
        self.provider = APIFootballProvider()
        self._cache: list[Match] = []

    def get_matches(self) -> list[Match]:
        try:
            matches = self.provider.get_matches()

            # Only replace the cache if we got data
            if matches:
                self._cache = matches

            return matches

        except requests.exceptions.Timeout:
            print("⚠ API timeout - using cached data")
            return self._cache

        except requests.exceptions.RequestException as e:
            print(f"⚠ API error: {e}")
            return self._cache

        except Exception as e:
            print(f"⚠ Unexpected error: {e}")
            return self._cache