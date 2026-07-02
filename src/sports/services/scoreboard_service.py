import requests

from sports.models import Match
from sports.providers.manager.provider_manager import ProviderManager


class ScoreboardService:
    def __init__(self):
        self.manager = ProviderManager()
        self._cache: list[Match] = []

    @property
    def provider(self):
        return self.manager.get_provider()

    def set_provider(self, name: str) -> None:
        self.manager.set_provider(name)

    def available_providers(self) -> list[str]:
        return self.manager.available()

    def get_matches(self) -> list[Match]:
        try:
            matches = self.provider.get_matches()

            # Only replace the cache if we actually received data
            if matches:
                self._cache = matches

            return self._cache

        except requests.exceptions.Timeout:
            print("⚠ API timeout - using cached data")
            return self._cache

        except requests.exceptions.RequestException as e:
            print(f"⚠ API error: {e}")
            return self._cache

        except Exception as e:
            print(f"⚠ Unexpected error: {e}")
            return self._cache