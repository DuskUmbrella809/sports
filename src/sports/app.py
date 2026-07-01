from textual.app import App

from sports.screens.dashboard import DashboardScreen


class SportsApp(App):
    CSS_PATH = "sports.tcss"

    TITLE = "SPORTS"
    SUB_TITLE = "Live Sports Dashboard"

    def on_mount(self) -> None:
        self.push_screen(DashboardScreen())