from sports.models import Match
from sports.notifications.event_detector import (
    EventDetector,
)

detector = EventDetector()

before = Match(
    fixture_id=1,
    league="Premier League",
    country="England",
    home_team="Manchester City",
    away_team="Arsenal",
    home_score="1",
    away_score="1",
    status="2H",
)

after = Match(
    fixture_id=1,
    league="Premier League",
    country="England",
    home_team="Manchester City",
    away_team="Arsenal",
    home_score="2",
    away_score="1",
    status="2H",
)

notifications = detector.detect(
    before,
    after,
)

print(notifications)