from textual.widgets import Static


class AppHeader(Static):
    def __init__(self):
        super().__init__()

        self.update_header(
            sport="Soccer",
            status="🟢 Connected",
        )

    def update_header(
        self,
        sport: str,
        status: str,
    ) -> None:

        self.update(
            (
                "🏟 SPORTS\n"
                f"{sport}   │   {status}"
            )
        )