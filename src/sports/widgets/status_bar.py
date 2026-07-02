from textual.widgets import Static


class StatusBar(Static):
    def __init__(self):
        super().__init__()

        self.update_status(
            sport="Soccer",
            connection="🟢 Connected",
            updated="Just now",
            favorites=0,
        )

    def update_status(
        self,
        sport: str,
        connection: str,
        updated: str,
        favorites: int,
    ) -> None:

        self.update(
            (
                f" {sport} │ "
                f"{connection} │ "
                f"Updated: {updated} │ "
                f"⭐ {favorites} Favorites │ "
                f"/ Search │ "
                f"f Favorite │ "
                f"q Quit "
            )
        )