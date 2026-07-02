from dataclasses import dataclass


@dataclass
class MatchStats:
    goals: int

    shots: int

    shots_on_target: int

    corners: int

    yellow_cards: int

    red_cards: int

    substitutions: int