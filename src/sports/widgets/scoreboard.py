from textual.app import ComposeResult
from textual.containers import Horizontal

from sports.models import Match
from sports.widgets.match_card import MatchCard


class Scoreboard(Horizontal):
    """Displays all current matches."""

    def __init__(self, matches: list[Match]) -> None:
        super().__init__()

        self.matches = matches
        self.cards: list[MatchCard] = []

    def compose(self) -> ComposeResult:
        self.cards.clear()

        for match in self.matches:
            card = MatchCard(match)
            self.cards.append(card)
            yield card

    def update_matches(self, matches: list[Match]) -> None:
        """Refresh every match on screen."""

        self.matches = matches

        self.remove_children()

        self.cards.clear()

        for match in self.matches:
            card = MatchCard(match)
            self.cards.append(card)
            self.mount(card)