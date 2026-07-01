from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from sports.services.scoreboard_service import ScoreboardService
from sports.widgets.scoreboard import Scoreboard


class SportsApp(App):
    TITLE = "SPORTS"
    SUB_TITLE = "Live World Cup Tracker"

    def compose(self) -> ComposeResult:
        self.service = ScoreboardService()

        self.scoreboard = Scoreboard(
            self.service.get_matches()
        )

        yield Header()
        yield self.scoreboard
        yield Footer()

    def on_mount(self) -> None:
        self.set_interval(10, self.refresh_scores)

    def refresh_scores(self) -> None:
        print("Refreshing...")
        matches = self.service.get_matches()
        self.scoreboard.update_matches(matches)