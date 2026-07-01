from rich.console import Console
from rich.table import Table

from sports.providers.espn import ESPNProvider

console = Console()


def main():
    provider = ESPNProvider()

    data = provider.get_scoreboard()

    table = Table(title="⚽ World Cup Matches")

    table.add_column("Home")
    table.add_column("Away")
    table.add_column("Status")

    for event in data["events"]:
        competition = event["competitions"][0]

        home = competition["competitors"][0]["team"]["displayName"]
        away = competition["competitors"][1]["team"]["displayName"]

        status = competition["status"]["type"]["shortDetail"]

        table.add_row(home, away, status)

    console.print(table)