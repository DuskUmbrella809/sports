from sports.models import Match

from sports.notifications.notification_watcher import (
    NotificationWatcher,
)

watcher = NotificationWatcher()

first = [
    Match(
        fixture_id=1,
        league="Premier League",
        country="England",
        home_team="Manchester City",
        away_team="Arsenal",
        home_score="1",
        away_score="1",
        status="2H",
    )
]

second = [
    Match(
        fixture_id=1,
        league="Premier League",
        country="England",
        home_team="Manchester City",
        away_team="Arsenal",
        home_score="2",
        away_score="1",
        status="2H",
    )
]

print("First update...")
watcher.update(first)

print()

print("Second update...")
watcher.update(second)