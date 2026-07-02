from dataclasses import dataclass, field
from datetime import datetime

from sports.models import Match


@dataclass
class AppState:
    matches: list[Match] = field(default_factory=list)

    selected_match: Match | None = None

    favorites: set[str] = field(default_factory=set)

    api_connected: bool = False

    last_refresh: datetime | None = None

    is_loading: bool = False

    error: str | None = None

    def update_matches(
        self,
        matches: list[Match],
    ) -> None:

        self.matches = matches

        self.api_connected = True

        self.last_refresh = datetime.now()

        self.error = None

    def set_error(
        self,
        message: str,
    ) -> None:

        self.api_connected = False

        self.error = message