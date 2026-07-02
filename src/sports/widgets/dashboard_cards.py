from textual.app import ComposeResult
from textual.containers import Horizontal

from sports.widgets.dashboard_card import DashboardCard


class DashboardCards(Horizontal):

    def compose(self) -> ComposeResult:

        self.live = DashboardCard(
            "LIVE",
            "0",
            "🔥",
        )

        self.goals = DashboardCard(
            "GOALS",
            "0",
            "⚽",
        )

        self.favorites = DashboardCard(
            "FAVORITES",
            "0",
            "⭐",
        )

        self.connection = DashboardCard(
            "STATUS",
            "🟢",
            "🌐",
        )

        yield self.live
        yield self.goals
        yield self.favorites
        yield self.connection