from textual.widgets import Static


class EventFeed(Static):
    BORDER_TITLE = "🔥 LIVE EVENTS"

    ICONS = {
        "Goal": "⚽",
        "Normal Goal": "⚽",
        "Penalty": "🎯",
        "Penalty Goal": "🎯",
        "Own Goal": "😬",
        "Yellow Card": "🟨",
        "Red Card": "🟥",
        "Second Yellow Card": "🟨🟥",
        "Substitution": "🔄",
        "Var": "📺",
        "VAR": "📺",
        "Missed Penalty": "❌",
    }

    def __init__(self):
        super().__init__()

    def on_mount(self) -> None:
        self.update("Waiting for live events...")

    def update_events(
        self,
        events: list[dict],
    ) -> None:

        if not events:
            self.update(
                "🏟 No live events yet.\n\n"
                "Events will appear here during the match."
            )
            return

        lines: list[str] = []

        for event in reversed(events):

            minute = event.get("time", {}).get(
                "elapsed",
                "?",
            )

            detail = event.get(
                "detail",
                "Event",
            )

            player = (
                event.get("player") or {}
            ).get(
                "name",
                "Unknown Player",
            )

            team = (
                event.get("team") or {}
            ).get(
                "name",
                "",
            )

            icon = self.ICONS.get(
                detail,
                "📌",
            )

            lines.append(
                "\n".join(
                    [
                        f"{icon} {minute}'  {detail}",
                        f"👤 {player}",
                        f"🏳 {team}",
                        "────────────────────────",
                    ]
                )
            )

        self.update("\n".join(lines))