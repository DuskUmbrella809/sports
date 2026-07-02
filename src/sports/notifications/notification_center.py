from sports.notifications.models import Notification


class NotificationCenter:
    """
    Central hub for every notification generated
    by SPORTS.
    """

    def __init__(self):

        self.history: list[Notification] = []

        self.listeners = []

    def subscribe(
        self,
        listener,
    ) -> None:

        self.listeners.append(listener)

    def publish(
        self,
        notification: Notification,
    ) -> None:

        self.history.append(notification)

        for listener in self.listeners:

            listener(notification)

    def latest(self) -> Notification | None:

        if not self.history:
            return None

        return self.history[-1]

    def clear(self) -> None:

        self.history.clear()