from dataclasses import dataclass


@dataclass
class Match:
    home_team: str
    away_team: str
    home_score: str
    away_score: str
    status: str