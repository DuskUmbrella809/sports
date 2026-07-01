from textual.widgets import Static


class Sidebar(Static):
    def render(self) -> str:
        return """
⚽ SPORTS

⭐ Favorites

🔴 Live

⚽ Soccer

🏈 NFL

🏀 NBA

⚾ MLB

🏒 NHL

🏎 Formula 1

🥊 UFC
"""