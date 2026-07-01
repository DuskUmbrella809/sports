from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer

from sports.services.scoreboard_service import ScoreboardService
from sports.widgets.sidebar import Sidebar
from sports.widgets.scoreboard import Scoreboard


class DashboardScreen(Screen):

    def compose(self) -> ComposeResult:
        self.service = ScoreboardService()

        self.scoreboard = Scoreboard(
            self.service.get_matches()
        )

        yield Header()

        with Horizontal():
            yield Sidebar()
            yield self.scoreboard

        yield Footer()

    def on_mount(self) -> None:
        self.set_interval(10, self.refresh_scores)

    def refresh_scores(self) -> None:
        matches = self.service.get_matches()
        self.scoreboard.update_matches(matches)