from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.timer import Timer

from sports.models import Match
from sports.services.dashboard_stats_service import DashboardStatsService
from sports.services.event_service import EventService
from sports.services.favorites_service import FavoritesService
from sports.services.scoreboard_service import ScoreboardService
from sports.services.stats_service import StatsService
from sports.widgets.status_bar import StatusBar

from sports.widgets.app_header import AppHeader
from sports.widgets.dashboard_cards import DashboardCards
from sports.widgets.event_feed import EventFeed
from sports.widgets.match_summary import MatchSummary
from sports.widgets.match_table import (
    FavoriteRequested,
    MatchSelected,
    MatchTable,
)
from sports.widgets.sidebar import (
    Sidebar,
    SportSelected,
)
from sports.widgets.notification_banner import (
    NotificationBanner,
)
from sports.notifications.notification_center import (
    NotificationCenter,
)

from sports.notifications.notification_watcher import (
    NotificationWatcher,
)
from sports.services.momentum_service import (
    MomentumService,
)


class DashboardScreen(Screen):
    def compose(self) -> ComposeResult:
        self.scoreboard_service = ScoreboardService()
        self.event_service = EventService()
        self.favorites_service = FavoritesService()
        self.dashboard_stats_service = DashboardStatsService()
        self.stats_service = StatsService()
        self.momentum_service = MomentumService()

        self.matches = self.scoreboard_service.get_matches()

        self.dashboard_cards = DashboardCards()

        self.match_table = MatchTable(self.matches)
        self.match_summary = MatchSummary()
        self.event_feed = EventFeed()
        self.notification_banner = NotificationBanner()
        self.notification_center = NotificationCenter()

        self.notification_watcher = NotificationWatcher(
             self.notification_center
      )

        self.header = AppHeader()
        self.status_bar = StatusBar()

        self.selected_match: Match | None = None
        self.event_timer: Timer | None = None

        yield self.header

        with Vertical():

            with Horizontal():

                yield Sidebar()

                with Vertical():

                    yield self.dashboard_cards

                    yield self.notification_banner

                    yield self.match_table

                    yield self.match_summary

                    yield self.event_feed

            yield self.status_bar

    def on_mount(self) -> None:
        self.set_interval(10, self.refresh_dashboard)

        if self.matches:
            self.selected_match = self.matches[0]
            self.load_events()
            self.update_match_summary()

        self.update_dashboard_cards()
         
        self.notification_center.subscribe(
            self.notification_banner.show_notification
        )
        
        self.notification_banner.show_notification(
    "🚀 SPORTS",
    "Notification Banner Online!",
)

        self.status_bar.update_status(
            sport="Soccer",
            connection="🟢 Connected",
            updated="Just now",
            favorites=self.favorites_service.count(),
        )

    def refresh_dashboard(self) -> None:

        self.matches = self.scoreboard_service.get_matches()

        self.notification_watcher.update(
            self.matches
    )

        self.match_table.update_matches(
            self.matches
    )

        self.update_dashboard_cards()

        if self.selected_match:

            self.update_match_summary()

            self.load_events()

    def update_dashboard_cards(self) -> None:
        """Update the dashboard statistics."""

        self.dashboard_cards.live.set_value(
            str(len(self.matches))
        )

        goals = sum(
            int(match.home_score)
            + int(match.away_score)
            for match in self.matches
        )

        self.dashboard_cards.goals.set_value(
            str(goals)
        )

        self.dashboard_cards.favorites.set_value(
            str(
                self.favorites_service.count()
            )
        )

        self.dashboard_cards.connection.set_value(
            "🟢"
        )

    def load_events(self) -> None:
        if self.selected_match is None:
            return

        try:
            events = self.event_service.get_events(
                self.selected_match.fixture_id
            )

            self.event_feed.update_events(events)

        except Exception:
            self.event_feed.update(
                "⚠ Unable to load live events."
            )

    def update_match_summary(self) -> None:
        if self.selected_match is None:
            return

        stats = self.stats_service.get_stats(
            self.selected_match.fixture_id
        )

        self.match_summary.update_summary(
            home=self.selected_match.home_team,
            away=self.selected_match.away_team,
            status=self.selected_match.status,
            goals=(
                int(self.selected_match.home_score)
                + int(self.selected_match.away_score)
            ),
            shots=stats.shots,
            on_target=stats.shots_on_target,
            corners=stats.corners,
            yellow=stats.yellow_cards,
            red=stats.red_cards,
            subs=stats.substitutions,
            home_momentum=50,
            away_momentum=50,
        )

    def on_match_selected(
        self,
        message: MatchSelected,
    ) -> None:

        self.selected_match = message.match

        self.update_match_summary()

        if self.event_timer:
            self.event_timer.stop()

        self.event_timer = self.set_timer(
            0.5,
            self.load_events,
        )

    def on_favorite_requested(
        self,
        message: FavoriteRequested,
    ) -> None:

        match = message.match

        if self.favorites_service.is_favorite(
            match.fixture_id
        ):

            self.favorites_service.remove(
                match.fixture_id
            )

            self.event_feed.update(
                f"⭐ Removed from favorites\n\n"
                f"{match.home_team} vs {match.away_team}"
            )

        else:

            self.favorites_service.add(
                match.fixture_id
            )

            self.event_feed.update(
                f"⭐ Added to favorites\n\n"
                f"{match.home_team} vs {match.away_team}"
            )

        self.update_dashboard_cards()

        self.status_bar.update_status(
            sport=self.scoreboard_service.current_provider().title(),
            connection="🟢 Connected",
            updated="Just now",
            favorites=self.favorites_service.count(),
        )

    def on_sport_selected(
        self,
        message: SportSelected,
    ) -> None:

        if message.sport == "favorites":

            favorite_ids = (
                self.favorites_service.get_all()
            )

            self.matches = [
                match
                for match in self.scoreboard_service.get_matches()
                if match.fixture_id in favorite_ids
            ]

            self.match_table.update_matches(
                self.matches
            )

            self.update_dashboard_cards()

            self.header.update_header(
                sport="Favorites",
                status="⭐ FAVORITES",
            )

            self.status_bar.update_status(
                sport="Favorites",
                connection="⭐ Favorites",
                updated="Just now",
                favorites=self.favorites_service.count(),
            )

            self.event_feed.update(
                "⭐ Viewing favorite matches."
            )

            return

        if message.sport == "live":

            self.matches = (
                self.scoreboard_service.get_matches()
            )

            self.match_table.update_matches(
                self.matches
            )

            self.update_dashboard_cards()

            self.header.update_header(
                sport="Live",
                status="🔴 LIVE",
            )

            self.status_bar.update_status(
                sport="Live",
                connection="🟢 Connected",
                updated="Just now",
                favorites=self.favorites_service.count(),
            )

            self.event_feed.update(
                "🔴 Showing all live matches."
            )

            return

        try:

            self.scoreboard_service.set_provider(
                message.sport
            )

            self.matches = (
                self.scoreboard_service.get_matches()
            )

            self.match_table.update_matches(
                self.matches
            )

            self.update_dashboard_cards()

            sport_name = (
                message.sport
                .replace(
                    "formula1",
                    "Formula 1",
                )
                .title()
            )

            self.header.update_header(
                sport=sport_name,
                status="🟢 CONNECTED",
            )

            self.status_bar.update_status(
                sport=sport_name,
                connection="🟢 Connected",
                updated="Just now",
                favorites=self.favorites_service.count(),
            )

            if self.matches:

                self.selected_match = self.matches[0]

                self.update_match_summary()

                self.load_events()

            else:

                self.match_summary.update_summary(
                    home="-",
                    away="-",
                    status="No Games",
                    goals=0,
                    shots=0,
                    on_target=0,
                    corners=0,
                    yellow=0,
                    red=0,
                    subs=0,
                )

                self.event_feed.update(
                    f"🏆 Switched to {sport_name}\n\n"
                    "No games available."
                )

        except Exception as e:

            self.event_feed.update(
                f"❌ Failed to switch provider\n\n{e}"
            )