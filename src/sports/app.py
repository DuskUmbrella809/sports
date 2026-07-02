from textual.app import App

from sports.screens.dashboard import DashboardScreen
from sports.state.app_state import AppState


class SportsApp(App):
    CSS_PATH = "sports.tcss"

    TITLE = "SPORTS"
    SUB_TITLE = "Live Sports Dashboard"

    def __init__(self):
        super().__init__()

        # Shared application state
        self.state = AppState()

    def on_mount(self) -> None:
        self.push_screen(DashboardScreen())