from textual.binding import Binding
from textual.message import Message
from textual.widgets import DataTable

from sports.models import Match
from sports.screens.match_details import MatchDetailsScreen
from sports.screens.search import SearchScreen


class MatchSelected(Message):
    """Sent whenever the highlighted match changes."""

    def __init__(self, match: Match) -> None:
        super().__init__()
        self.match = match


class MatchTable(DataTable):

    BINDINGS = [
        Binding("/", "search", "Search"),
    ]

    def __init__(self, matches: list[Match]):
        super().__init__()
        self.matches = matches

    def on_mount(self) -> None:
        self.cursor_type = "row"

        self.add_columns(
            "League",
            "Home",
            "Score",
            "Away",
            "Status",
        )

        self.load_matches()

    def load_matches(self) -> None:
        self.clear()

        for match in self.matches:
            self.add_row(
                match.league,
                match.home_team,
                f"{match.home_score} - {match.away_score}",
                match.away_team,
                match.status,
            )

    def update_matches(self, matches: list[Match]) -> None:
        self.matches = matches
        self.load_matches()

    def on_data_table_row_highlighted(
        self,
        event: DataTable.RowHighlighted,
    ) -> None:

        row = event.cursor_row

        # No row selected yet
        if row < 0:
            return

        # Safety check
        if row >= len(self.matches):
            return

        self.post_message(
            MatchSelected(
                self.matches[row]
            )
        )

    def on_data_table_row_selected(
        self,
        event: DataTable.RowSelected,
    ) -> None:

        row = event.cursor_row

        if row < 0:
            return

        if row >= len(self.matches):
            return

        self.app.push_screen(
            MatchDetailsScreen(
                self.matches[row]
            )
        )

    def action_search(self) -> None:
        self.app.push_screen(
            SearchScreen()
        )