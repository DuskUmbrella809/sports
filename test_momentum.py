from sports.models.match_stats import MatchStats
from sports.services.momentum_service import MomentumService

service = MomentumService()

home = MatchStats(
    shots=14,
    shots_on_target=8,
    corners=6,
    yellow_cards=1,
    red_cards=0,
    substitutions=3,
)

away = MatchStats(
    shots=8,
    shots_on_target=3,
    corners=2,
    yellow_cards=2,
    red_cards=0,
    substitutions=3,
)

home_percent, away_percent = service.calculate(
    home,
    away,
)

print(f"Home Momentum: {home_percent}%")
print(f"Away Momentum: {away_percent}%")