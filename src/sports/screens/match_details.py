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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 {self.match.league}

⚽ MATCH CENTER

{self.match.home_team}
      {self.match.home_score} - {self.match.away_score}
{self.match.away_team}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱ Status

{self.match.status}

🌍 Country

{self.match.country}

🆔 Fixture ID

{self.match.fixture_id}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 MATCH SUMMARY

⚽ Total Goals..............{int(self.match.home_score) + int(self.match.away_score)}

🏠 Home Team...............{self.match.home_team}

🛫 Away Team...............{self.match.away_team}

🏆 Competition.............{self.match.league}

🌍 Location................{self.match.country}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📰 LIVE TIMELINE

No live events available.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 LINEUPS

Lineups are not available for this match.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 STANDINGS

Standings are not available for this competition.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Press ESC to return.
"""
        )

        yield Footer()