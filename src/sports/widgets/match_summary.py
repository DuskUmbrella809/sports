from textual.widgets import Static


class MatchSummary(Static):
    def __init__(self):
        super().__init__()

        self.update_summary(
            league="-",
            country="-",
            fixture_id=0,
            home="-",
            away="-",
            status="Waiting",
            goals=0,
            shots=0,
            on_target=0,
            corners=0,
            yellow=0,
            red=0,
            subs=0,
            home_momentum=50,
            away_momentum=50,
        )

    def _bar(self, percent: int) -> str:
        filled = round(percent / 10)
        return "█" * filled + "░" * (10 - filled)

    def update_summary(
        self,
        *,
        league: str,
        country: str,
        fixture_id: int,
        home: str,
        away: str,
        status: str,
        goals: int,
        shots: int,
        on_target: int,
        corners: int,
        yellow: int,
        red: int,
        subs: int,
        home_momentum: int,
        away_momentum: int,
    ) -> None:

        home_bar = self._bar(home_momentum)
        away_bar = self._bar(away_momentum)

        self.update(
            f"""
🔥 MATCH SUMMARY

🏆 {league}

{home} vs {away}

⏱ Status: {status}

🌍 Country: {country}

🆔 Fixture: {fixture_id}

━━━━━━━━━━━━━━━━━━━━━━━━━━

⚽ Goals.............{goals}

🎯 Shots.............{shots}

🥅 On Target.........{on_target}

🚩 Corners...........{corners}

🟨 Yellow Cards......{yellow}

🟥 Red Cards.........{red}

🔄 Substitutions.....{subs}

━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 MOMENTUM

{home}

{home_bar} {home_momentum}%

{away}

{away_bar} {away_momentum}%
"""
        )