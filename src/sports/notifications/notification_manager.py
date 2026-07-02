from sports.notifications.history import (
    NotificationHistory,
)
from sports.notifications.models import (
    Notification,
)


class NotificationManager:

    def __init__(self):

        self.history = NotificationHistory()

    def send(
        self,
        notification: Notification,
    ) -> None:

        self.history.add(notification)

        print()

        print("=" * 50)

        print(notification.title)

        print(notification.message)

        print("=" * 50)

        print()