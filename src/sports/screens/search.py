from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Input, Footer, Header


class SearchScreen(ModalScreen):

    BINDINGS = [
        Binding("escape", "app.pop_screen", "Close"),
    ]

    def compose(self) -> ComposeResult:

        yield Header()

        with Vertical():

            yield Input(
                placeholder="Search for a team, league, player..."
            )

        yield Footer()