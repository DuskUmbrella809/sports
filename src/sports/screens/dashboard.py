from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.timer import Timer

from sports.models import Match
from sports.services.event_service import EventService
from sports.services.favorites_service import FavoritesService
from sports.services.scoreboard_service import ScoreboardService
from sports.widgets.app_header import AppHeader
from sports.widgets.event_feed import EventFeed
from sports.widgets.match_table import (
    FavoriteRequested,
    MatchSelected,
    MatchTable,
)
from sports.widgets.sidebar import (
    Sidebar,
    SportSelected,
)
from sports.widgets.status_bar import StatusBar


class DashboardScreen(Screen):
    def compose(self) -> ComposeResult:
        self.scoreboard_service = ScoreboardService()
        self.event_service = EventService()
        self.favorites_service = FavoritesService()

        self.matches = self.scoreboard_service.get_matches()

        self.match_table = MatchTable(self.matches)
        self.event_feed = EventFeed()

        self.header = AppHeader()
        self.status_bar = StatusBar()

        self.selected_match: Match | None = None
        self.event_timer: Timer | None = None

        yield self.header

        with Vertical():

            with Horizontal():
                yield Sidebar()

                with Vertical():
                    yield self.match_table
                    yield self.event_feed

            yield self.status_bar

    def on_mount(self) -> None:
        self.set_interval(10, self.refresh_dashboard)

        if self.matches:
            self.selected_match = self.matches[0]
            self.load_events()

    def refresh_dashboard(self) -> None:
        self.matches = self.scoreboard_service.get_matches()
        self.match_table.update_matches(self.matches)

    def load_events(self) -> None:
        if self.selected_match is None:
            return

        try:
            events = self.event_service.get_events(
                self.selected_match.fixture_id
            )
            self.event_feed.update_events(events)

        except Exception:
            self.event_feed.update(
                "⚠ Unable to load live events."
            )

    def on_match_selected(
        self,
        message: MatchSelected,
    ) -> None:

        self.selected_match = message.match

        if self.event_timer:
            self.event_timer.stop()

        self.event_timer = self.set_timer(
            0.5,
            self.load_events,
        )

    def on_favorite_requested(
        self,
        message: FavoriteRequested,
    ) -> None:

        match = message.match

        if self.favorites_service.is_favorite(match.fixture_id):
            self.favorites_service.remove(match.fixture_id)

            self.event_feed.update(
                f"⭐ Removed from favorites\n\n"
                f"{match.home_team} vs {match.away_team}"
            )
        else:
            self.favorites_service.add(match.fixture_id)

            self.event_feed.update(
                f"⭐ Added to favorites\n\n"
                f"{match.home_team} vs {match.away_team}"
            )

        self.status_bar.update_status(
            sport="Soccer",
            connection="🟢 Connected",
            updated="Just now",
            favorites=self.favorites_service.count(),
        )

    def on_sport_selected(
        self,
        message: SportSelected,
    ) -> None:

        if message.sport in ("favorites", "live"):
            self.event_feed.update(
                f"📂 {message.sport.title()} coming soon..."
            )
            return

        try:
            self.scoreboard_service.set_provider(
                message.sport
            )

            self.matches = (
                self.scoreboard_service.get_matches()
            )

            self.match_table.update_matches(
                self.matches
            )

            sport_name = message.sport.replace(
                "formula1",
                "Formula 1",
            ).title()

            self.header.update_header(
                sport=sport_name,
                status="🟢 Connected",
            )

            self.status_bar.update_status(
                sport=sport_name,
                connection="🟢 Connected",
                updated="Just now",
                favorites=self.favorites_service.count(),
            )

            if self.matches:
                self.selected_match = self.matches[0]
                self.load_events()
            else:
                self.event_feed.update(
                    f"🏆 Switched to {sport_name}\n\n"
                    "No games available."
                )

        except Exception as e:
            self.event_feed.update(
                f"❌ Failed to switch provider\n\n{e}"
            )