from sports.models import Match
from sports.notifications.models import (
    Notification,
    NotificationType,
)


class EventDetector:

    def detect(
        self,
        previous: Match,
        current: Match,
    ) -> list[Notification]:

        notifications: list[Notification] = []

        previous_home = int(previous.home_score)
        previous_away = int(previous.away_score)

        current_home = int(current.home_score)
        current_away = int(current.away_score)

        # Home goal
        if current_home > previous_home:

            notifications.append(
                Notification(
                    notification_type=NotificationType.GOAL,
                    fixture_id=current.fixture_id,
                    title="⚽ GOAL",
                    message=(
                        f"{current.home_team}\n\n"
                        f"{current.home_team} "
                        f"{current.home_score}"
                        f"-"
                        f"{current.away_score} "
                        f"{current.away_team}"
                    ),
                )
            )

        # Away goal
        if current_away > previous_away:

            notifications.append(
                Notification(
                    notification_type=NotificationType.GOAL,
                    fixture_id=current.fixture_id,
                    title="⚽ GOAL",
                    message=(
                        f"{current.away_team}\n\n"
                        f"{current.home_team} "
                        f"{current.home_score}"
                        f"-"
                        f"{current.away_score} "
                        f"{current.away_team}"
                    ),
                )
            )

        return notifications