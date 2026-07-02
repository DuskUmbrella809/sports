from textual.widgets import Static


class EventFeed(Static):
    BORDER_TITLE = "🔥 LIVE EVENTS"

    ICONS = {
        "Goal": "⚽",
        "Normal Goal": "⚽",
        "Penalty": "🎯",
        "Own Goal": "😬",
        "Yellow Card": "🟨",
        "Red Card": "🟥",
        "Substitution": "🔄",
        "Var": "📺",
    }

    def __init__(self):
        super().__init__()

        self.events: list[dict] = []

    def on_mount(self) -> None:
        self.update(
            "Waiting for live events..."
        )

    def update_events(
        self,
        events: list[dict],
    ) -> None:

        if not events:

            self.update(
                "No live events."
            )

            return

        lines = []

        for event in reversed(events):

            minute = (
                event["time"]["elapsed"]
            )

            detail = (
                event["detail"]
            )

            player = (
                event["player"]["name"]
                if event["player"]
                else "Unknown Player"
            )

            team = (
                event["team"]["name"]
            )

            icon = self.ICONS.get(
                detail,
                "📌",
            )

            lines.append(
                f"{icon} {minute}'  {team}\n"
                f"    {player}"
            )

        self.update(
            "\n\n".join(lines)
        )