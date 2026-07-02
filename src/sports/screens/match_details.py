from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Footer, Header, Static

from sports.models import Match


class MatchDetailsScreen(Screen):

    BINDINGS = [
        Binding("escape", "app.pop_screen", "Back"),
    ]

    def __init__(self, match: Match):
        super().__init__()

        self.match = match

    def compose(self) -> ComposeResult:

        yield Header()

        yield Static(
            f"""

🏆 {self.match.league}

{self.match.home_team}

{self.match.home_score} - {self.match.away_score}

{self.match.away_team}

Country:
{self.match.country}

Status:
{self.match.status}

----------------------------------------

Statistics coming soon...

Timeline coming soon...

Lineups coming soon...

Standings coming soon...

"""
        )

        yield Footer()