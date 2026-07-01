from rich.text import Text
from textual.widgets import Static

from sports.models import Match


class MatchCard(Static):
    def __init__(self, match: Match) -> None:
        super().__init__()

        self.match = match

    def render(self) -> Text:
        text = Text()

        # League
        text.append(f"🏆 {self.match.league}", style="bold cyan")

        if self.match.country:
            text.append(f" ({self.match.country})", style="dim")

        text.append("\n\n")

        # Home Team
        text.append("⚽ ", style="yellow")
        text.append(self.match.home_team, style="bold white")
        text.append("\n")

        # Score
        text.append(
            f"      {self.match.home_score}  —  {self.match.away_score}\n",
            style="bold green",
        )

        # Away Team
        text.append("⚽ ", style="yellow")
        text.append(self.match.away_team, style="bold white")

        text.append("\n\n")

        # Status colors
        status = self.match.status

        if status == "FT":
            status_style = "red"
        elif status == "HT":
            status_style = "yellow"
        elif status in ("1H", "2H", "LIVE"):
            status_style = "green"
        else:
            status_style = "cyan"

        text.append("Status: ", style="bold")
        text.append(status, style=status_style)

        return text