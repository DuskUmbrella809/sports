from textual.widgets import Static


class AppHeader(Static):
    def __init__(self):
        super().__init__(id="app-header")

        self.update_header(
            sport="Soccer",
            status="🟢 CONNECTED",
        )

    def update_header(
        self,
        sport: str,
        status: str,
    ) -> None:

        self.update(
            f"""
🏟  SPORTS                                        {status}

Live Sports Dashboard

Current Sport: ⚽ {sport}
"""
        )