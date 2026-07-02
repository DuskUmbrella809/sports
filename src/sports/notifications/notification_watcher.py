from sports.notifications.event_detector import (
    EventDetector,
)
from sports.notifications.notification_center import (
    NotificationCenter,
)
from sports.models import Match


class NotificationWatcher:
    """
    Watches live matches for score changes and publishes
    notifications whenever an event is detected.
    """

    def __init__(
        self,
        center: NotificationCenter,
    ) -> None:

        self.center = center

        self.detector = EventDetector()

        self.previous_matches: dict[int, Match] = {}

    def update(
        self,
        matches: list[Match],
    ) -> None:

        for match in matches:

            previous = self.previous_matches.get(
                match.fixture_id
            )

            if previous is not None:

                notifications = self.detector.detect(
                    previous,
                    match,
                )

                for notification in notifications:

                    self.center.publish(
                        notification
                    )

            self.previous_matches[
                match.fixture_id
            ] = match