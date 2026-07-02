from textual.widgets import Static


class AppHeader(Static):
    def __init__(self):
        super().__init__(id="app-header")

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
            "\n"
            "🏟  SPORTS\n"
            "\n"
            f"   {sport}    │    {status}\n"
        )