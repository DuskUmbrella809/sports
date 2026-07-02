from textual.widgets import Static


class EventFeed(Static):
    BORDER_TITLE = "🔥 LIVE EVENTS"

    def __init__(self):
        super().__init__()

        self.events: list[str] = []

    def on_mount(self) -> None:
        self.update("Waiting for live events...")

    def update_events(self, events: list[dict]) -> None:
        if not events:
            self.update("No live events.")
            return

        lines = []

        for event in reversed(events):
            minute = event["time"]["elapsed"]
            detail = event["detail"]
            player = event["player"]["name"] if event["player"] else "Unknown"

            lines.append(
                f"{minute}' {detail}\n{player}"
            )

        self.update("\n\n".join(lines))