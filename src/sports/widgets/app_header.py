from textual.widgets import Static


class AppHeader(Static):
    DEFAULT_CSS = """
    AppHeader {
        height: 1;
        padding: 0 2;
        margin: 0;
        content-align: left middle;
    }
    """

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
            f"🏟 SPORTS    ⚽ {sport}    {status}"
        )