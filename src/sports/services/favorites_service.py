import json
from pathlib import Path


class FavoritesService:
    FILE = Path.home() / ".sports_favorites.json"

    def __init__(self):
        self.favorites = self.load()

    def load(self) -> set[int]:
        if not self.FILE.exists():
            return set()

        try:
            with open(self.FILE, "r") as file:
                data = json.load(file)

            return set(data)

        except Exception:
            return set()

    def save(self) -> None:
        with open(self.FILE, "w") as file:
            json.dump(
                list(self.favorites),
                file,
                indent=4,
            )

    def add(self, fixture_id: int) -> None:
        self.favorites.add(fixture_id)
        self.save()

    def remove(self, fixture_id: int) -> None:
        self.favorites.discard(fixture_id)
        self.save()

    def is_favorite(self, fixture_id: int) -> bool:
        return fixture_id in self.favorites