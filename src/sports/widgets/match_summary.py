from textual.widgets import Static


class MatchSummary(Static):
    def __init__(self):
        super().__init__()

        self.update_summary(
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
        )

    def update_summary(
        self,
        *,
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
    ) -> None:

        self.update(
            f"""
🔥 MATCH SUMMARY

{home} vs {away}

Status: {status}

━━━━━━━━━━━━━━━━━━━━━━━━━━

⚽ Goals.............{goals}

🎯 Shots.............{shots}

🥅 On Target.........{on_target}

🚩 Corners...........{corners}

🟨 Yellow Cards......{yellow}

🟥 Red Cards.........{red}

🔄 Substitutions.....{subs}
"""
        )