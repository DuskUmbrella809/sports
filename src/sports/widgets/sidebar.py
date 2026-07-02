from textual.app import ComposeResult
from textual.message import Message
from textual.widgets import Label, ListItem, ListView


class SportSelected(Message):
    def __init__(self, sport: str):
        super().__init__()
        self.sport = sport


class Sidebar(ListView):

    SPORTS = [
        ("⭐ Favorites", "favorites"),
        ("🔴 Live", "live"),
        ("⚽ Soccer", "soccer"),
        ("🏀 NBA", "nba"),
        ("🏈 NFL", "nfl"),
        ("⚾ MLB", "mlb"),
        ("🏒 NHL", "nhl"),
        ("🏎 Formula 1", "formula1"),
        ("🥊 UFC", "ufc"),
    ]

    def compose(self) -> ComposeResult:
        for label, sport in self.SPORTS:
            item = ListItem(Label(label))
            item.sport = sport
            yield item

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.post_message(
            SportSelected(
                event.item.sport
            )
        )