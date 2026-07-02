from sports.providers.api_football import APIFootballProvider
from sports.providers.nba import NBAProvider


class ProviderManager:
    def __init__(self):
        self.providers = {
            "soccer": APIFootballProvider(),
            "nba": NBAProvider(),
        }

        self.current = "soccer"

    def get_provider(self):
        return self.providers[self.current]

    def set_provider(self, name: str) -> None:
        if name not in self.providers:
            raise ValueError(f"Unknown provider: {name}")

        self.current = name

    def current_provider(self) -> str:
        return self.current

    def available(self) -> list[str]:
        return sorted(self.providers.keys())