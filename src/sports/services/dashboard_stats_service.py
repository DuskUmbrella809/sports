from sports.models import Match


class DashboardStatsService:
    """Builds the statistics shown on the dashboard cards."""

    def build(
        self,
        matches: list[Match],
        favorites: int,
    ) -> dict[str, int | str]:

        live_matches = len(matches)

        total_goals = 0

        for match in matches:
            try:
                home = int(match.home_score)
                away = int(match.away_score)
                total_goals += home + away

            except (ValueError, TypeError):
                # Ignore malformed scores
                continue

        return {
            "live": live_matches,
            "goals": total_goals,
            "favorites": favorites,
            "status": "🟢 ONLINE",
        }