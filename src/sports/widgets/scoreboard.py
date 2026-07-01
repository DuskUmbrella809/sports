from collections import defaultdict

from rich.text import Text
from textual.containers import VerticalScroll
from textual.widgets import Static

from sports.models import Match


class Scoreboard(VerticalScroll):
    def __init__(self, matches: list[Match]):
        super().__init__()

        self.matches = matches

    def compose(self):
        yield Static(self.build_dashboard())

    def build_dashboard(self) -> Text:
        text = Text()

        leagues = defaultdict(list)

        for match in self.matches:
            leagues[match.league].append(match)

        for league in sorted(leagues):

            text.append(f"🏆 {league}\n", style="bold cyan")
            text.append("─" * 62 + "\n", style="dim")

            for match in leagues[league]:

                text.append(
                    f"{match.home_team:<28}",
                    style="bold white",
                )

                text.append(
                    f"{match.home_score} - {match.away_score}",
                    style="bold green",
                )

                text.append(
                    f"{match.away_team:>28}",
                    style="bold white",
                )

                text.append(
                    f"   {match.status}\n",
                    style="yellow",
                )

            text.append("\n")

        return text

    def update_matches(self, matches):
        self.matches = matches

        self.remove_children()

        self.mount(
            Static(
                self.build_dashboard()
            )
        )