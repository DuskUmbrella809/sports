from collections import deque

from sports.notifications.models import Notification


class NotificationHistory:

    def __init__(
        self,
        max_items: int = 100,
    ):

        self._notifications = deque(
            maxlen=max_items
        )

    def add(
        self,
        notification: Notification,
    ) -> None:

        self._notifications.appendleft(
            notification
        )

    def all(
        self,
    ) -> list[Notification]:

        return list(
            self._notifications
        )

    def unread(
        self,
    ) -> list[Notification]:

        return [
            n
            for n in self._notifications
            if not n.read
        ]

    def mark_all_read(
        self,
    ) -> None:

        for notification in self._notifications:
            notification.read = True

    def clear(
        self,
    ) -> None:

        self._notifications.clear()