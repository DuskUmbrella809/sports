from dataclasses import dataclass


@dataclass
class Match:
    fixture_id: int

    league: str
    country: str

    home_team: str
    away_team: str

    home_score: str
    away_score: str

    status: str