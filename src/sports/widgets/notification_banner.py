from textual.widgets import Static


class NotificationBanner(Static):
    DEFAULT_MESSAGE = "✓ All systems operational"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)

    def show_notification(
        self,
        title: str,
        message: str,
    ) -> None:

        # Ignore the old title ("🚀 SPORTS")
        # and display only the useful message.

        self.update(f"🔔 {message}")

    def hide_notification(self) -> None:
        self.update(self.DEFAULT_MESSAGE)