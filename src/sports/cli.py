from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text

from sports.providers.espn import ESPNProvider

console = Console()


def build_match_panel(match):

    body = Text()

    body.append(f"{match.home_team}\n", style="bold cyan")

    body.append("\n")

    body.append(
        f"{match.home_score} - {match.away_score}\n",
        style="bold white",
    )

    body.append("\n")

    body.append(f"{match.away_team}\n", style="bold green")

    body.append("\n")

    body.append(match.status, style="yellow")

    return Panel(
        body,
        title="⚽ Match",
        border_style="blue",
    )


def main():

    provider = ESPNProvider()

    matches = provider.get_matches()

    panels = []

    for match in matches:
        panels.append(build_match_panel(match))

    console.print()

    console.print(
        Columns(
            panels,
            equal=True,
            expand=True,
        )
    )

    console.print()