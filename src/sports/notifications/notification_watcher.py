from sports.notifications.event_detector import (
    EventDetector,
)
from sports.notifications.notification_service import (
    NotificationService,
)


class NotificationWatcher:

    def __init__(self):

        self.detector = EventDetector()

        self.notifications = NotificationService()

        self.previous_matches = {}

    def update(
        self,
        matches,
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

                    self.notifications.manager.send(
                        notification
                    )

            self.previous_matches[
                match.fixture_id
            ] = match