from textual.widgets import Static


class NotificationBanner(Static):

    DEFAULT_MESSAGE = "No new notifications."

    def __init__(self):

        super().__init__(self.DEFAULT_MESSAGE)

        self.display = False

    def show_notification(
        self,
        title: str,
        message: str,
    ) -> None:

        self.update(
            f"{title}\n\n{message}"
        )

        self.display = True

    def hide_notification(
        self,
    ) -> None:

        self.update(
            self.DEFAULT_MESSAGE
        )

        self.display = False