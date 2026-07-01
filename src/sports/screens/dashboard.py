from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header

from sports.services.scoreboard_service import ScoreboardService
from sports.widgets.match_table import MatchTable
from sports.widgets.sidebar import Sidebar


class DashboardScreen(Screen):
    def compose(self) -> ComposeResult:
        self.service = ScoreboardService()

        self.match_table = MatchTable(
            self.service.get_matches()
        )

        yield Header()

        with Horizontal():
            yield Sidebar()
            yield self.match_table

        yield Footer()

    def on_mount(self) -> None:
        self.set_interval(10, self.refresh_scores)

    def refresh_scores(self) -> None:
        matches = self.service.get_matches()
        self.match_table.update_matches(matches)