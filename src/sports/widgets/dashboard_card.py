from textual.widgets import Static


class DashboardCard(Static):
    def __init__(
        self,
        title: str,
        value: str,
        icon: str,
    ):
        super().__init__()

        self.title = title
        self.value = value
        self.icon = icon

        self.render_card()

    def render_card(self) -> None:
        self.update(
            f"""
{self.icon} {self.title}

{self.value}
"""
        )

    def set_value(
        self,
        value: str,
    ) -> None:

        self.value = value

        self.render_card()