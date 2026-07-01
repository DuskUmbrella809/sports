from textual.widgets import DataTable

from sports.models import Match


class MatchTable(DataTable):

    def __init__(self, matches: list[Match]):
        super().__init__()

        self.matches = matches

    def on_mount(self) -> None:

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