from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Footer, Header

from sports.services.event_service import EventService
from sports.services.scoreboard_service import ScoreboardService
from sports.widgets.event_feed import EventFeed
from sports.widgets.match_table import MatchSelected, MatchTable
from sports.widgets.sidebar import Sidebar


class DashboardScreen(Screen):
    def compose(self) -> ComposeResult:
        self.scoreboard_service = ScoreboardService()
        self.event_service = EventService()

        self.matches = self.scoreboard_service.get_matches()

        self.match_table = MatchTable(self.matches)
        self.event_feed = EventFeed()

        yield Header()

        with Horizontal():
            yield Sidebar()

            with Vertical():
                yield self.match_table
                yield self.event_feed

        yield Footer()

    def on_mount(self) -> None:
        self.set_interval(10, self.refresh_dashboard)

        # Load events for the first match when the app starts
        if self.matches:
            self.load_events(self.matches[0])

    def refresh_dashboard(self) -> None:
        self.matches = self.scoreboard_service.get_matches()
        self.match_table.update_matches(self.matches)

    def load_events(self, match) -> None:
        try:
            events = self.event_service.get_events(match.fixture_id)
            self.event_feed.update_events(events)
        except Exception as e:
            self.event_feed.update(
                f"Unable to load events.\n\n{e}"
            )

    def on_match_selected(
        self,
        message: MatchSelected,
    ) -> None:
        self.load_events(message.match)