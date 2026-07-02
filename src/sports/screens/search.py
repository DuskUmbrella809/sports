from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.message import Message
from textual.screen import ModalScreen
from textual.widgets import Footer, Header, Input


class SearchSubmitted(Message):
    def __init__(self, query: str):
        super().__init__()
        self.query = query


class SearchScreen(ModalScreen):

    BINDINGS = [
        Binding("escape", "app.pop_screen", "Close"),
    ]

    def compose(self) -> ComposeResult:

        yield Header()

        with Vertical():

            yield Input(
                placeholder="Search teams or leagues..."
            )

        yield Footer()

    def on_input_submitted(
        self,
        event: Input.Submitted,
    ) -> None:

        self.post_message(
            SearchSubmitted(
                event.value
            )
        )

        self.app.pop_screen()