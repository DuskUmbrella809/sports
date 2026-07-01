from textual.widgets import Static

from sports.models import Match


class MatchCard(Static):
    """A single match card."""

    def __init__(self, match: Match) -> None:
        super().__init__()

        self.match = match

    def render(self) -> str:
        return f"""
🏠 {self.match.home_team}

      {self.match.home_score} - {self.match.away_score}

✈ {self.match.away_team}

⏱ {self.match.status}
"""