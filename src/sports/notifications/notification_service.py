from sports.notifications.models import (
    Notification,
    NotificationType,
)
from sports.notifications.notification_manager import (
    NotificationManager,
)


class NotificationService:

    def __init__(self):

        self.manager = NotificationManager()

    def send_system_message(
        self,
        message: str,
    ) -> None:

        notification = Notification(
            notification_type=NotificationType.SYSTEM,
            title="🟢 SPORTS",
            message=message,
        )

        self.manager.send(notification)

    def goal(
        self,
        fixture_id: int,
        team: str,
        scorer: str,
        minute: str,
    ) -> None:

        notification = Notification(
            notification_type=NotificationType.GOAL,
            fixture_id=fixture_id,
            title="⚽ GOAL",
            message=(
                f"{team}\n\n"
                f"{scorer} ({minute}')"
            ),
        )

        self.manager.send(notification)