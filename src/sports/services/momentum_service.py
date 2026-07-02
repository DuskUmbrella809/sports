from sports.models.match_stats import MatchStats


class MomentumService:
    """
    Calculates a simple momentum score based on
    live match statistics.
    """

    def calculate(
        self,
        home: MatchStats,
        away: MatchStats,
    ) -> tuple[int, int]:

        home_score = (
            home.shots_on_target * 5
            + home.shots * 2
            + home.corners
        )

        away_score = (
            away.shots_on_target * 5
            + away.shots * 2
            + away.corners
        )

        total = home_score + away_score

        if total == 0:
            return (50, 50)

        home_percent = round(
            home_score / total * 100
        )

        away_percent = 100 - home_percent

        return (
            home_percent,
            away_percent,
        )