from sports.models.match_stats import MatchStats


class MomentumService:
    """
    Calculates live momentum from match statistics.

    Weighting:
    - Goals: 10
    - Shots on Target: 5
    - Shots: 3
    - Corners: 2
    """

    GOAL_WEIGHT = 10
    SHOT_ON_TARGET_WEIGHT = 5
    SHOT_WEIGHT = 3
    CORNER_WEIGHT = 2

    def _score(
        self,
        stats: MatchStats,
    ) -> int:
        return (
            stats.goals * self.GOAL_WEIGHT
            + stats.shots_on_target
            * self.SHOT_ON_TARGET_WEIGHT
            + stats.shots * self.SHOT_WEIGHT
            + stats.corners * self.CORNER_WEIGHT
        )

    def calculate(
        self,
        home: MatchStats,
        away: MatchStats,
    ) -> tuple[int, int]:

        home_score = self._score(home)
        away_score = self._score(away)

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